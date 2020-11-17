import datetime

t = str(datetime.datetime.today())

t = t.split()

print(f'Das heutige Datum ist der {t[0]}')

print('')

print(f'Die aktuelle Uhrzeit ist {t[1][0:8]}')
