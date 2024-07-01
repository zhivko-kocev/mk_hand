# MK_HAND Project

### This project is designed to automatically import data from Excel files into a database using SQLAlchemy. The project is structured to maintain clean code organization, separating models, configuration, and scripts.

## Project Structure

### Description of Files and Directories

- **models/**: Contains all SQLAlchemy models. There are only two now but more to be added in the next days...
    - `__init__.py`: Dynamically imports all model files.
    - `base.py`: Contains the base class for all models.
    - `lawyer.py`: Example model for lawyer.
    - `legal_clinic.py`: Example model for legal_clinic.

- **data_xls/**: Directory where all Excel files to be imported are stored. Now it has dummy xls files for testing.

- **config.py**: Contains database configuration details.

- **script.py**: Main script to run the data import process.

- **README.md**: Project documentation file.

## Setting Up the Project

- **Setup Instructions**:
    - **Clone the Repository**: Clone your project repository locally.
    - **Create a Virtual Environment**: Set up a virtual environment to isolate dependencies.
    - **Install Dependencies**: Use `pip` to install required packages (`sqlalchemy` and `pandas` in this case) directly
      into the virtual environment.
    - **Configure the Database**: Edit `config.py` to specify your database connection URL.

- **Running the Script**:
    - **Add Excel Files**: Place Excel files with data to import into the `data_xls` directory.
    - **Execute the Script**: Run `python script.py` to start the data import process. It will read Excel files, import
      data into corresponding database tables, and move processed files to a target directory.

This `README.md` file provides a clear guide for setting up your project, installing dependencies, configuring the
database, and running the script for data import from Excel files into your SQLAlchemy-based database. Adjust paths,
model names, and other details to fit your specific project requirements.





