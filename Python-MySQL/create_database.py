# importing the mysql connector module
import mysql.connector
# importing logging module
import logging

log_format = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="create_database.log",
                    level=logging.INFO,
                    format=log_format,
                    datefmt="%d/%m/%y %I:%M:%S:%p")
logging.info("New  Database create request came !")

# establishing the connection between python programme and mysql database
my_connection = mysql.connector.connect(host="localhost", user="root", passwd="root")
# creating cursor object to execute queries
my_cursor = my_connection.cursor()
# taking database input from the user
database = input(" enter database name to create database :").strip()

try:
    # executing the query by using cursor object
    my_cursor.execute("CREATE DATABASE " + database.lower())
    print(database, "Database was created successfully.....!")

# if database already exists we get exception
except Exception as message:
    print(message)
    logging.warning(message)

finally:
    # displaying databases list
    my_cursor.execute("SHOW DATABASES")
    print("Databases list :")
    for databases in my_cursor:
        print(databases)
    # closing the connection
    my_connection.close()
    print(" connection closed....!")
