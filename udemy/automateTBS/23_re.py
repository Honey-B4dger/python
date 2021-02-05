import re

message = 'Call 214-555-1011 or 415-555-999'
message += ' 123-456-7890 foo'

phoneNumRegex = re.compile(r'\d\d\d\-\d\d\d-\d\d\d\d')

mo = phoneNumRegex.findall(message)
#print(mo.group())
print(mo)
