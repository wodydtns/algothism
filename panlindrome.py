def isPalindrome(s):
    i = 0
    j = len(s) - 1

    s = s.lower()
    flag = False
    while i < j:
        while i < j:
            if s[i].isalnum():
                break
            i += 1
        while i < j:
            if s[j].isalnum():
                break
            j -= 1
        if s[i] != s[j]:
            return flag
        i += 1
        j -= 1
    flag = True
    print(flag)
    return flag


def isPalindrome2(s):
    s = "".join(list(filter(str.isalnum, s))).lower()
    return s == s[::-1]


s = "Abbc, cbb a"
isPalindrome2(s)
