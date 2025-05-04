s = "ababbcdefab"
ss = "ab"

def solution(s , ss):
    i = len(ss)
    j = 0
    count = 0
    while(i < len(s)):
        temp = s[j:i]
        if(temp == ss):
            count+=1
        i+=1
        j+=1
    if(s[j:i] == ss):
        count+=1
    print(count)

solution(s , ss)
