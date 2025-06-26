#Функция по поиску минимального числа клеток для закрашивания
def find_min(data_set, n:int, k:int):
        sequence = 'B' * k
        index = data_set.find(sequence)
        #Если последовательность k закрашенных клеток есть в исходной последовательности то вернётся значение 0
        if index != -1:
            return 0
        else:
            size_reduce_sequence = k

            #Поиск максимальной последовательности закрашенных клеток, но меньшей длины k
            while(index == -1):
                sequence = sequence[:-1]
                index = data_set.find(sequence)
                size_reduce_sequence -= 1
                if size_reduce_sequence == 0: return k #Если в последовательности нет закрашенных клеток то вернётся значение k
            additional_size_sequence = k - size_reduce_sequence
            
            #Поиск всех возможных последовательностей максимальной длины
            set_index_sequence = set()
            while(index != -1):
                set_index_sequence.add(index)
                index = data_set.find(sequence, index+size_reduce_sequence)
            
            #Подсчет числа незакрашенных клеток с двух сторон
            set_num_W = set()
            for i in set_index_sequence:
                if i!=0:
                    num = data_set[i-additional_size_sequence:i].count('W')
                    set_num_W.add(num)
                if i + size_reduce_sequence !=n:
                    num = data_set[i + size_reduce_sequence:i+k].count('W')
                    set_num_W.add(num)
            #Выбор минимального значения
            return min(set_num_W)

#Получение числа последовательностей
t = int(input())
for i in range(t):
    # Получение значений n, k и последовательности клеток
    n, k = map(int, input().split())
    data_set = input()

    #Вывод результата
    print(find_min(data_set, n, k))
