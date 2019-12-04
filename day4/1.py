from collections import Counter

RANGE_MIN = 124075
RANGE_MAX = 580769

def validated(password_digits):
    flag = False
    for d in range(1, len(password_digits)):
        if(password_digits[d] < password_digits[d-1]):
            return False
        else:
            # if last
            if(d == len(password_digits)-1):
                if(password_digits[d] == password_digits[d-1]):
                    return True
                elif(flag == True):
                    return True
                else:
                    return False
            # otherwise...
            else:
                if(password_digits[d] > password_digits[d-1]):
                    continue
                elif(password_digits[d] == password_digits[d-1]):
                    flag = True
                    continue
                else:
                    return False

def start():
    counter = 0
    for password in range(RANGE_MIN, RANGE_MAX):
        password_digits = [int(d) for d in str(password)]
        if(validated(password_digits)):
            counter += 1
    print(counter)
start()