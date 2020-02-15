""" Hello User name Program """

def welcome (name):
    print ("Hello", name, "!!!")

def get_name():
    name = input (" Enter your name: ")
    return name

def main():
    user_name = get_name()
    welcome(user_name)

#main start from here
main()
