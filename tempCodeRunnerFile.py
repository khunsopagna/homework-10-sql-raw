sql = "DELETE FROM employee WHERE emp_id = 168"
cursor.execute(sql)
DB.commit()
print(cursor.rowcount, "record updated.")