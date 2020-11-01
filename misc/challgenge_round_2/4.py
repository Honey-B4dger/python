import urllib.request

def create_url(nothing):
    url_ = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    url = url_ + nothing
    return url

def determine_next_nothing(nothing):
    url = create_url(nothing)

    with urllib.request.urlopen(url) as response:
        html = response.read()
        s = html.decode('utf-8')
        print(s)
        next_nothing = ''.join([char for char in s if char.isdigit()])
        if 'Divide' in next_nothing:
            next_nothing = str(int(next_nothing) / 2)
        print(next_nothing)
        return next_nothing


previous_nothing = '3875'
for i in range(400):
    next_nothing = determine_next_nothing(previous_nothing)
    previous_nothing = next_nothing


