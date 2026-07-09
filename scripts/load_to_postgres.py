import pandas as pd
import json
import xml.etree.ElementTree as ET

from database_connection import get_connection
from logger_config import logger


# ---------------- SALES ----------------

def load_sales_data():

    try:
        df = pd.read_csv("data/processed/clean_sales.csv")

        connection = get_connection()
        cursor = connection.cursor()

        for _, row in df.iterrows():

            cursor.execute(
                """
                INSERT INTO sales
                (
                    sale_id,
                    customer_id,
                    product,
                    category,
                    quantity,
                    price,
                    sale_date,
                    city
                )
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
                """,
                (
                    int(row["sale_id"]),
                    row["customer_id"],
                    row["product"],
                    row["category"],
                    int(row["quantity"]),
                    float(row["price"]),
                    row["sale_date"] if pd.notna(row["sale_date"]) else None,
                    row["city"]
                )
            )

        connection.commit()
        cursor.close()
        connection.close()

        print("Sales data loaded successfully")

    except Exception as e:
        print(e)
        logger.error(e)



# ---------------- CUSTOMERS ----------------

def load_customer_data():

    try:
        with open("data/processed/clean_customers.json") as file:
            customers = json.load(file)

        connection = get_connection()
        cursor = connection.cursor()

        for customer in customers:

            cursor.execute(
                """
                INSERT INTO customers
                (
                    customer_id,
                    customer_name,
                    email,
                    city
                )
                VALUES (%s,%s,%s,%s)
                """,
                (
                    customer["customer_id"],
                    customer["customer_name"],
                    customer["email"],
                    customer["city"]
                )
            )

        connection.commit()
        cursor.close()
        connection.close()

        print("Customer data loaded successfully")

    except Exception as e:
        print(e)
        logger.error(e)



# ---------------- EMPLOYEES ----------------

def load_employee_data():

    try:
        tree = ET.parse(
            "data/processed/clean_employees.xml"
        )

        root = tree.getroot()

        connection = get_connection()
        cursor = connection.cursor()

        for employee in root:

            cursor.execute(
                """
                INSERT INTO employees
                (
                    employee_id,
                    employee_name,
                    department,
                    salary
                )
                VALUES (%s,%s,%s,%s)
                """,
                (
                    employee.find("employee_id").text,
                    employee.find("employee_name").text,
                    employee.find("department").text,
                    float(employee.find("salary").text)
                    
                )
            )

        connection.commit()
        cursor.close()
        connection.close()

        print("Employee data loaded successfully")

    except Exception as e:
        print(e)
        logger.error(e)



# ---------------- LOGS ----------------

def load_logs_data():

    try:
        df = pd.read_csv(
            "data/processed/clean_logs.csv"
        )

        connection = get_connection()
        cursor = connection.cursor()

        for _, row in df.iterrows():

            cursor.execute(
                """
                INSERT INTO website_logs
                (
                    timestamp,
                    ip_address,
                    url,
                    status_code
                )
                VALUES (%s,%s,%s,%s)
                """,
                (
                    row["timestamp"],
                    row["ip_address"],
                    row["url"],
                    int(row["status_code"])
                )
            )

        connection.commit()
        cursor.close()
        connection.close()

        print("Logs data loaded successfully")

    except Exception as e:
        print(e)
        logger.error(e)



# ---------------- MAIN ----------------

if __name__ == "__main__":

    load_sales_data()

    load_customer_data()

    load_employee_data()

    load_logs_data()