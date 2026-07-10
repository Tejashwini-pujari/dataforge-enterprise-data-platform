# 🚀 DataForge Enterprise Data Platform

## 📌 Project Overview

DataForge Enterprise Data Platform is an end-to-end Data Engineering project that demonstrates the complete ETL (Extract, Transform, Load) process using Python and PostgreSQL.

The project ingests data from multiple file formats, validates and cleans the data, loads it into a PostgreSQL database, and performs SQL-based analytics to generate business insights.

---

## 🎯 Objectives

* Extract data from multiple file formats.
* Validate data quality.
* Clean and transform raw data.
* Store processed data in PostgreSQL.
* Perform SQL analytics for reporting and insights.
* Build a modular and reusable ETL pipeline.

---

## 🛠️ Technologies Used

* Python 3
* PostgreSQL
* Pandas
* psycopg2
* JSON
* XML
* CSV
* Git & GitHub
* VS Code

---

## 📂 Project Structure

```text
dataforge-enterprise-data-platform/
│
├── data/
│   ├── raw/
│   │   ├── sales.csv
│   │   ├── customers.json
│   │   ├── employees.xml
│   │   └── website_logs.txt
│   │
│   └── processed/
│       ├── clean_sales.csv
│       ├── clean_customers.json
│       ├── clean_employees.xml
│       ├── clean_logs.csv
│       └── final_sales_report.csv
│
├── scripts/
│   ├── ingest_csv.py
│   ├── ingest_json.py
│   ├── ingest_xml.py
│   ├── ingest_logs.py
│   ├── validator.py
│   ├── validator_json.py
│   ├── validator_xml.py
│   ├── validator_logs.py
│   ├── cleaner.py
│   ├── cleaner_json.py
│   ├── cleaner_xml.py
│   ├── cleaner_logs.py
│   ├── merge_data.py
│   ├── database_connection.py
│   ├── load_to_postgres.py
│   └── logger_config.py
│
├── config.py
├── main.py
├── test_connection.py
├── requirements.txt
└── README.md
```

---

## 🔄 ETL Pipeline

### 1. Extract

The pipeline reads data from multiple formats:

* CSV (Sales)
* JSON (Customers)
* XML (Employees)
* TXT Log Files (Website Logs)

---

### 2. Validate

The validation layer checks:

* Missing values
* Duplicate records
* Invalid data
* Incorrect formats
* Data quality issues

---

### 3. Transform

The cleaning layer:

* Removes duplicates
* Handles missing values
* Converts data types
* Standardizes data
* Produces clean datasets

---

### 4. Load

Cleaned datasets are loaded into PostgreSQL tables using Python and `psycopg2`.

Database:

```
dataforge
```

Tables:

* sales
* customers
* employees
* website_logs

---

## 🗄️ Database Schema

### Sales

* sale_id
* customer_id
* product
* category
* quantity
* price
* sale_date
* city

### Customers

* customer_id
* customer_name
* email
* city

### Employees

* employee_id
* employee_name
* department
* salary

### Website Logs

* timestamp
* ip_address
* url
* status_code

---

## 📊 SQL Analytics

Example analyses performed:

* Total Sales
* Total Revenue
* Revenue by Product
* Sales by City
* Customer Analysis
* Customer Purchase Summary
* Employee Salary Analysis
* Website Log Analysis

---

## ▶️ How to Run

### Clone Repository

```bash
git clone https://github.com/Tejashwini-pujari/dataforge-enterprise-data-platform.git
cd dataforge-enterprise-data-platform
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

### Run ETL Scripts

```bash
python scripts/ingest_csv.py
python scripts/ingest_json.py
python scripts/ingest_xml.py
python scripts/ingest_logs.py
```

### Load Data into PostgreSQL

```bash
python scripts/load_to_postgres.py
```

---

## 📈 Project Workflow

```
Raw Data
     │
     ▼
Data Ingestion
     │
     ▼
Validation
     │
     ▼
Cleaning & Transformation
     │
     ▼
Processed Data
     │
     ▼
PostgreSQL Database
     │
     ▼
SQL Analytics
```

---

## 📚 Key Skills Demonstrated

* ETL Pipeline Development
* Data Validation
* Data Cleaning
* PostgreSQL Integration
* SQL Querying
* Python Programming
* Data Processing
* Git & GitHub
* Modular Project Design

---

## 🚀 Future Improvements

* Dockerize the application
* Add Apache Airflow for workflow orchestration
* Integrate Apache Spark/PySpark for large-scale processing
* Store credentials securely using environment variables
* Deploy on a cloud platform such as AWS or Azure
* Build interactive dashboards using Power BI or Tableau

---

## 👩‍💻 Author

**Tejashwini Pujari**

* GitHub: https://github.com/Tejashwini-pujari
* LinkedIn: [www.linkedin.com/in/tejashwini-pujari](http://www.linkedin.com/in/tejashwini-pujari)
