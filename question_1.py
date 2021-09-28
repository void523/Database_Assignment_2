import sqlite3


def get_connection():
    try:

        con = sqlite3.connect('employee.db')

        print("Connection is established: Database is created in memory")

        return con

    except:

        print('Error')


con = get_connection()
cur = con.cursor()


def find_employee(cur):
    x = input("Enter the letter to search with : ").upper()
    a = x + '%'
    name_query = "SELECT * FROM Employee WHERE Name LIKE ?"
    cur.execute(name_query, (a,))
    result = cur.fetchall()

    for row in result:
        print("ID = ", row[0])
        print("Name = ", row[1])
        print("Salary = ", row[2])
        print("Department_Id = ", row[3])
        print("City = ", row[4], '\n')


def get_employee_details(id):
    try:
        id_query = """SELECT * FROM employee WHERE ID = ? """
        cur.execute(id_query, (id,))
        records = cur.fetchall()
        print("Details of employee based on ID:", id, '\n')
        for row_ in records:
            print("ID = ", row_[0])
            print("Name = ", row_[1])
            print("Salary = ", row_[2])
            print("Department_Id = ", row_[3])
            print("City = ", row_[4], '\n')
    except (Exception, sqlite3.Error) as error:
        print("Error while retrieving data", error)


def change_name(id_):
    try:
        # geting the current name
        name_query = """SELECT Name FROM employee WHERE ID = ?"""
        cur.execute(name_query, (id_,))
        ch_name = cur.fetchone()

        # geting the new name
        new_name = input("Enter the new name which is to be updated: ")

        # updating the new name
        new_name_query = """UPDATE employee SET Name = ? where ID = ?"""
        cur.execute(new_name_query, (new_name, id_,))
        con.commit()
        print("ID:", id_, "Name is updated to:", new_name)
        print('\n')
        print("Updated Details of ID, Name and Salary of employees from table are; \n")
        cur.execute("SELECT ID,Name,Salary FROM employee")
        formatted_result = [f"\t{ID:<8}{Name:<12}{Salary:<35}" for ID, Name, Salary in cur.fetchall()]
        ID, Name, Salary = "ID", "NAME", "Salary"
        print('\n'.join([f"\t{ID:<8}{Name:<12}{Salary:<35}"] + formatted_result))
    except (Exception, sqlite3.Error) as error:
        print("Error while getting doctor's data", error)


########################################################################################################################
'''
Creating table employee
'''
# employee_sql = """
# CREATE TABLE employee(
#     ID INTEGER NOT NULL PRIMARY KEY,
#     Name TEXT NOT NULL,
#     Salary INTEGER NOT NULL,
#     Department_Id INTEGER NOT NULL);"""
# cur.execute(employee_sql)
# con.commit()

"""
Adding new column
"""

# column_sql = """
# ALTER TABLE employee ADD COLUMN City TEXT """
# cur.execute(column_sql)
# con.commit()

'''
Inserting records into table
'''

employee_sql = """
INSERT OR REPLACE  INTO employee (ID,Name,Salary,Department_Id,City) VALUES (?,?,?,?,?)"""
employee_list = [
    ('101', 'David', '40000', '521', 'Kochi'),
    ('102', 'Michael', '20000', '522', 'Kannur'),
    ('103', 'Joseph', '25000', '523', 'Kottayam'),
    ('104', 'Robert', '28000', '524', 'Trivandrum'),
    ('105', 'Linda', '42000', '525', 'Kozhikode')
]
cur.executemany(employee_sql, employee_list)
con.commit()

'''
Reading ID, NAME and Salary from employee table
'''

print("Details of ID, Name and Salary of employees from table are; \n")
# res = con.execute("SELECT ID, Name, Salary FROM  employee")
# for row in res:
#     print("ID = ", row[0])
#     print("Name = ", row[1])
#     print("Salary = ", row[2], '\n')

########################OR###################################################

cur.execute("SELECT ID,Name,Salary FROM employee")
formatted_result = [f"\t{ID:<8}{Name:<12}{Salary:<35}" for ID, Name, Salary in cur.fetchall()]
ID,Name,Salary = "ID","NAME" , "Salary"
print('\n'.join([f"\t{ID:<8}{Name:<12}{Salary:<35}"] + formatted_result))

print('\n')
if __name__ == '__main__':

    '''
    Reading Details of Employee Based on first letter of name
    '''

    find_employee(cur)

    """
    Details of employee based on ID 
    """

    try:
        id = input("Enter the ID of employee whose details are required: ")
        if id.isdigit():
            get_employee_details(id)
        else:
            print("Enter Valid ID")

    except:
        print("Error, enter a valid ID")

    '''
    Changing Name of Employee
    '''

    try:
        id_ = input("Enter the ID of employee whose name is to be changed: ")
        if id_.isdigit():
            change_name(id_)
        else:
            print("Enter Valid ID")

    except:
        print("Error, enter a valid ID")

    con.close()
