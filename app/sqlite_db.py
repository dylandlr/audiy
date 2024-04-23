import sqlite3
from audit_data import audit_features

connection = sqlite3.connect("audit_list.db")
cursor = connection.cursor()

# Create the audit_features table for sqlite database
cursor.execute("create table audit_list (id integer, title text, description text, importance text, compliance integer)")
  
# cursor.executemany("insert into audit_list (id, title, description, importance, compliance) values (?, ?, ?, ?, ?)", audit_features)  

cursor.executemany("insert into audit_list values (?, ?, ?, ?, ?)", audit_features)
  
for row in cursor.execute("select * from audit_list"):
    print(row)
    
    
connection.commit()
connection.close()