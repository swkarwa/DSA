def sort012(s: str):
    s = [_ for _ in s]
    i = 0;
    j = 0;
    k = len(s) - 1
    while (j <= k):
        if (s[j] == '0'):
            s[i], s[j] = s[j], s[i]
            i += 1
            j += 1
        elif (s[j] == '1'):
            j += 1
        else:
            s[j], s[k] = s[k], s[j]
            k -= 1
    print("".join(s))
    return "".join(s)

sort012("012012")
