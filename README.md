# Data Pipeline with Reddit, Airflow, Celery, Postgres, S3, AWS Glue, Athena, and Redshift

This project provides a comprehensive solution to extract, transform, and load (ETL) Reddit data into a Redshift data warehouse. The pipeline uses a combination of powerful tools and services including Apache Airflow, Celery, PostgreSQL, Amazon S3, AWS Glue, Athena, and Redshift, ensuring efficient and scalable data processing.

## Overview

The goal of this data pipeline is to:

1. **Extract** data from Reddit using its API.
2. **Store** the raw data in an S3 bucket via Airflow.
3. **Transform** the raw data using AWS Glue and Amazon Athena.
4. **Load** the transformed data into Amazon Redshift for analytics and querying.

This pipeline automates the entire process of Reddit data ingestion, transformation, and loading, making it easy to perform data analysis and derive insights.

## Architecture

![RedditDataEngineering](https://github.com/user-attachments/assets/ed6b9b4f-b699-4ca9-b444-ff17a2f851c8)


The architecture is composed of the following components:

- **Reddit API**: The data source for fetching Reddit posts and comments.
- **Apache Airflow & Celery**: These work together to orchestrate and distribute the ETL tasks.
- **PostgreSQL**: Serves as a temporary storage solution and metadata management layer.
- **Amazon S3**: Storage for the raw data fetched from Reddit.
- **AWS Glue**: Used for data cataloging and running ETL jobs for data transformation.
- **Amazon Athena**: A query service to run SQL-based transformations on data stored in S3.
- **Amazon Redshift**: The final destination for the transformed data, serving as a data warehouse for querying and analytics.

## Prerequisites

Before setting up the pipeline, ensure you have the following:

- **AWS Account** with permissions to use S3, Glue, Athena, and Redshift.
- **Reddit API credentials** for data access.
- **Docker** installed on your system to run containers.
- **Python 3.9** or higher for the development environment.

## System Setup

### Step 1: Clone the repository

```bash
git clone https://github.com/airscholar/RedditDataEngineering.git
```
### Step 2: Create and activate a virtual environment
```
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```
Step 4: Configure the application
```
mv config/config.conf.example config/config.conf
```

### Step 5: Start the containers

```bash
docker-compose up -d
```

### Step 6: Launch the Airflow web UI

Once the services are up and running, access the Apache Airflow web UI at:

http://localhost:8080

From here, you can monitor and manage the data pipeline tasks.


# AWS ETL JOB Scripts
## This script add after first (# script generated for node amazon s3) <<< commnet on codebase
```
from pyspark.sql.functions import concat_ws
from awsglue import DynamicFrame
df = AmazonS3_node1234567890123.toDF()

#concatenate the three columns into a single column
df_combined = df.withColumn('ESS_updated', concat_WS('-', df['edited'], df['spoiler'], df['sticked']))
df_combined = df.withColumn.drop('edited', 'spoiler', 'stickied')

#convert back to DynamicFrame

S3bucket_node_combined = DynamicFrame.fromDF(df_combined, glueContext, 'S3bucket_node_combined')

# change the frame= to S3bucket_node_combined```
