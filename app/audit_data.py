# audit_data.py
# audit features data for the application
# This file contains the audit features data that is used to populate the audit list in the application. 
# The audit features data includes the title, description, importance, and compliance status of each feature. 
# The audit features data is used to display the audit list in the application and allow users to check off the compliance status of each feature.
# The audit features data is a list of dictionaries, where each dictionary represents an audit feature. Each audit feature dictionary includes the following fields:

# id: The unique identifier of the audit feature.
# title: The title or name of the audit feature.
# description: A description of the audit feature and its requirements.
# importance: The importance level of the audit feature (e.g., high, medium, low).
# compliance: A boolean flag indicating whether the audit feature is compliant or not.

# 
audit_features = [
    (1, 'User Authentication', 'Ensure user authentication mechanisms are secure, implementing strong password policies and considering two-factor authentication.', 'High', 0),
    (2, 'Data Encryption', 'Sensitive data such as user information and ToDo items should be encrypted both at rest and in transit.', 'High', 0),
    (3, 'SQL Injection Prevention', 'Implement measures to prevent SQL injection attacks, such as using parameterized queries or ORM frameworks.', 'High', 0),
    (4, 'Cross-Site Scripting (XSS) Protection', 'Ensure all user input is sanitized to prevent XSS attacks, especially in areas where user-generated content is displayed.', 'Medium', 0),
    (5, 'Error Handling', 'Properly manage error handling to prevent leakage of sensitive information through error messages or stack traces.', 'Medium', 0),
    (6, 'API Security', 'Secure all APIs with appropriate authentication and ensure sensitive endpoints are not exposed unnecessarily.', 'High', 0),
    (7, 'Logging and Monitoring', 'Implement comprehensive logging and monitoring to detect and respond to potential security incidents promptly.', 'Medium', 0),
    (8, 'Session Management', 'Sessions should be securely managed, implementing timeouts and proper session invalidation on logout.', 'High', 0),
    (9, 'Server Security', 'Ensure that the server hosting the application is secured and regularly updated to protect against known vulnerabilities.', 'High', 0),
    (10, 'Third-party Dependencies', 'Regularly update and audit third-party libraries and dependencies to protect against vulnerabilities.', 'Medium', 0)
]



# audit_features = [
#     {
#         "id": 1,
#         "title": "User Authentication",
#         "description": "Ensure user authentication mechanisms are secure, implementing strong password policies and considering two-factor authentication.",
#         "importance": "High",
#         "compliance": 0
#     },
#     {
#         "id": 2,
#         "title": "Data Encryption",
#         "description": "Sensitive data such as user information and ToDo items should be encrypted both at rest and in transit.",
#         "importance": "High",
#         "compliance": 0
#     },
#     {
#         "id": 3,
#         "title": "SQL Injection Prevention",
#         "description": "Implement measures to prevent SQL injection attacks, such as using parameterized queries or ORM frameworks.",
#         "importance": "High",
#         "compliance": 0
#     },
#     {
#         "id": 4,
#         "title": "Cross-Site Scripting (XSS) Protection",
#         "description": "Ensure all user input is sanitized to prevent XSS attacks, especially in areas where user-generated content is displayed.",
#         "importance": "Medium",
#         "compliance": 0
#     },
#     {
#         "id": 5,
#         "title": "Error Handling",
#         "description": "Properly manage error handling to prevent leakage of sensitive information through error messages or stack traces.",
#         "importance": "Medium",
#         "compliance": 0
#     },
#     {
#         "id": 6,
#         "title": "API Security",
#         "description": "Secure all APIs with appropriate authentication and ensure sensitive endpoints are not exposed unnecessarily.",
#         "importance": "High",
#         "compliance": 0
#     },
#     {
#         "id": 7,
#         "title": "Logging and Monitoring",
#         "description": "Implement comprehensive logging and monitoring to detect and respond to potential security incidents promptly.",
#         "importance": "Medium",
#         "compliance": 0
#     },
#     {
#         "id": 8,
#         "title": "Session Management",
#         "description": "Sessions should be securely managed, implementing timeouts and proper session invalidation on logout.",
#         "importance": "High",
#         "compliance": 0
#     },
#     {
#         "id": 9,
#         "title": "Server Security",
#         "description": "Ensure that the server hosting the application is secured and regularly updated to protect against known vulnerabilities.",
#         "importance": "High",
#         "compliance": 0
#     },
#     {
#         "id": 10,
#         "title": "Third-party Dependencies",
#         "description": "Regularly update and audit third-party libraries and dependencies to protect against vulnerabilities.",
#         "importance": "Medium",
#         "compliance": 0
#     }
# ]
