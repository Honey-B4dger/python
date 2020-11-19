import os

os.system('clear')

#######################################################################
# Ausgabe aller Schlüssel-Werte-Paare, zeilenweise

print('=' * 72)

processors = {
    "iPad Pro": "A12Z Bionic",
    "Mac mini": "M1",
    "MacBook Pro": "M1",
    "MacBook Air": "M1",
    "iPad Air": "A14 Bionic",
    "iPad": "A12 Bionic",
    "iMac": "Intel Core i7",
    "iPad mini": "A8",
    }

print('\nEs sind folgende Prozessoren verbaut:')

for model, processor in processors.items():
    print(f'\n- {model}: \t{processor}')

################################################################################
# Ausgabe der einzigartigen Werte, sortiert

print('\n' + '=' * 72 + '\n')

processors_only =[]

for model, processor in sorted(processors.items(), key = lambda item : item[1]):
    if processor not in processors_only:
        processors_only.append(processor)

print('Es kommen folgende Prozessoren zum Einsatz:\n')

for processor in processors_only:
    print(f'- {processor}')

# Ausgabe in einer Zeile
print('\nIn einer Zeile zusammengefasst:')
print('\n' + ', '.join(processors_only))

# alternativ:
print(', '.join(sorted(set(processors.values()))))

################################################################################
# Ausgabe des gesamten dictionary nach Werten sortiert

print('\n' + '=' * 72 + '\n')

print('Dies sind alles Schlüssel-Werte-Paare, sortiert nach den Werten:')

for m, p in sorted(processors.items(), key = lambda item: item[1]):
    print(f'\n- {m}: \t{p}')
