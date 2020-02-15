""" String as required format """

def string_format(name,surname):
    print("Name:",name.lower(),"Surname:",surname.lower())
    print(name.upper(),surname.upper())
    print("--------------------------------")
    print(surname.capitalize(),",",name.capitalize())

def get_value():
    fname = input ("Enter first name : ")
    lname = input ("Enter last name : ")
    string_format(fname,lname)

def main():
    get_value()

#Main starts from here

main()
