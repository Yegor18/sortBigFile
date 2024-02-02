import random

with open('sample_input.txt', 'w') as file:
    for _ in range(100000):  
        file.write(f'{random.randint(1, 1000000)}\n')
    file.write(f'{random.randint(1, 1000000)}')
# В итоговом файле пустых строк быть не должно