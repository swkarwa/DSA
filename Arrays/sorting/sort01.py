def sort01(s: str):
    s = [_ for _ in s]
    i = 0
    j = 0
    while(i< len(s)):
        if(s[i]=='0'):
            s[i], s[j] = s[j], s[i]
            j+=1
        i+=1
    print("".join(s))

def sort01a2(s: str):
    s = [_ for _ in s]
    i = 0
    for j in range(len(s)):
        if(s[j]=='0'):
            s[i], s[j] = s[j], s[i]
            i+=1
    print("".join(s))

sort01a2("1101011010001")

