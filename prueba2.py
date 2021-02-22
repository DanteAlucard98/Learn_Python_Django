import csv

with open('students_data.csv', mode='r') as read,open('students_data.csv', mode='w') as write :
    reader = csv.DictReader(read)
    fieldnames = ['id', 'student_name', 'birth_month', 'career']
    writer = csv.DictWriter(write,fieldnames=fieldnames)

    for row in reader:
        if row["id"]==1:
            print(f'\t{row["student_name"]} with id {row["id"]} is a {row["career"]}')