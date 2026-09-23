# 🛒 E-commerce Data Engineering Pipeline

> End-to-End Data Engineering Project using Python, SQL Server, Docker and Apache Airflow

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?logo=pandas)
![SQL Server](https://img.shields.io/badge/SQL%20Server-2022-red?logo=microsoftsqlserver)
![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED?logo=docker)
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-Orchestration-017CEE?logo=apacheairflow)
![PyODBC](https://img.shields.io/badge/PyODBC-Database%20Connection-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## 📌 Overview

This project is an **end-to-end Data Engineering pipeline** built to process and transform Brazilian e-commerce transaction data into a structured data warehouse for analytics.

The project uses the **Brazilian E-Commerce Public Dataset by Olist**, containing information about orders, customers, products, sellers, payments, reviews and other transactional entities.

The main objective is to simulate a practical Data Engineering workflow:

```text
Raw CSV Dataset
       │
       ▼
Data Ingestion
       │
       ▼
Python + Pandas
       │
       ▼
SQL Server
       │
       ▼
Bronze Layer
       │
       ▼
Silver Layer
       │
       ▼
Gold Layer
       │
       ▼
Data Warehouse
       │
       ▼
Analytics
