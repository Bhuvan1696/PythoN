""" Square root of three digit positive number """

def sqaure_root(values):
    all_numbers = values
    for x in all_numbers:
        if (x < 1000 and x > 100):
            sqrt = x ** 0.5
            print (sqrt, "Square root of :", x)
        else:
            continue

def get_numbers():
    numbers = []
    count = 0
    value = input("Enter the number :")
    value = int(value)
    numbers.append(value)
    while(value != 0):
        num = input("Enter the number :")
        num = int(num)
        numbers.append(num)
        value = num
        count += 1
    return numbers

def main():
    values = get_numbers()
    sqaure_root(values)
    
#Main starts from here
main()
