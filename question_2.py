import sqlite3


def get_connection():
    try:

        con = sqlite3.connect('department.db')

        print("Connection is established: Database is created in memory")

        return con

    except:

        print('Error')


con = get_connection()
cur = con.cursor()

def dept_name_info(dept_id):
    try:
        name_query = "SELECT * FROM department WHERE Department_Id = ?"
        cur.execute(name_query,(dept_id,))
        result = cur.fetchone()
        return result[1]
    except:
        print("Error while retrieving data")

def get_details_dept(dept_id):
    try:
        dept_name = dept_name_info(dept_id)
        dept_query = '''SELECT * FROM employee  WHERE Department_Id = ?'''
        cur.execute(dept_query,(dept_id,))
        records_ = cur.fetchall()
        print("Employee Details of" , dept_name , "with Departemnt ID" , dept_id)
        print("\n")
        for row_s in records_:
            print("ID = ", row_s[0])
            print("Name = ", row_s[1])
            print("Salary = ", row_s[2])
            print("City = ", row_s[4], '\n')
    except (Exception, sqlite3.Error) as error:
        print("Error while retrieving data", error)
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
Creating a Department Table
'''

# department_sql = """
# CREATE TABLE department(
#     Department_Id INTEGER NOT NULL PRIMARY KEY,
#     Department_Name TEXT NOT NULL
#       );"""
# cur.execute(department_sql)
# con.commit()

'''
Inserting Values into Department table
'''

department_sql = '''
INSERT OR REPLACE INTO department (Department_Id,Department_Name) VALUES (?,?)
'''
department_list = [
    (521,'General Management'),
    (522,'Finance Department'),
    (523,'Human Resource'),
    (524,'Quality Assurance'),
    (525,'Research and Development')
]
cur.executemany(department_sql,department_list)
con.commit()

# res1 = cur.execute("SELECT * FROM employee")
# print(res1.fetchall())
# print('\n')
# res2 = cur.execute("SELECT * FROM department")
# print(res2.fetchall())

print("Details of Department Id, Department Name from Department  table are; \n")
# res = con.execute("SELECT Department_Id, Department_Name FROM department")
# for row in res:
#     print("Department Id = ", row[0])
#     print("Department Name = ", row[1],'\n')


cur.execute("SELECT Department_Id,Department_Name FROM department")
formatted_result = [f"\t{Department_Id:<18}{Department_Name:<20}" for Department_Id, Department_Name in cur.fetchall()]
Department_Id,Department_Name = "Dept Id","Department Name"
print('\n'.join([f"\t{Department_Id:<18}{Department_Name:<20}"] + formatted_result))
print('\n')
try:
    dep_id = input("Please enter the Department ID to get Employee Details of that Department: ")
    print('\n')
    if dep_id.isdigit():
        get_details_dept(dep_id)
    else:
        print("Please enter a valid Department ID")

except:
    print("Error, try Again")

con.close()

