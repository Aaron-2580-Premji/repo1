ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
            "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
            "seventeen", "eighteen", "nineteen"]

tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

n=int(input("enter ur number"))
def num_word(n):
    if n<20:
        word=print(ones[n])

    elif 20<n<100:
        word=print(tens[n//10] +" "+ ones[n%10])

    elif 100<n<1000:
        word1=ones[n//100] +" "+ "hundred"
        result=n%100
        word2= print(word1 +" " + tens[result//10] +" "+ ones[result%10] )

    elif 1000<n<10000:
        word1=ones[n//1000]+" "+"thousand"
        result=n%1000
        word2=word1+" "+ ones[result//100] +" "+ "hundred"
        result=result%100
        word3= print(word2+" "+ tens[result//10] +" "+ ones[result%10] )

num_word(n)

    

