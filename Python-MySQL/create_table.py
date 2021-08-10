# importing the mysql connector module
import mysql.connector
# importing logging module
import logging

log_format = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="table_create.log",
                    level=logging.INFO,
                    format=log_format,
                    datefmt="%d/%m/%y %I:%M:%S:%p")
logging.info("New  table create request came !")

# establishing the connection between python programme and mysql database
my_connection = mysql.connector.connect(host="localhost",
                                        user="root",
                                        passwd="root",
                                        database="mydatabase")
# creating cursor object to execute queries
my_cursor = my_connection.cursor()

try:
    # executing the query by using cursor object
    my_cursor.execute("CREATE TABLE customer "
                      "(id INT AUTO_INCREMENT PRIMARY KEY , name VARCHAR(20), city VARCHAR(20))")
    print("Table was created successfully.....!")

# if table already exists we get exception
except Exception as message:
    print(message)
    logging.warning(message)

finally:
    # displaying tables list in the database
    my_cursor.execute("SHOW TABLES")
    print("Tables list :")
    for table in my_cursor:
        print(table)

    # closing the connection
    my_connection.close()
    print(" connection closed....!")
