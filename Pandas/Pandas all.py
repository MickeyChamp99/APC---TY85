# # # # # # # # # # # # # # import pandas as pd

# # # # # # # # # # # # # # data = {
# # # # # # # # # # # # # #     'Student_ID': [1, 2, 3, 4, 5],
# # # # # # # # # # # # # #     'Name': ['Amit', 'Neha', 'Riya', 'Raj', 'Sneha'],
# # # # # # # # # # # # # #     'Python': [80, 70, 90, 60, 85],
# # # # # # # # # # # # # #     'DBMS': [75, 80, 85, 65, 90],
# # # # # # # # # # # # # #     'Maths': [85, 75, 80, 70, 95]
# # # # # # # # # # # # # # }

# # # # # # # # # # # # # # df = pd.DataFrame(data)

# # # # # # # # # # # # # # print(df)

# # # # # # # # # # # # # # df['Total'] = df['Python'] + df['DBMS'] + df['Maths']
# # # # # # # # # # # # # # df['Average'] = df['Total'] / 3

# # # # # # # # # # # # # # print("\nTotal and Average Marks:")
# # # # # # # # # # # # # # print(df)

# # # # # # # # # # # # # # print("\nStudents with average above 75:")
# # # # # # # # # # # # # # print(df[df['Average'] > 75])










# # # # # # # # # # # # # import pandas as pd

# # # # # # # # # # # # # data = {
# # # # # # # # # # # # #     'Employee_ID': [101, 102, 103, 104, 105],
# # # # # # # # # # # # #     'Name': ['Amit', 'Neha', 'Raj', 'Riya', 'Sneha'],
# # # # # # # # # # # # #     'Department': ['CSE', 'IT', 'HR', 'CSE', 'IT'],
# # # # # # # # # # # # #     'Salary': [45000, 60000, 55000, 70000, 40000],
# # # # # # # # # # # # #     'Experience': [2, 5, 4, 7, 3]
# # # # # # # # # # # # # }

# # # # # # # # # # # # # df = pd.DataFrame(data)

# # # # # # # # # # # # # print(df)

# # # # # # # # # # # # # print("\nSalary above 50000:")
# # # # # # # # # # # # # print(df[df['Salary'] > 50000])

# # # # # # # # # # # # # print("\nAverage Salary:")
# # # # # # # # # # # # # print(df['Salary'].mean())

# # # # # # # # # # # # # print("\nH
# # # # # # # # # # # # # ighest Salary:")
# # # # # # # # # # # # # print(df['Salary'].max())

# # # # # # # # # # # # # print("\nEmployee with Highest Experience:")
# # # # # # # # # # # # # print(df[df['Experience'] == df['Experience'].max()])








# # # # # # # # # # # # import pandas as pd

# # # # # # # # # # # # data = {
# # # # # # # # # # # #     'Product_ID': [1, 2, 3, 4, 5],
# # # # # # # # # # # #     'Product_Name': ['Laptop', 'Mobile', 'Mouse', 'Keyboard', 'Tablet'],
# # # # # # # # # # # #     'Category': ['Electronics', 'Electronics', 'Accessories', 'Accessories', 'Electronics'],
# # # # # # # # # # # #     'Price': [50000, 20000, 500, 1000, 30000],
# # # # # # # # # # # #     'Quantity': [2, 5, 10, 4, 3]
# # # # # # # # # # # # }

# # # # # # # # # # # # df = pd.DataFrame(data)

# # # # # # # # # # # # df['Total_Amount'] = df['Price'] * df['Quantity']

# # # # # # # # # # # # print(df)

# # # # # # # # # # # # print("\nProduct with Highest Sales:")
# # # # # # # # # # # # print(df[df['Total_Amount'] == df['Total_Amount'].max()])






# # # # # # # # # # # import pandas as pd

# # # # # # # # # # # data = {
# # # # # # # # # # #     'Patient_ID': [1, 2, 3, 4, 5],
# # # # # # # # # # #     'Name': ['Amit', 'Neha', 'Raj', 'Riya', 'Sneha'],
# # # # # # # # # # #     'Age': [65, 45, 70, 30, 55],
# # # # # # # # # # #     'Disease': ['Diabetes', 'Fever', 'Heart', 'Cold', 'Asthma'],
# # # # # # # # # # #     'Medical_Charges': [60000, 20000, 80000, 15000, 55000]
# # # # # # # # # # # }

