# Имитация машины Тьюринга в случае конечной ленты

# набор команд
R = 1
L = -1
S = 0

# обозначения позиции элемента
per = 0
move = 1
step = 2

# список, соответствующий стартовому состоянию
list_ = list(str(input()))


# функция "Машина Тьюринга" с 4 параметрами:
# code - программа, tape - лента машины Тьюринга,
# start - начальное состояние; cell - начальная позиция на ленте
def turing_machine(code, tape, start, cell):
    state = start
    while True:
        rows = code[state]
        row = rows[int(tape[cell])]
        tape[cell] = row[per]
        if not row[move]:
            break
        cell += row[move] 
        state = row[step]
    return tape


# запуск машины с начальными данными
result = turing_machine({
    'A' : ((0, R, 'A'), (1, R, 'B')),
    'B' : ((1, S, 'C'), (1, R, 'B')),
    'C' : ((0, S, 'C'), (1, S, 'C'))}, 
    list_, "A", 0)
    
print(result)
