# Upload something from local to GCS
`gcloud storage cp test.txt gs://<your_path>/`

# Sync data between local and GCS
gcloud storage rsync -r ./ gs://<your_path>/rsync/ --delete-unmatched-destination-objects



# Stop the compute instance before changing service account
gcloud compute instances stop <your_compute_engine_name> --zone=<your_compute_engine_zone>

# Set service account with required scopes (cloud-platform for GCP services, drive for Google Drive access)
gcloud compute instances set-service-account <your_compute_engine_name> \
  --zone=<your_compute_engine_zone> \
  --scopes=https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/drive

# Start the compute instance with the new service account and scopes
gcloud compute instances start <your_compute_engine_name> --zone=<your_compute_engine_zone>
