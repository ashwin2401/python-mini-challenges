# --------------
#Code starts here
def palindrome(num):
    num=num+1
    num=str(num)
    if num==num[::-1]:
        return int(num)
    else:
        while num != num[::-1]:
            num=int(num)+1
            num=str(num)
        return int(num)


# --------------
#Code starts here
def a_scramble(str_1,str_2):
    str_1 = str_1.upper()
    list_1 = str_1.split()
    str_2 = str_2.upper()
    chk=[]


    for element1 in list_1:
        chk_2=[]
        for element2 in element1:
            if element2 in str_2:
                chk_2.append(True)
            else:
                chk_2.append(False)
        if any(chk_2):
            chk.append(True)
        else:
            chk.append(False)
        print(chk_2)
    
    if all(chk):
        return True
    else:
        return False


# --------------
#Code starts here
def check_fib(num):
    a = 1
    b = 2
    total = 0
    chk=[]
    while (num>=total):
        total = a+b
        a=b
        b=total
        chk.append(total)
    if num in chk:
        return True
    else:
        return False


# --------------
#Code starts here
def compress(word):
    word=word.lower()
    newStr=word[0]+"1"
    for char in word[1:]:
        if newStr[-2]==char:
            newStr = newStr[:-1]+str(int(newStr[-1])+1)
        else:
            newStr=newStr+char+"1"
    return  newStr


# --------------
#Code starts here
def k_distinct(string,k):
    string = string.lower()
    str_2 = ""
    for i in string:
        if i not in str_2:
            str_2 = str_2+i
    return k==len(str_2)


