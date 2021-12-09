from flask import Flask, render_template, request, redirect
from db import mydb, mycursor


app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')



@app.route('/gotoadmin')
def admin():
    mycursor.execute("SELECT * FROM Profiles")
    students = mycursor.fetchall()
    return render_template('Lecturer.html', students = students)




@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    if request.method == 'GET':
        mycursor.execute(f'SELECT * FROM Profiles WHERE  ID={id}')
        students = mycursor.fetchone()
        return render_template('edit.html', student = students)
    if request.method == 'POST':
        fullname = request.form['fullname']
        dateofbirth = request.form['dateofbirth']
        email = request.form['email']
        phonenumber = request.form['phonenumber']
        department = request.form['department']
        level = request.form['level']
        intake = request.form['intake']
        fieldofstudy = request.form['fieldofstudy']
        studentid = request.form['studentid']
        
        sql = f'UPDATE Profiles SET Students_Full_Name = %s,  Date_of_Birth = %s,  Email_Address =%s,  Phone_Number =%s,  Department =%s,  Level =%s,  Intake =%s, Field_of_Study =%s ,   Student_id =%s WHERE  ID = %s'
        values = (fullname, dateofbirth,email, phonenumber, department, level, intake, fieldofstudy, studentid, id)
        mycursor.execute(sql, values)
        mydb.commit()
        mycursor.execute("SELECT * FROM Profiles")
        students = mycursor.fetchall()
        return render_template('Lecturer.html', students = students)







@app.route('/delete/<int:id>')
def delete_student(id):
    sql = f'DELETE FROM Profiles WHERE ID={id}'
    mycursor.execute(sql)
    mydb.commit()
    mycursor.execute("SELECT * FROM Profiles")
    student = mycursor.fetchall()
    return render_template('Lecturer.html', students = student)

               




         

@app.route('/forms', methods=['GET', 'POST'])
def forms():
    if request.method == 'POST':
        fullname = request.form['fullname']
        dateofbirth = request.form['dateofbirth']
        email = request.form['email']
        phonenumber = request.form['phonenumber']
        department = request.form['department']
        level = request.form['level']
        intake = request.form['intake']
        fieldofstudy = request.form['fieldofstudy']
        studentid = request.form['studentid']
        sql = 'INSERT INTO Profiles(Students_Full_Name, Date_of_Birth,Email_Address,Phone_Number,  Department, Level, Intake, Field_of_Study, Student_id) VALUE (%s, %s, %s ,%s, %s, %s, %s, %s, %s)'
        val = (fullname, dateofbirth,email, phonenumber, department, level, intake, fieldofstudy, studentid)
        mycursor.execute(sql, val)
        mydb.commit()
        return render_template('index.html')



if __name__ == '__main__':
    app.run()