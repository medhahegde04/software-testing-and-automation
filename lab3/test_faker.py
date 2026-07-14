from faker import Faker
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Fake Data"
ws.append(["Name", "Address", "Email", "Phone Number", "Date Of Birth"])

fake_data = Faker()
for i in range(1, 11):
    ws.append([fake_data.name(), fake_data.address(), fake_data.email(), fake_data.phone_number(), fake_data.date_of_birth()])

wb.save("Fake_Data.xlsx")