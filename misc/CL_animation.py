import time

symbols = '/-\|/-\|'

def waiting():
    while True:
        try:
            for symbol in symbols:
                print('Waiting... ' + symbol, end = '\r')
                time.sleep(0.2)
        except KeyboardInterrupt:
            break

def progress_bar(percentage):
    completed = percentage // 10
    remaining = 10 - completed
    print('|' +  completed * '=' + remaining * ' ' + '|')



#waiting()
progress_bar(10)
