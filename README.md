# MySQL to JSON Conversion Tool

This tool allows you to convert the results of a given MySQL query into a JSON file.

## Installation

1. Clone or download the project.
2. Before running the project, install the necessary modules by executing the command below:

```
pip install mysql-connector-python
```

## Configuration

Before using the tool, you need to update the database configuration details in the script. Open `index.py` and locate the following section:

```python
config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'example',
}
```

Replace `'root'`, `''`, `'127.0.0.1'`, and `'example'` with your MySQL database user, password, host, and database name respectively.

## Usage

1. Run the `index.py` file:

```
python index.py
```

2. The application will prompt you to enter an SQL query. Enter your query and press the Enter key.
3. Next, input the name for the JSON file where the results will be saved.
4. The results will be saved in the `temp` folder with the name you provided in JSON format.

## Features

- Saves SQL query results in JSON format.
- Automatically converts special data types like date and time.
- Saves the results in a readable format (indented).