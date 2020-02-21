""" Student Mark Statement """

def grade(percentage, eng, sci, mat):
    if ( eng >= 25 and sci >= 35 and mat >= 35):
        if (percentage > 90):
            print ("Grade A")
        elif (percentage > 75 and percentage <= 90):
            print ("Grafe B")
        else:
            print ("Average")
    else:
        print("Fail..!")
        
def total_marks(eng, theory, practical, mat):
    if (eng <= 75 and theory <= 75 and practical <= 25 and mat <= 100):
        tot_sci = theory + practical
        total = eng + tot_sci + mat
        percent = total/3
        print ("Over all percentage :", percent)
        grade(percent, eng, tot_sci, mat)
    else:
        print(" Out of Marks..")
        
    
def get_marks():
    eng = input("Enter English out of 75 :")
    eng = int(eng)
    sci_thoery = input("Enter Science_Thoery out of 75 :")
    sci_thoery = int(sci_thoery)
    sci_practical = input("Enter Science_Pracical out of 25 :")
    sci_practical = int(sci_practical)
    mat = input("Enter Maths out of 100 :")
    mat = int(mat)
    return eng, sci_thoery, sci_practical, mat

def main():
    english, thoery, practical, maths = get_marks()
    total_marks(english, thoery, practical, maths)

#Main starts from here
main()
