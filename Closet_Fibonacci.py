""" Print closet fibonacci number """

def fibbo(number):
    num1 = 0
    num2 = 1
    count = 0
    while(count < 20):
        n = num1 + num2
        num1 = num2
        num2 = n
        if( num1 == number or num2 == number):
            print("Fibonacci:",number)
            break
        elif( num1 < number and num2 > number):
            print(num1, number, num2)
            c = number - num1
            d = num2 - number
            if c < d:
                print( "Closest number", num1)
            else:
                print( "Closest number", num2)
        count += 1

def get_value():
    value = input("Enter the number")
    value = int (value)
    fibbo(value)

def main():
    get_value()
    
#Main start from here

main()
