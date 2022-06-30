from math import ceil

# n - кількість чисел
# w - ширина, кількість стовпчиків
# start - з якого числа почати (необов'язково)
def numbers_table(nums, width, start=1):
    # Змінна для збереження результату
    table = ''

    # Останнє число в таблиці
    end = start + nums

    # Розрахування ширини всередині однієї клітинки, на основі найбільшого числа
    # Для того, щоб табличка була рівною
    cell_width = len(str(end))

    # Цикл 
    i = start
    while i < end:
        for j in range(abs(width)):
            if i > end: break
            table += str(i)
            table += (cell_width - len(str(i)) + 1) * ' '
            i += 1
        table += '\n'
        
    return table
    
print( numbers_table(15, 3) )
