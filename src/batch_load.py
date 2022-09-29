from user_management import create_user
import csv

def create_users_from_csv(file_path):
    file = open(file_path, "r")
    data = list(csv.reader(file, delimiter=","))
    file.close()

    for row in data:
        user_email = row[0]
        print(user_email)
        create_user(user_email)
