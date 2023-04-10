from teamreg.models import Student
import csv

with open('validregnos.csv', newline='') as file:
    reader = csv.reader(file)
    next(reader)
    for data in reader:
        Student(*data).save()
