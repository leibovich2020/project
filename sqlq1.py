import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="workers"

)
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE workers")
# mycursor.execute("SHOW DATABASES")






# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE worker (employee_id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(255), last_name VARCHAR(255), email VARCHAR(255), phone_number VARCHAR(255), hire_date VARCHAR(255),job_id VARCHAR(255),salary INT(10),comission INT(10))")
# mycursor.execute("SHOW TABLES")
# for tb in mycursor:
#     print(tb)


# mycursor = mydb.cursor()
# sqlFormula = "INSERT INTO worker (first_name, last_name, email, phone_number, hire_date,job_id,salary, comission  ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
# workes = [  ("Slim", "Shady","slim@gmail.com","064646267734","29/09/2012",2 ,32442,0),
#             ("Bibi", "Netanyahu","bibi@gmail.com","55423532","28/07/2021", 2,4442,0),
#             ("Dmitriy", "Nagiev","dmitriy@gmail.com","35252462","24/12/2020",1,100000,0),
#             ("Dwayne", "Johnson","dwayne@gmail.com","976846246","06/06/2019",3,3342,0),
#             ("Albert", "Einstein","albert@gmail.com","087573226","14/09/2019",3,655553,0),
#             ("Angelina", "Jolie","angelina@gmail.com","22152623","24/03/2020",3,1142,0),
#             ("Leonardo", "Dicaprio","leonardo@gmail.com","624673754","22/02/2016",2,242,0),
#             ("Jim", "Carrey","jim@gmail.com","9876543","12/01/2018",2,1242,0),
#             ("Gal", "Gadot","gal@gmail.com","12345678","06/04/2020",3,11442,0),
#             ("Lionel", "Messi","lionel@gmail.com","1010101010","04/06/2019",3,235442,0)]
# mycursor.executemany(sqlFormula,workes)
# mydb.commit()

#
# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE id_job (id INT(10), name VARCHAR(255))")
# mycursor.execute("SHOW TABLES")
# for tb in mycursor:
#     print(tb)
# #
# mycursor = mydb.cursor()
# sqlFormula = "INSERT INTO id_job (id, name) VALUES (%s, %s)"
# job = [     (1, "Owner"),
#             (2, "manager"),
#             (3, "worker")
# ]
# mycursor.executemany(sqlFormula,job)
# mydb.commit()
#
# mycursor = mydb.cursor()
# sql = "SELECT worker.first_name AS user, id_job.name AS job_id FROM worker INNER JOIN id_job ON worker.job_id = id_job.id"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for user in myresult:
#     print(user)
# mydb.commit()