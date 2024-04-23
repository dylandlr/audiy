from audit_data import audit_features

data = [(feature['id'], feature['title'], feature['description'], feature['importance'], feature['compliance']) for feature in audit_features]

print(data)