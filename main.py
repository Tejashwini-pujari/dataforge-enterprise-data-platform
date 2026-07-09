from config import *

# CSV
from scripts.ingest_csv import read_sales_data, data_quality_report
from scripts.validator import validate_data
from scripts.cleaner import clean_data, save_clean_data

# JSON
from scripts.ingest_json import read_customer_data, customer_quality_report
from scripts.validator_json import validate_customer_data
from scripts.cleaner_json import (
    clean_customer_data,
    save_clean_customers,
)

# XML
from scripts.ingest_xml import read_employee_data, employee_quality_report
from scripts.validator_xml import validate_employee_data
from scripts.cleaner_xml import (
    clean_employee_data,
    save_clean_employees,
)

# LOGS
from scripts.ingest_logs import read_log_data, log_quality_report
from scripts.validator_logs import validate_log_data
from scripts.cleaner_logs import (
    clean_log_data,
    save_clean_logs,
)


def main():

    print("=" * 60)
    print("DATAFORGE ENTERPRISE DATA PLATFORM")
    print("=" * 60)

    # =============================
    # CSV PIPELINE
    # =============================

    print("\nRunning CSV Pipeline...")

    sales_df = read_sales_data(SALES_FILE)

    if sales_df is not None:

        data_quality_report(sales_df)

        validate_data(sales_df)

        clean_sales = clean_data(sales_df)

        save_clean_data(clean_sales, CLEAN_SALES)

    # =============================
    # JSON PIPELINE
    # =============================

    print("\nRunning JSON Pipeline...")

    customer_df = read_customer_data(CUSTOMERS_FILE)

    if customer_df is not None:

        customer_quality_report(customer_df)

        validate_customer_data(customer_df)

        clean_customer = clean_customer_data(customer_df)

        save_clean_customers(
            clean_customer,
            CLEAN_CUSTOMERS,
        )

    # =============================
    # XML PIPELINE
    # =============================

    print("\nRunning XML Pipeline...")

    employee_df = read_employee_data(EMPLOYEES_FILE)

    if employee_df is not None:

        employee_quality_report(employee_df)

        validate_employee_data(employee_df)

        clean_employee = clean_employee_data(employee_df)

        save_clean_employees(
            clean_employee,
            CLEAN_EMPLOYEES,
        )

    # =============================
    # LOG PIPELINE
    # =============================

    print("\nRunning LOG Pipeline...")

    logs_df = read_log_data(LOG_FILE)

    if logs_df is not None:

        log_quality_report(logs_df)

        validate_log_data(logs_df)

        clean_logs = clean_log_data(logs_df)

        save_clean_logs(
            clean_logs,
            CLEAN_LOGS,
        )

    print("\n" + "=" * 60)
    print("ALL PIPELINES COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()