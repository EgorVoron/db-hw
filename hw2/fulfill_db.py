import pymongo
import csv
import random

client = pymongo.MongoClient('localhost', 27017)
db = client.db_hw
customers = db.customers

with open('archive/Mall_Customers.csv', 'r+') as csv_file:
    reader = csv.reader(csv_file)
    for idx, line in enumerate(reader):
        if idx == 0:
            continue
        customer_id, sex, age, annual_income, spending_score = line
        document = {
            "customer_id": int(customer_id),
            "sex": sex,
            "age": int(age),
            "annual_income": int(annual_income),
            "spending_score": int(spending_score)
        }
        customers.insert_one(document)


# датасет мелкий (200 записей), так что догенерю еще (чтобы была заметна разница в скорости работы)
for idx in range(201, 200000):
    document = {
            "customer_id": idx,
            "sex": random.choice(["Male", "Female"]),
            "age": random.randint(18, 60),
            "annual_income": random.randint(15, 137),
            "spending_score": random.randint(1, 99)
        }
    customers.insert_one(document)
