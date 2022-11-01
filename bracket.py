def isValid(s: str) -> bool:
    stack = []

    paren_map = {
        ')': '(',
        '}': '{',
        '[': ']'
    }
    for ch in s:
        if ch not in paren_map.keys():
            stack.append(ch)
        else:
            pair = stack.pop() if stack else ''
            if paren_map[ch] != pair:
                return False
    print(len(stack) == 0)
    return len(stack) == 0


s = "((){})"
isValid(s)
