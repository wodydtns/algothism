import string


def check_ip_v4(ipv4: str) -> str:
    ipnums = ipv4.split(".")

    for num in ipnums:
        if len(num) == 0 or len(num) > 3:
            return 'Neither'

        if len(num) != 1 and num[0] == '0' or not num.isdigit() or int(num) > 255:
            return 'Neither'
        return 'IPv4'


def check_ip_v6(ipv6: str) -> str:
    ipnums = ipv6.split(":")

    for num in ipnums:
        if len(num) == 0 or len(num) > 4 or not all(c in string.hexdigits for c in num):
            return 'Neither'
    return 'IPv6'


def validIPAdress(IP: str) -> str:
    if IP.count(".") == 3:
        return check_ip_v4(IP)
    elif IP.count(".") == 7:
        return check_ip_v6(IP)
    return 'Neither'
