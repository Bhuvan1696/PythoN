""" Fibonacci """

def fibbo(number):
    count = 0
    a = 0
    b = 1
    while (count < number):
        print(a)
        n = a + b
        a = b
        b = n
        count += 1

def main():
    till_num = input ("Enter till number:")
    till_num = int(till_num)
    fibbo(till_num)

#Main start from here

main()
