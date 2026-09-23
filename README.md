# 🛒 E-Commerce Data Engineering Platform

<p align="center">

<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=for-the-badge&logo=pandas&logoColor=white">
<img src="https://img.shields.io/badge/SQL%20Server-2022-CC2927?style=for-the-badge&logo=microsoftsqlserver&logoColor=white">
<img src="https://img.shields.io/badge/Docker-Containerization-2496ED?style=for-the-badge&logo=docker&logoColor=white">
<img src="https://img.shields.io/badge/Airflow-3.3.2-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white">
<img src="https://img.shields.io/badge/ETL-Pipeline-orange?style=for-the-badge">
<img src="https://img.shields.io/badge/Data%20Warehouse-SQL%20Server-blue?style=for-the-badge">

</p>

---

# 📌 1. Project Overview

This project is an end-to-end **Data Engineering project** designed to simulate a real-world e-commerce data platform.

The project uses the Brazilian E-Commerce Public Dataset from Olist and builds a complete data pipeline from raw CSV files to an analytical Data Warehouse.

The main technologies used in this project are:

- Python
- Pandas
- PyODBC
- Microsoft SQL Server 2022
- Docker
- Docker Compose
- Apache Airflow
- PostgreSQL
- Redis
- SQL

The project focuses on the complete Data Engineering workflow:

```text
                    RAW DATA
                       │
                       ▼
              ┌─────────────────┐
              │   CSV DATASETS  │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Python + Pandas │
              │      ETL        │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │    SQL SERVER   │
              │  EcommerceDW    │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  BRONZE LAYER   │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  SILVER LAYER   │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │   GOLD LAYER    │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  FACT / DIM     │
              │     TABLES      │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │    ANALYTICS    │
              └─────────────────┘
