import csv
with open('C:/Users/premj/OneDrive/Desktop/student.csv','r') as file:
    reader = csv.reader(file)
    next(reader)

    print("Students scoring above 75%:")
    for i in reader:
        name = i[0]
        marks = int(i[1])
        if marks > 75:
            print(name)
