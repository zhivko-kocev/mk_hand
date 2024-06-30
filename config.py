from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'sqlite:///test.db'  # replace with your database URL

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
