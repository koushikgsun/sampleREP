import csv


HeadRow = ["Sno.", "Name", "Age" , "Marks"]


with open("Marks.csv", 'a+') as file:
    reader = csv.reader(file)
    for row in reader