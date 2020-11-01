s = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle
qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

url = 'map'

def shiftASCII(char):
    code = ord(char)
    if code in range(97,121):
        new_code = code + 2
        return chr(new_code)
    elif code == 121:
        return 'a'
    elif code == 122:
        return 'b'
    else:
        return char

s_shifted = [shiftASCII(char) for char in s]
url_shifted = [shiftASCII(char) for char in url]

print(''.join(s_shifted))
print(''.join(url_shifted))

