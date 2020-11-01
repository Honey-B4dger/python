import re

# a = [1, 11, 21, 1211, 111221, ...]
# len(a[30]) = ?

def next_member(member):
    result = ''
    while len(member) > 0:
        digit = member[0]
        #print(digit)
        #rex = 'r' + '\'' + digit + '+\''
        match = re.match(r'{}'.format(digit + '+'), member).group(0)
        #print(match)
        result += str(len(match))
        result += digit
        member = member[len(match):]
    return (result)

#print(next_member('1211'))

member = '1'
for i in range(30):
    member = next_member(member)
    print(len(member))

