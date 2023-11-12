## Answers

1. 
today = datetime.now()

sql ="INSERT INTO employee (emp_num, emp_lname, emp_fname, emp_initial, job_code, emp_hiredate) VALUES (%s, %s, %s, %s, %s, %s)"
value = (168, "Doe", "John", "JD", 500, today)

cursor.execute(sql, value)
DB.commit()

2. 
sql = "SELECT employee.emp_num, employee.emp_lname, employee.emp_fname, employee.emp_initial, job.job_description, job.job_chg_hour, emp_hiredate FROM employee JOIN job ON employee.job_code = job.job_code WHERE emp_num = 168"

cursor.execute(sql)
result = cursor.fetchall()
DB.commit()

3. 
sql = "UPDATE employee SET job_code = 502 where emp_num = 168"
cursor.execute(sql)
DB.commit()

4. 
sql = "SELECT project.proj_num, project.proj_name, employee.emp_fname, employee.emp_lname, FROM project JOIN employee on project.emp_num = employee.emp_num WHERE employee.job_code = 500"

cursor.execute(sql)
result = cursor.fetchall()
DB.commit()

5. 
sql = "DELETE FROM employee WHERE emp_num = 168"

cursor.execute(sql)
DB.commit()