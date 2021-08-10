# importing the mysql connector module
import mysql.connector
# importing logging module
import logging

log_format = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="insert_rows.log",
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
    # giving multiple rows values in list of tuples
    vals = [("ganesh", "madanapalle"),
            ("ram", "tirupati"),
            ("ben", "bangalore"),
            ("amy", "mumbai"),
            ("sravan kumar", "hydrabad")
            ]
    # executing the query by using cursor object executemany method
    my_cursor.executemany(sql, vals)
    # commit the changes by using commit() method
    my_connection.commit()
    # printing the success message
    print("data inserted successfully....!")
    logging.info("all data inserted successfully....!")
    my_cursor.execute("select * from customer")
    # executing the query by using cursor object to get all data from the table
    data = my_cursor.fetchall()
    # displaying all  rows data by using for loop
    for row in data:
        print("customer id :", row[0])
        print("customer name :", row[1])
        print("customer city :", row[2])
        print()
        print()
except Exception as message:
    # printing exception
    print(message)
    logging.warning(message)
finally:
    # closing the connection
    my_connection.close()
    print(" connection closed....!")

