def checkLeap(year):
    if ( (year <= 1917) and (year%4 == 0)    or (( year%400 == 0) or (( year%4 == 0 ) and ( year%100 != 0)))):
        return True
    elif (year == 1918):
        return True
    else:
        return False

def dayOfProgrammer(year):
    check=checkLeap(year)

    if check == True and year == 1918:
        print("26.09.1918")

    elif check == True:
        print("12.09." + str(year))
        
    elif check == False:
        print("13.09." + str(year))
        



if __name__ == '__main__':
    year = int(input())
    dayOfProgrammer(year)

