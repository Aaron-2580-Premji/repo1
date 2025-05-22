def char_count(sent):
    char_count = {}
    char=list(sent)
    list1 = []
    for i in char:
        if i != " ":
            list1.append(i)

    for i in list1:
        if i in char_count:
            char_count[i] +=1
        else:
            char_count[i] = 1
    print(char_count)


sentence=str(input("enter ur sentence"))
char_count(sentence)