# # # # # # # # # # # df = pd.DataFrame(data)

# # # # # # # # # # # print(df)

# # # # # # # # # # # print("\nPatients above 60:")
# # # # # # # # # # # print(df[df['Age'] > 60])

# # # # # # # # # # # print("\nAverage Medical Charge:")
# # # # # # # # # # # print(df['Medical_Charges'].mean())

# # # # # # # # # # # print("\nMaximum Medical Charge:")
# # # # # # # # # # # print(df['Medical_Charges'].max())

# # # # # # # # # # # print("\nCharges above 50000:")
# # # # # # # # # # # print(df[df['Medical_Charges'] > 50000])









# # # # # # # # # # import pandas as pd

# # # # # # # # # # data = {
# # # # # # # # # #     'Order_ID': [1, 2, 3, 4, 5],
# # # # # # # # # #     'Customer': ['Amit', 'Neha', 'Raj', 'Riya', 'Sneha'],
# # # # # # # # # #     'Product': ['Laptop', 'Mobile', 'Mouse', 'Tablet', 'Keyboard'],
# # # # # # # # # #     'Quantity': [2, 1, 5, 2, 3],
# # # # # # # # # #     'Price': [40000, 20000, 500, 15000, 1000],
# # # # # # # # # #     'Discount': [2000, 1000, 200, 500, 100]
# # # # # # # # # # }

# # # # # # # # # # df = pd.DataFrame(data)

# # # # # # # # # # df['Final_Amount'] = df['Quantity'] * df['Price'] - df['Discount']

# # # # # # # # # # print("All Orders:")
# # # # # # # # # # print(df)

# # # # # # # # # # print("\nOrders above 5000:")
# # # # # # # # # # print(df[df['Final_Amount'] > 5000])

# # # # # # # # # # print("\nHighest Value Order:")
# # # # # # # # # # print(df[df['Final_Amount'] == df['Final_Amount'].max()])

# # # # # # # # # # print("\nAverage Order Value:")
# # # # # # # # # # print(df['Final_Amount'].mean())











# # # # # # # # # import pandas as pd

# # # # # # # # # data = {
# # # # # # # # #     'Student_ID': [1, 2, 3, 4, 5],
# # # # # # # # #     'Name': ['Amit', 'Neha', 'Raj', 'Riya', 'Sneha'],
# # # # # # # # #     'Department': ['CSE', 'IT', 'CSE', 'IT', 'CSE'],
# # # # # # # # #     'Total_Classes': [100, 100, 100, 100, 100],
# # # # # # # # #     'Classes_Attended': [80, 65, 90, 70, 95]
# # # # # # # # # }

# # # # # # # # # df = pd.DataFrame(data)

# # # # # # # # # df['Attendance_Percentage'] = (
# # # # # # # # #     df['Classes_Attended'] / df['Total_Classes']
# # # # # # # # # ) * 100

# # # # # # # # # print(df)

# # # # # # # # # print("\nStudents with attendance below 75%:")
# # # # # # # # # print(df[df['Attendance_Percentage'] < 75])









# # # # # # # # import pandas as pd

# # # # # # # # data = {
# # # # # # # #     'Product_ID': [1, 2, 3, 4, 5],
# # # # # # # #     'Product_Name': ['Laptop', 'Mobile', 'Mouse', 'Tablet', 'Keyboard'],
# # # # # # # #     'Category': ['Electronics', 'Electronics', 'Accessories', 'Electronics', 'Accessories'],
# # # # # # # #     'Price': [50000, 20000, 500, 30000, 1000],
# # # # # # # #     'Quantity': [2, 3, 10, 2, 5]
# # # # # # # # }

# # # # # # # # df = pd.DataFrame(data)

# # # # # # # # df['Total_Sales'] = df['Price'] * df['Quantity']

# # # # # # # # print(df)

# # # # # # # # print("\nSales above 10000:")
# # # # # # # # print(df[df['Total_Sales'] > 10000])

# # # # # # # # print("\nProduct with Maximum Sales:")
# # # # # # # # print(df[df['Total_Sales'] == df['Total_Sales'].max()])

# # # # # # # # print("\nAverage Sales:")
# # # # # # # # print(df['Total_Sales'].mean())


















# # # # # # # import pandas as pd

# # # # # # # data = {
# # # # # # #     'Amit': 80,
# # # # # # #     'Neha': 90,
# # # # # # #     'Raj': 65,
# # # # # # #     'Riya': 75,
# # # # # # #     'Sneha': 85
# # # # # # # }

