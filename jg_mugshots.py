from google.cloud import aiplatform
from google.cloud.aiplatform.gapic.schema import predict
from google.cloud import storage
import base64
from config import GCP_PROJECT_NAME, GCP_BUCKET_NAME


def create_dataset(project, location, display_name):
    aiplatform.init(project=project, location=location)

    # Verify the bucket exists and list its contents
    storage_client = storage.Client(project=project)
    bucket = storage_client.get_bucket(GCP_BUCKET_NAME)
    blobs = list(bucket.list_blobs())

    if not blobs:
        raise ValueError(f"No files found in gs://{GCP_BUCKET_NAME}/")

    # Use the root of the bucket as the GCS source
    gcs_source = f"gs://{GCP_BUCKET_NAME}/"

    dataset = aiplatform.ImageDataset.create(
        display_name=display_name,
        gcs_source=gcs_source,
        import_schema_uri=aiplatform.schema.dataset.ioformat.image.single_label_classification
    )
    return dataset

def train_model(project, location, dataset, model_display_name):
    aiplatform.init(project=project, location=location)
    job = aiplatform.AutoMLImageTrainingJob(
        display_name=model_display_name,
        prediction_type="classification",
        multi_label=False,
        model_type="CLOUD",
        base_model=None
    )
    model = job.run(
        dataset=dataset,
        model_display_name=model_display_name,
        training_fraction_split=0.8,
        validation_fraction_split=0.1,
        test_fraction_split=0.1,
        budget_milli_node_hours=8000,
    )
    return model

def predict_image(project, location, model_id, image_file):
    aiplatform.init(project=project, location=location)
    endpoint = aiplatform.Endpoint(model_id)
    
    with open(image_file, "rb") as f:
        file_content = f.read()
    
    encoded_content = base64.b64encode(file_content).decode("utf-8")
    instance = predict.instance.ImageClassificationPredictionInstance(
        content=encoded_content,
    ).to_value()
    instances = [instance]
    
    prediction = endpoint.predict(instances=instances)
    return prediction

# Usage
project = GCP_PROJECT_NAME
location = "us-central1"
dataset_name = "coffee_cup_dataset"
model_name = "coffee_cup_detector"

# Create dataset
dataset = create_dataset(project, location, dataset_name)

# Train model
model = train_model(project, location, dataset, model_name)

# Make prediction
image_file = "jg-mugshot.jpeg"
prediction = predict_image(project, location, model.name, image_file)
print(prediction)