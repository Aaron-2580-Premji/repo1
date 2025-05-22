str1=str(input("enter word 1:"))
str2=str(input("enter word 2:"))
i=0 
j=0
def checker(str1,str2):
    word1 = list(str1)
    word2 = list(str2)
    flag = 0 
    for i in range(len(word1)):
        for j in range(len(word2)):
            if sorted(word1[i]) not in sorted(word2[j]):
                flag = 1
            else:
                flag = 0 

    if flag == 0:
        print("Not anagram")    
    else:
        print("anagram")
    
checker(str1,str2)
        


