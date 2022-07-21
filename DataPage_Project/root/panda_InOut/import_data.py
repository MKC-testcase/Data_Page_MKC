import os

from pandas import read_csv, read_excel, read_sql_table, read_sql, read_sql_query
from os import getcwd

# By: Marcus Chan
# functions as hub to collect data from various data sources and places the results into a
# pandas dataframe

# read from csv file
def r_csv(filename):
    # filename = csv filename with file path
    home_folder = getcwd()
    if filename[-4:] == ".csv":
        try:
            panda_frame = read_csv(filename)
        except(FileNotFoundError):
            print("File not found, attempting to locate in project directory")
            # second attempt to connect
            try:
                panda_frame = read_csv(home_folder + "/" +filename)
            except(FileNotFoundError):
                print("File not found")
                return 0
    else:
        return 0
    return panda_frame

# read from excel file
def r_excel(filename):
    # filename = csv filename with file path
    home_folder = getcwd()
    if filename[-5:] == ".xlsx":
        try:
            panda_frame = read_excel(filename)
        except(FileNotFoundError):
            print("File not found, attempting to locate in project directory")
            # second attempt to connect
            try:
                panda_frame = read_excel(home_folder + "/" +filename)
            except(FileNotFoundError):
                print("File not found")
                return 0
    else:
        return 0
    return panda_frame

# read from sql table (entire table)
def r_sql_table(tablename, conn):
    # tablename = sql table name , connector = SQLAlchemy sql connector
    try:
        panda_frame = read_sql_table(tablename, conn)
    except(ConnectionError):
        print("There was an issue with the connector for the SQL database")
        return 0
    return panda_frame

# read from sql results
def r_sql(select_statement, conn):
    # tablename = sql table name , connector = SQLAlchemy sql connector
    try:
        panda_frame = read_sql(select_statement, conn)
    except(ConnectionError, SyntaxError):
        print("There was an issue with the connector for the SQL database")
        return 0
    return panda_frame

# read from SQL query
def r_sql_query(select_statement, conn):
    # tablename = sql table name , connector = SQLAlchemy sql connector
    try:
        panda_frame = read_sql_query(select_statement, conn)
    except(ConnectionError, SyntaxError):
        print("There was an issue with the connector for the SQL database")
        return 0
    return panda_frame

