def insert(dict1,name,marks):
    dict1[name] = marks
    print(dict1)

def search(dict1,name):
    print(dict1[name])


def main():
    dict1 = {}
    i = 0
    while i != -1:
        name = str(input("Enter the name: "))
        marks = int(input("Enter the marks: "))
        insert(dict1,name,marks)
        print("Do you want to search a name: ")
        check = str(input("Enter Yes or No: "))
        if check == "Yes" or "yes":
            name1= str(input("Enter the name to search: "))
            search(dict1,name1)
    i = int(input("DO you wannt to give input: type -1 to exit:  "))
    i+=1

main()