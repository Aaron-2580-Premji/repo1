def longest(string):
    word = string.split()
    largest = ""
    for i in word:
        if len(i)>len(largest):
            largest= i
        
    print("the largest word is",largest)


string=str(input("enter ur sentence"))
longest(string)