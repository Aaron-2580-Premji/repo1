def prime_numbers(num):
    for i in range(2,int(num** 0.5) + 1):
        if num%i == 0:
            return False
    return True
        
start= int(input("Enter the range "))
end=int(input("enter the end range"))   
for num in range(start,end+1):
    if prime_numbers(num):
        print(num)
