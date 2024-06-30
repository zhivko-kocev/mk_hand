import pandas as pd
import os
from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Kje se dodatat i drugite tabeli i kje se strukturira proektot soodvetno vo narednite denovi

Base = declarative_base()
DATABASE_URL = 'sqlite:///mk_hand.db'  # replace with your database URL


class Table1(Base):
    __tablename__ = 'table1'
    id = Column(Integer, primary_key=True)
    column1 = Column(String)
    column2 = Column(String)


class Table2(Base):
    __tablename__ = 'table2'
    id = Column(Integer, primary_key=True)
    column1 = Column(String)
    column2 = Column(String)


# ...


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
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    excel_directory = './data_xls'
    for excel_file in os.listdir(excel_directory):
        if excel_file.endswith('.xlsx') or excel_file.endswith('.xls'):
            file_path = os.path.join(excel_directory, excel_file)
            insert_data_from_excel(file_path, session)


if __name__ == '__main__':
    main()
