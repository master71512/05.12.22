# 3) Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

data = open('D:/GB/Python/HW/05.12.22/1.txt', 'r')
string = data.read()
data.close()

def Spliter (string):
    array = [[1, string[0]]]
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            array[len(array)-1][0] += 1 
        else:
            array.append([1, string[i]])
    new_string = ''
    for i in array:
        new_string += str(i[0]) + i[1]
    return new_string    

def Decoder(string):
    new_string = ''
    for i in range(len(string)):
        if string[i].isdigit():
            new_string += int(string[i])*string[i+1]
    return new_string

if string.isalpha():
    result = Spliter(string)
else:
    result = Decoder(string)
data = open('D:/GB/Python/HW/05.12.22/2.txt', 'a')
data.write(result + '\n')
data.close()