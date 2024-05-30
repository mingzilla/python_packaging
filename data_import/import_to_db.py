# Import to DB
import argparse
import os
import re

import pandas as pd  # type: ignore
from sqlalchemy import create_engine


def format_name(name):
    return re.sub(r"\s+", "_", name.strip().lower())


def read_all_excel_sheets(file_path):
    xls = pd.ExcelFile(file_path)
    sheets_dict = {}
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        df.columns = map(format_name, df.columns)  # Lowercase the column names
        formatted_sheet_name = format_name(sheet_name)
        sheets_dict[formatted_sheet_name] = df
    return sheets_dict


def create_db_connection(user, password, host, port, database):
    """Create a SQLAlchemy engine for the database connection."""
    connection_string = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(connection_string)
    return engine


def write_to_db(df, table_name, engine):
    """Write a DataFrame to a specified table in the database."""
    table_name = table_name.lower()  # Ensure the table name is lowercase
    df.to_sql(table_name, con=engine, if_exists="replace", index=False)


def main(file_path):
    print(f"Current Path: {os.getcwd()}")  # Print the current working directory

    # Database connection details
    user = "sales"
    password = "salesP1"
    host = "localhost"
    port = "3316"
    database = "storage"

    sheets_dict = read_all_excel_sheets(file_path)

    engine = create_db_connection(user, password, host, port, database)

    for table_name, df in sheets_dict.items():
        write_to_db(df, table_name, engine)

    print("Data successfully written to the database.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Read Excel file and import to MariaDB."
    )
    parser.add_argument("file_path", type=str, help="The path to the Excel file.")
    args = parser.parse_args()

    main(args.file_path)
