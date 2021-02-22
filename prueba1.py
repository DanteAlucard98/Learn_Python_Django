import csv

data_as_json = [
    {'id': 1, 'student_name': 'Pablito Mix', 'birth_month': 'November', 'career': 'DJ'},
    {'student_name': 'JBalvin', 'birth_month': 'January', 'career': 'musician'},
    {'id':76, 'student_name': 'Toño', 'career': 'stalker'},
    {'student_name': 'Edgar'},
    {'id': 8},
    {'id': 35, 'student_name': 'Santiaguito', 'birth_month': 'December'},
    {'id': 8.0, 'student_name': 'DieGOL Maradona', 'career': 'soccer player'},
    {'id': 1, 'student_name': 'Pelé'},
    {'id': 'hji', 'student_name': 'Brad Pitt', 'birth_month': 'May', 'career': 'actor'}
]


with open('students_data.csv', mode='w') as csv_file:
    fieldnames = ['id', 'student_name', 'birth_month', 'career']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for key in data_as_json:
        writer.writerow(key)

with open('students_data.csv', mode='r') as csv_file:
    reader = csv.DictReader(csv_file)
    line_count = 0
    for row in reader:
        if line_count == 0:
            print(f'Column names are {",".join(row)}')
            line_count += 1
        print(f'\t{row["student_name"]} with id {row["id"]} is a {row["career"]}')
        line_count += 1
    print(f'Processed {line_count} lines.') 
            
with open('students_data.csv', mode='r') as read, open('students_data.csv', mode='r') as write:
    fieldnames = ['id', 'student_name', 'birth_month', 'career']
    writer = csv.DictWriter(write, fieldnames=fieldnames)
    reader = csv.DictReader(read)
    for row in reader:
        if row["id"]=="":
            print(f'\t{row["student_name"]} with id {row["id"]} is a {row["career"]}')
            writer.writerow(row)