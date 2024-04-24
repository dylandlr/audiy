import sqlite3
from audit_data import audit_features


connection = sqlite3.connect("audit_list.db")
cursor = connection.cursor()

# Create the audit_features table for sqlite database
cursor.execute("create table if not exists audit_list (id integer, title text, description text, importance text, compliance integer)")
  
# cursor.executemany("insert into audit_list (id, title, description, importance, compliance) values (?, ?, ?, ?, ?)", audit_features)  

cursor.executemany("""
    insert into audit_list (id, title, description, importance, compliance) 
    values (:id, :title, :description, :importance, :compliance)
""", audit_features)
  
# for row in cursor.execute("select * from audit_list"):
#     print(row)
def generate_report():
    # Connect to the database
    connection = sqlite3.connect("audit_list.db")
    cursor = connection.cursor()
    
    # Get all the audit features from the database
    cursor.execute("select * from audit_list")
    audit_features = cursor.fetchall()
    
    # Generate the report
    report = ""
    for feature in audit_features:
        report += f"Feature ID: {feature[0]}\n"
        report += f"Title: {feature[1]}\n"
        report += f"Description: {feature[2]}\n"
        report += f"Importance: {feature[3]}\n"
        report += f"Compliance: {feature[4]}\n\n"
    
    # Close the database connection
    connection.commit()
    connection.close()
    return report

def update_compliance(feature_id, compliance):
    connection = sqlite3.connect("audit_list.db")
    cursor = connection.cursor()

    cursor.execute("""
        update audit_list
        set compliance = :compliance
        where id = :id
    """, {"id": feature_id, "compliance": compliance}) 
    connection.commit()
    connection.close() 
    
def get_compliance(feature_id):
    connection = sqlite3.connect("audit_list.db")
    cursor = connection.cursor()

    cursor.execute("""
        select compliance
        from audit_list
        where id = :id
    """, {"id": feature_id})

    result = cursor.fetchone()

    connection.close()

    if result is None:
        return None
    return result[0]  
    
connection.commit()
connection.close()
