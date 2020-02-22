""" Census tool login validation """

def pcode_validation(pcode):
    passcode = []
    passcode.append(pcode)
    count = 1
    attempt = 4
    while(count < attempt):
        if (pcode == login_code):
            print("Welcome!!!")
            break
        elif (pcode in range(less, more +1)):
            print("InVaLiD PaSsCoDe")
        elif (pcode < less):
            print("invalid passcode")
        elif (pcode > more):
            print("INVALID PASSCODE")
        pcode = get_passcode()
        passcode.append(pcode)
        count += 1
    else:
        while(count == attempt):
            if (pcode == login_code):
                print("Welcome!!!")
                break
            elif (pcode in range(less, more +1)):
                print("InVaLiD PaSsCoDe")
            elif (pcode < less):
                print("invalid passcode")
            elif (pcode > more):
                print("INVALID PASSCODE")
            count += 1
            print("Login failed")
        else:
            for x in passcode:
                if( x != login_code and x in range(less, more +1)):
                    last = get_passcode()
                    if( last == login_code):
                        print("Welcome!!")
                        break
                    else:
                        print("Login Failed!!!")
        
def get_passcode():
    code = input("Enter Passcode :")
    code = int(code)
    return code

def main():
    pcode = get_passcode()
    pcode_validation(pcode)

#Main Start From Here
login_code = 15
less = login_code - 2 #13
more = login_code + 2 #17
main()
