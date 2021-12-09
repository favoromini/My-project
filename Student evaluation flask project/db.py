import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    database = 'Student_Eva',
    user = 'root',
    password = ''
)



mycursor = mydb.cursor(dictionary = True)




mycursor.execute(
    """CREATE TABLE IF NOT EXISTS Profiles(
        ID INT NOT NULL AUTO_INCREMENT,
        Students_Full_Name VARCHAR(255),
        Date_of_Birth VARCHAR(255),
        Email_Address VARCHAR(255),
        Phone_Number VARCHAR(255),
        Department VARCHAR(255),
        Level VARCHAR(255),
        Intake VARCHAR(255),
        Field_of_Study VARCHAR(255),
        Student_id  VARCHAR(255),
        PRIMARY KEY(ID)
    )
    """
)
