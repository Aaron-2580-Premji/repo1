def freq_word(paragrapgh):
    word_count = {}
    word=paragrapgh.split()
    for i in word:
        if i in word_count:
            word_count[i] +=1
        else:
            word_count[i] = 1
    print(word_count)

paragrapgh=str(input("enter ur sentence"))
freq_word(paragrapgh)