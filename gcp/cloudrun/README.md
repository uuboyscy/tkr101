# Services

## Artifact Registry (Like a DockerHub on GCP)

- Get authenticated
```bash
gcloud auth login  # Login via your user account
gcloud auth configure-docker asia-east1-docker.pkg.dev  # Authenticate Docker registry
gcloud auth print-access-token | docker login -u oauth2accesstoken --password-stdin asia-east1-docker.pkg.dev  # Docker login with authentication above (If your are using Windows, you should convert the command yourself)
```

- Build and push image
  - Create a python file
  - Create a Dockerfile
  - Build and push Docker image:
    - `docker buildx build --platform linux/amd64 -t asia-east1-docker.pkg.dev/<your-project>/tkr101-repo/bigquery-demo:latest --push .`

## Cloud Run Job (Run job, from Docker image)
- Select the image you built
- Create and execute the job to see if it works
- If testing execution via service account locally is required, run:
  - `gcloud auth application-default login --impersonate-service-account=<your-service-account>`

### IaC
```bash
gcloud run jobs deploy bigquery-demo-job-2 --image=asia-east1-docker.pkg.dev/<your-project_id>/tkr101-repo/bigquery-demo:latest --service-account=bigquery-user@<your-project-id>.iam.gserviceaccount.com --region=asia-east1
```

## Cloud Run Service (Web service, from Docker image)


## Remote function
```sql
CREATE FUNCTION `notional-zephyr-229707.tkr101.remote_add`(x INT64, y INT64) RETURNS INT64
REMOTE WITH CONNECTION `notional-zephyr-229707.asia-east1.model-conn`
OPTIONS (
  endpoint = 'https://remote-add-30300274673.asia-east1.run.app'
);

SELECT
  val,
  `notional-zephyr-229707.tkr101`.remote_add(val, 2)
FROM
  UNNEST([NULL,2,3,5,8]) AS val;
```

# Note
- `gcloud auth login` is for "user" authentication to use gcloud command
- `gcloud auth application-default` is for application, e.g. Python or any other programming language execution