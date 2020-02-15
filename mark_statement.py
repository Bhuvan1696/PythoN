""" Student Mark Statement """


def mark_statement(english,science,maths):
    avg = (english + science + maths) / 3
    print ("Your average is :", avg)
    if (english > 35 and science > 35 and maths > 35):
        if (avg >= 75 and avg <90):
            print ("Second class")
        elif(avg >= 90):
            print(" First class")
        else:
            print (" Average ")
    else:
        print (" Failed ")
    
def get_marks():
    eng = input ("Enter english marks out of 80 :")
    sci = input ("Enter science marks out of 90 :")
    mat = input ("Enter Maths marks out of 100 :")
    eng = int(eng)
    sci = int(sci)
    mat = int(mat)
    mark_statement(eng,sci,mat)

def main():
    get_marks()

#Main start from here

main()
