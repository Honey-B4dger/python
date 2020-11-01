import zipfile
import urllib.request


def txt_from_zip(filename):
    text = myZip.open(filename, 'r').read().decode('utf-8')
    return text

def comment_from_zip(filename):
    myZipInfo = myZip.getinfo(filename)
    comment = myZipInfo.comment.decode('utf-8')
    return comment

def determine_next_nothing(nothing):
    file = nothing + '.txt'
    extract = txt_from_zip(file)
    #print(extract)
    next_nothing = ''.join([char for char in extract if char.isdigit()])
    #print(next_nothing)
    return next_nothing

myZip = zipfile.ZipFile('resources/channel.zip', 'r')

infolist = myZip.infolist()
#print(type(infolist))
#print(len(infolist))
namelist = myZip.namelist()

#print(comment_from_zip('90052.txt'))
#print(txt_from_zip('readme.txt'))
#print(txt_from_zip('90052.txt'))

order = []
previous_nothing = '90052'
order.append(previous_nothing)

for i in range(len(infolist) - 1):
    next_nothing = determine_next_nothing(previous_nothing)
    previous_nothing = next_nothing
    order.append(previous_nothing)

order.pop(-1)
comments_in_order = []

for file in order:
    comments_in_order.append(comment_from_zip(file + '.txt'))

#print(comments_in_order)

s = ''.join(comments_in_order)
print(s)
#print(order)

