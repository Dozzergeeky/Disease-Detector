#4
import mysql.connector as sqlcon
def func_2():
    con = sqlcon.connect(host="localhost", user="root", password="1234", database="management")
    cursor = con.cursor()
    query = "s"
    try:
        cursor.execute()
        con.commit()
    except:
        con.rollback()
    cursor.close()
    con.close()
def func_1():
    con = sqlcon.connect(host="localhost", user="root", password="1234", database="management")
    cursor = con.cursor()
    query = "insert into management values(%s,%s,%s,%s,%s)"
    enter = (input("Enter ename:"), input("Enter deptname:"), input("Enter designation:"), input("Enter salary:"),
             input("Enter date of joining:"))
    try:
        cursor.execute(query, enter)
        con.commit()
    except:
        con.rollback()
    con.close()
def func_3():
    con = sqlcon.connect(host="localhost", user="root", password="1234", database="management")
    cursor = con.cursor()
    query = "select * from employee"
    try:
        cursor.execute(query)
    except:
        con.rollback()
    cursor.close()
    con.close()
def func_4():
    con = sqlcon.connect(host="localhost", user="root", password="1234", database="management")
    cursor = con.cursor()
    query = "update employee set %s = %s where %s = %s;"
    enter = (input("Enter what to set:"), input("Enter value 1:"), input("Enter where to set:"), input("Enter value 2:"))
    try:
        cursor.execute(query, enter)
        con.commit()
    except:
        con.rollback()
    cursor.close()
    con.close()
def func_5():
    con = sqlcon.connect(host="localhost", user="root", password="1234", database="management")
    cursor = con.cursor()
    query = "delete from employee where %s = %s"
    enter = (input("Enter what to set:"), input("Enter value 1:"))
    try:
        cursor.execute(query,enter)
        con.commit()
    except:
        con.rollback()
    cursor.close()
    con.close()


while True:
    print("Enter")
    print(" 1 : Add a record ")
    print(" 2 : Add multiple records")
    print(" 3 : display all records")
    print(" 4 : Update a record")
    print(" 5 : Delete a record")
    print(" 6 : Exit")
    choice = int(input("Enter the function number: "))
    if choice == 1:
        func_1()
    if choice == 2:
        func_2()
    if choice == 3:
        func_3()
    if choice == 4:
        func_4()
    if choice == 5:
        func_5()
    if choice == 6:
        break
