# Platform for Amazon SQS Events Visualization

This platform is designed to consume Amazon SNS Events, facilitating their storage and visualization.

**[Check out the website in production](https://fetch-rewards-siddarth-sairaj.netlify.app/)**

## Current Architecture

![arch drawio](https://github.com/boatcow/AWS_SQS_DE_ASSESSMENT/assets/40225095/d05306b7-883d-4f2e-a37d-d8e47d382ddb)


## Features

1. **Load Events to Database**: Extracts events from SQS, transforms the data, and loads it into a Postgres database.
2. **View Records**: Allows users to visualize the events stored in the Postgres database. Within this feature, there's an option to 'View Unmasked Data' to reveal any Personal Identifiable Information (PII).

## Screenshots

1. **Instructions Screen**: View functions of this platform.
<img width="1439" alt="inscructions" src="https://github.com/boatcow/AWS_SQS_DE_ASSESSMENT/assets/40225095/80621141-03c2-47f2-9ca0-088373858a2e">


2. **Load Events Interface**: Decide the number of events you want to push to the database.
<img width="1439" alt="load_events" src="https://github.com/boatcow/AWS_SQS_DE_ASSESSMENT/assets/40225095/a23b856e-751c-4d68-98de-5e523e5804f1">


3. **All Records View**: A glance at all the events loaded into the database.
<img width="1439" alt="view_events" src="https://github.com/boatcow/AWS_SQS_DE_ASSESSMENT/assets/40225095/315cf63f-0f79-435a-9fb4-df8fc40bcbba">

4. **Unmask PII Data View**: Allows for a deeper dive into the unmasked PII data.
<img width="1439" alt="unmask" src="https://github.com/boatcow/AWS_SQS_DE_ASSESSMENT/assets/40225095/99d02125-f9d7-439c-bd5d-cb9381821c29">

## Local Setup Instructions

If you wish to set up the platform locally, follow these steps:

**Step 1**: Setting up Docker-Compose:
- Ensure you have both Docker and Docker Compose installed. If not, you can download and install from [Docker's official website](https://www.docker.com/get-started).
- Verify the installation:
  ```bash
  docker --version
  docker-compose --version
  ```
- Clone the repository and navigate to the project directory where `docker-compose.yml` is located.

**Step 2**: 
```bash
docker-compose up
```

**Step 3**: 
Navigate to `localhost:8080` on your preferred browser to access and utilize the platform.

## Next Steps
Modify the system to a more Scalable Architecture with custom DNS, Similar to one below
![arch drawio (1)](https://github.com/boatcow/AWS_SQS_DE_ASSESSMENT/assets/40225095/0f4488c9-ee21-4610-bf18-f0dd89f6eca0)


---

Thank you for choosing our platform. If you encounter any issues or require assistance, please raise an issue on GitHub. Your feedback is highly appreciated!
