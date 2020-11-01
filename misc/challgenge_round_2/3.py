with open('3_source.txt', 'r') as f:
    raw = f.read().replace('\n', '')

#print(raw)

#def checkBodyguards(s):
#    results = []
#    results = [True if char.isupper() else False for char in s]
#    results.pop(3)
#    print(results)
#    if False in results and s[3].isupper():
#        return ''
#    else:
#        return s[3]

def checkBodyguards(s):
    result = [0 if char.islower() else 1 for char in s]
#    print(s)
#    print(result)
    if result == [0,1,1,1,0,1,1,1,0]:
        return s[4]
    else:
        return ''
#print(checkBodyguards('FOOxBAR'))

def check_entire_string(long_string):
    solution = ''
    for i in range(4,len(long_string) - 4):
        snippet = long_string[i-4:i+5]
        solution = solution + checkBodyguards(snippet)
    print(solution)

def check_alpha(s):
    result = True
    for element in s:
        if not element.isalpha():
            result = False
    return result

#print(check_alpha(raw))
check_entire_string(raw)
#print(checkBodyguards('fOOxBAR'))
