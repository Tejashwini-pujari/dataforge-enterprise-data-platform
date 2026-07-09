import pandas as pd
from logger_config import logger



def validate_employee_data(df):
    """
    Validate employee data and print row-level issues.
    """

    print("\n" + "=" * 50)
    print("EMPLOYEE DATA VALIDATION REPORT")
    print("=" * 50)

    logger.info("Starting Employee Data Validation")

    # -------------------------------
    # Check Duplicate Employee IDs
    # -------------------------------
    duplicate_ids = df[df.duplicated(subset=["employee_id"], keep=False)]

    if not duplicate_ids.empty:
        print("\nDuplicate Employee IDs Found:")
        print(duplicate_ids["employee_id"].tolist())
        logger.warning(
            f"Duplicate Employee IDs Found: {duplicate_ids['employee_id'].tolist()}"
        )

    # -------------------------------
    # Row-by-row Validation
    # -------------------------------
    for _, row in df.iterrows():

        employee_id = row["employee_id"]

        # Missing Employee Name
        if pd.isna(row["employee_name"]) or str(row["employee_name"]).strip() == "":
            print(f"Employee {employee_id} -> Missing Employee Name")
            logger.warning(f"Employee {employee_id}: Missing Employee Name")

        # Missing Department
        if pd.isna(row["department"]) or str(row["department"]).strip() == "":
            print(f"Employee {employee_id} -> Missing Department")
            logger.warning(f"Employee {employee_id}: Missing Department")

        # Missing Salary
        if pd.isna(row["salary"]):
            print(f"Employee {employee_id} -> Missing Salary")
            logger.warning(f"Employee {employee_id}: Missing Salary")

        # Invalid Salary
        elif row["salary"] <= 0:
            print(f"Employee {employee_id} -> Invalid Salary")
            logger.warning(f"Employee {employee_id}: Invalid Salary")

        # Missing City
        if pd.isna(row["city"]) or str(row["city"]).strip() == "":
            print(f"Employee {employee_id} -> Missing City")
            logger.warning(f"Employee {employee_id}: Missing City")

    logger.info("Employee Data Validation Completed")