# # # # # # # s = pd.Series(data)

# # # # # # # print("Student Marks:")
# # # # # # # print(s)

# # # # # # # print("\nMarks of Neha:")
# # # # # # # print(s['Neha'])

# # # # # # # print("\nMaximum Marks:")
# # # # # # # print(s.max())

# # # # # # # print("\nMinimum Marks:")
# # # # # # # print(s.min())

# # # # # # # print("\nAverage Marks:")
# # # # # # # print(s.mean())

# # # # # # # print("\nStudents scoring above 75:")
# # # # # # # print(s[s > 75])














# # # # # # import pandas as pd

# # # # # # data = {
# # # # # #     'Amit': 45000,
# # # # # #     'Neha': 60000,
# # # # # #     'Raj': 55000,
# # # # # #     'Riya': 70000,
# # # # # #     'Sneha': 40000
# # # # # # }

# # # # # # s = pd.Series(data)

# # # # # # print(s)

# # # # # # print("\nHighest Salary:")
# # # # # # print(s.max())

# # # # # # print("\nLowest Salary:")
# # # # # # print(s.min())

# # # # # # print("\nAverage Salary:")
# # # # # # print(s.mean())

# # # # # # print("\nEmployees earning above 50000:")
# # # # # # print(s[s > 50000])





















# # # # # import pandas as pd

# # # # # data = {
# # # # #     'Amit': 45000,
# # # # #     'Neha': 60000,
# # # # #     'Raj': 55000,
# # # # #     'Riya': 70000,
# # # # #     'Sneha': 40000
# # # # # }

# # # # # s = pd.Series(data)

# # # # # print(s)

# # # # # print("\nHighest Salary:")
# # # # # print(s.max())

# # # # # print("\nLowest Salary:")
# # # # # print(s.min())

# # # # # print("\nAverage Salary:")
# # # # # print(s.mean())

# # # # # print("\nEmployees earning above 50000:")
# # # # # print(s[s > 50000])






# # # # import pandas as pd

# # # # data = {
# # # #     'Laptop': 50000,
# # # #     'Mobile': 20000,
# # # #     'Mouse': 500,
# # # #     'Keyboard': 1500,
# # # #     'Tablet': 30000
# # # # }

# # # # s = pd.Series(data)

# # # # print("Product Prices:")
# # # # print(s)

# # # # print("\nPrices after 10% Increase:")
# # # # s = s * 1.10
# # # # print(s)

# # # # print("\nMost Expensive Product:")
# # # # print(s.idxmax())

# # # # print("\nProducts costing above 1000:")
# # # # print(s[s > 1000])







# # # import pandas as pd

# # # data = {
# # #     101: 45,
# # #     102: 65,
# # #     103: 70,
# # #     104: 35,
# # #     105: 80
# # # }

# # # s = pd.Series(data)

# # # print(s)

# # # print("\nAverage Age:")
# # # print(s.mean())

# # # print("\nOldest Patient:")
# # # print(s.idxmax())

# # # print("\nYoungest Patient:")
# # # print(s.idxmin())

# # # print("\nPatients above 60:")
# # # print(s[s > 60])









# # import pandas as pd

# # data = {
# #     'Amit': 80,
# #     'Neha': 65,
# #     'Raj': 95,
# #     'Riya': 70,
# #     'Sneha': 92
# # }

# # s = pd.Series(data)

# # print(s)

# # print("\nAverage Attendance:")
# # print(s.mean())

# # print("\nAttendance below 75:")
# # print(s[s < 75])

# # print("\nAttendance above 90:")
# # print(s[s > 90])

# # print("\nHighest Attendance:")
# # print(s.max())
























# import pandas as pd

# df = pd.read_csv('students.csv')

# print("First 5 Records:")
# print(df.head())

# print("\nLast 5 Records:")
# print(df.tail())

# df['Total'] = df['Python'] + df['DBMS'] + df['Maths']
# df['Average'] = df['Total'] / 3

# print("\nTotal and Average Marks:")
# print(df)

# print("\nStudents with Average above 75:")
# print(df[df['Average'] > 75])

# print("\nStudent with Highest Average:")
# print(df[df['Average'] == df['Average'].max()])

# print("\nSubject-wise Average:")
# print(df[['Python', 'DBMS', 'Maths']].mean())
