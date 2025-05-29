#EXERCÍCIO 1

pop_A = 98000000
pop_B = 200000000
anos = 0

while pop_A < pop_B:
    pop_A *= 1.035
    pop_B *= 1.015
    anos += 1

print (f'A população do país A será maior que a população do país B em {anos} anos.')