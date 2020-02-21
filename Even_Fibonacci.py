""" First 12 even Fibonacci Number """

def even_fibbo():
    num1 = 1
    num2 = 1
    count = 0
    while (count < 38):
        even = num1 % 2
        if (even == 0):
            print(num1)
        number = num1 + num2
        num1 = num2
        num2 = number
        count += 1
        
def main():
    even_fibbo()

#Main starts from here

main()
