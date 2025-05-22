with open("C:/Users/premj/OneDrive/Desktop/example.txt",'r') as file:
    line=file.readlines()
    line_count=len(line)
    word_count=0
    char_count=0
    for i in line:
        word_count+=len(i.split())
        char_count+=len(i)

print(line_count)
print(word_count)
print(char_count)