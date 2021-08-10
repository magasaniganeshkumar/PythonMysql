# importing the mysql connector module
import mysql.connector
# importing logging module
import logging

log_format = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="insert_row.log",
                    level=logging.INFO,
                    format=log_format,
                    datefmt="%d/%m/%y %I:%M:%S:%p")
logging.info("New insert request came !")

try:
    # establishing the connection between python programme and mysql database
    my_connection = mysql.connector.connect(host="localhost",
                                            user="root",
                                            passwd="root",
                                            database="mydatabase")
    # creating cursor object to execute queries
    my_cursor = my_connection.cursor()
    # writing sql query
    sql = "INSERT INTO customer (name, city) VALUES (%s, %s)"
    # giving the values
    val = ("ganesh", "madanapalle")
    # executing the query by using cursor object
    my_cursor.execute(sql, val)
    # commit the changes by using commit() method
    my_connection.commit()
    # printing the success message
    print("data inserted successfully....!")
    logging.info("data inserted successfully....!")
    # executing the query by using cursor object to get all data from the table
    my_cursor.execute("select * from customer")
    # displaying only one row data
    data = my_cursor.fetchone()
    print("customer id :", data[0])
    print("customer name :", data[1])
    print("customer city :", data[2])

except Exception as message:
    # printing exception
    print(message)
    logging.warning(message)

finally:
    # closing the connection
    my_connection.close()
    print(" connection closed....!")

