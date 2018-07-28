in1=[6676, 3216, 4063, 8373, 423, 586, 8850, 6762]

def reverseArray(a):
    n = len(a)
    answerStr = str(a[n-1])
    for i in range(1,n):
        answerStr += " "+str(a[n-i-1])
    return answerStr

print(reverseArray(in1))