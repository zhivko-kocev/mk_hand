import os
import pandas as pd
from models import Base
from config import engine, Session


def list_files(current_directory):
    files = os.listdir(current_directory)
    return [file for file in files if os.path.isfile(os.path.join(current_directory, file))]


def insert_data_from_excel(file_path, session):
    excel_file = pd.ExcelFile(file_path)

    for sheet_name in excel_file.sheet_names:
        model_class = Base.metadata.tables[sheet_name]
        if not model_class:
            print(f"No model found for table {sheet_name}")
            continue

        data_frame = pd.read_excel(excel_file, sheet_name=sheet_name)
        for index, row in data_frame.iterrows():
            row_data = row.to_dict()
            instance = model_class(**row_data)
            session.add(instance)

    session.commit()


def main():
    current_directory = './data_xls'  # Current directory

    files = list_files(current_directory)
    print("Files in the current directory:", files)

    session = Session()

    for file in files:
        if file.endswith('.xlsx') or file.endswith('.xls'):
            file_path = os.path.join(current_directory, file)
            insert_data_from_excel(file_path, session)


if __name__ == '__main__':
    Base.metadata.create_all(engine)  # Create tables
    main()
