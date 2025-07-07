# AWS Data Engineering: Hybrid Streaming and Batch Pipeline

A complete end-to-end data engineering project demonstrating both **real-time streaming** and **batch ingestion** using AWS services, built with production-grade code and modular components.

---

# Introduction & Goals

This project simulates a real-world AWS Data Engineering scenario by combining **streaming pipelines** with **batch ingestion pipelines** to process retail transaction data.

- **Dataset:** Synthetic e-commerce transaction data.
- **Tools:** AWS Lambda, API Gateway, Kinesis, DynamoDB, Firehose, S3, Redshift.
- **Goal:** 
  - Real-time delivery of streaming data to Redshift and DynamoDB.
  - Batch ingestion of historical CSV data via API into the same pipeline.
  - Support for dashboard reporting and customer-level data views.

---

# Contents

- [The Data Set](#the-data-set)
- [Used Tools](#used-tools)
  - [Connect](#connect)
  - [Buffer](#buffer)
  - [Processing](#processing)
  - [Storage](#storage)
- [Pipelines](#pipelines)
  - [Stream Processing](#stream-processing)
    - [Storing Data Stream](#storing-data-stream)
    - [Processing Data Stream](#processing-data-stream)
  - [Batch Processing](#batch-processing)
- [Demo](#demo)
- [Conclusion](#conclusion)

---

# The Data Set

- A sample CSV dataset `TestSample.csv` simulating retail transactions.
- Fields: `InvoiceNo`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `UnitPrice`, `CustomerID`, `Country`.
- **Chosen for its resemblance to real transactional systems** and ability to simulate customer and inventory flows.
- Used for both **batch ingestion** and **stream simulation** via API.

---

# Used Tools

## Connect
- **API Gateway**: Entry point for both real-time and batch data via POST/GET requests.
- **Lambda**: Lightweight serverless compute to handle API events.

## Buffer
- **Kinesis Data Stream**: Captures incoming records in near real-time.
- **Kinesis Firehose**: Buffers and delivers data to storage destinations.

## Processing
- **Lambda**:
  - `kinesis_dynamo_api_lambda.py`: Processes GET/POST via API Gateway.
  - `kinesis_to_dynamodb.py`: Stores real-time data to DynamoDB.
  - `kinesis_to_s3.py`: Writes incoming records to S3 for Redshift.

## Storage
- **DynamoDB**: Stores customer-specific data for quick lookup.
- **S3**: Intermediate storage bucket for Firehose delivery.
- **Redshift**: Final sink for dashboard and analytical queries.

---

# Pipelines

## Stream Processing

### Storing Data Stream
- `API Gateway → Lambda → Kinesis Stream (APIData) → Firehose → S3 → Redshift`
- Real-time ingestion of transaction records.

### Processing Data Stream
- Additional Lambda functions consume Kinesis data:
  - `kinesis_to_dynamodb.py`: Writes real-time transactional updates to DynamoDB for customer-facing applications.
  - `kinesis_to_s3.py`: Writes newline-separated JSON to S3 buckets for Redshift COPY.

## Batch Processing
- `csv_to_api_ingest.py`: Python script to send historical CSV data via API to the same streaming pipeline.
- Useful for bootstrapping datasets or simulating streaming from static files.

---

# Demo

> You can insert a demo video or link here once you’ve created one.

---

# Conclusion

This project successfully demonstrates a hybrid data engineering pipeline using core AWS services without relying on external orchestration tools. Key takeaways:

- Learned to handle streaming and batch ingestion in parallel.
- Designed modular Lambda functions for ingestion and transformation.
- Set up IAM policies, JSONPath configs, and Redshift schema mappings manually.
- Faced challenges debugging payload mismatches and permissions — but overcame them with structured testing and modular development.

---
