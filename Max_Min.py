""" finding single, double and triple digits
    finding maxium and minimum """

def max_min(list2):
    print(max(list2), ": Maximum")
    print(min(list2[:-1]), ": Minimum")

def digits(list1):
    for x in list1[:-1]:
        if (x < 10):
            print (x, " Single Digit ")
        elif (x < 100):
             print (x, " Double Digit ")
        elif (x < 1000):
            print (x, " Triple Digit ")
        else:
            print (x, "More digits")

def get_value():
    list = []
    number = input (" Enter number ")
    number = int (number)
    list.append(number)
    infinity = float ('inf') 
    while (number < infinity):
        if (number == 0):
            break
        else:
            number = input ("Enter the number : ")
            number = int (number)
            list.append(number)
    digits(list)
    max_min(list)

def main():
    get_value()
    
#Main starts from here
main()
