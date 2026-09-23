# 🛒 Olist E-Commerce Data Engineering Pipeline

> **End-to-End Data Engineering Project**  
> Building an automated ETL pipeline for Brazilian E-Commerce data using **Python, SQL Server, Docker, Apache Airflow, PostgreSQL and Redis**.

---

## 📌 Table of Contents

- [1. Project Overview](#1-project-overview)
- [2. Project Objectives](#2-project-objectives)
- [3. Business Context](#3-business-context)
- [4. Dataset](#4-dataset)
- [5. Technologies](#5-technologies)
- [6. Architecture](#6-architecture)
- [7. Project Structure](#7-project-structure)
- [8. Data Sources](#8-data-sources)
- [9. ETL Pipeline](#9-etl-pipeline)
- [10. Extract](#10-extract)
- [11. Transform](#11-transform)
- [12. Load](#12-load)
- [13. Data Warehouse](#13-data-warehouse)
- [14. Airflow Orchestration](#14-airflow-orchestration)
- [15. Docker Environment](#15-docker-environment)
- [16. SQL Server](#16-sql-server)
- [17. PostgreSQL](#17-postgresql)
- [18. Redis](#18-redis)
- [19. Data Quality](#19-data-quality)
- [20. Error Handling](#20-error-handling)
- [21. Logging](#21-logging)
- [22. Running the Project](#22-running-the-project)
- [23. Python Environment](#23-python-environment)
- [24. SQL Server Connection](#24-sql-server-connection)
- [25. Airflow Web Interface](#25-airflow-web-interface)
- [26. Pipeline Workflow](#26-pipeline-workflow)
- [27. Data Flow](#27-data-flow)
- [28. Example ETL Process](#28-example-etl-process)
- [29. Data Warehouse Design](#29-data-warehouse-design)
- [30. Fact Tables](#30-fact-tables)
- [31. Dimension Tables](#31-dimension-tables)
- [32. Analytical Queries](#32-analytical-queries)
- [33. Project Challenges](#33-project-challenges)
- [34. Problems Solved](#34-problems-solved)
- [35. Technical Skills Demonstrated](#35-technical-skills-demonstrated)
- [36. Future Improvements](#36-future-improvements)
- [37. Project Roadmap](#37-project-roadmap)
- [38. Conclusion](#38-conclusion)
- [39. Author](#39-author)

---

# 1. Project Overview

This project is an **End-to-End Data Engineering pipeline** built around the Brazilian E-Commerce dataset from Olist.

The main goal is to design and implement a complete data pipeline that can:

1. Extract raw e-commerce data from CSV files.
2. Validate and clean the raw data.
3. Transform data using Python and Pandas.
4. Load processed data into a relational database.
5. Build a Data Warehouse structure.
6. Orchestrate ETL workflows using Apache Airflow.
7. Run the entire infrastructure using Docker.
8. Connect different services together inside a Docker network.
9. Prepare the data for analytical queries and Business Intelligence.

The project simulates a real-world Data Engineering environment where raw data is transformed into structured and analytical data.

---

# 2. Project Objectives

The project was developed to practice and demonstrate practical Data Engineering skills.

### Main objectives

- Understand the complete ETL process.
- Work with real-world e-commerce datasets.
- Build reusable Python ETL scripts.
- Work with Pandas for data transformation.
- Connect Python applications to SQL Server.
- Design relational tables.
- Build a Data Warehouse.
- Automate pipelines with Apache Airflow.
- Containerize services using Docker.
- Understand Docker networking.
- Separate raw data from processed data.
- Implement data validation.
- Handle ETL errors.
- Create reproducible development environments.
- Prepare data for downstream analytics.

---

# 3. Business Context

E-commerce platforms generate large amounts of data from different business processes.

For example:

- Customers
- Orders
- Products
- Sellers
- Payments
- Reviews
- Order items
- Geographical information

These datasets are usually stored separately.

For data analysts and business teams, querying raw CSV files directly is inconvenient and inefficient.

Therefore, a Data Engineering pipeline is required to:

```text
Raw Data
    ↓
Data Extraction
    ↓
Data Cleaning
    ↓
Data Transformation
    ↓
Data Validation
    ↓
Data Warehouse
    ↓
Analytics
