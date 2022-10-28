

from itertools import count


def file_read_code():
    input_txt = open('input.txt', 'r')
    j = ""
    i = 0
    for line in input_txt:
        while i < len(line):
            count = 1
 
            while i + 1 < len(line) and line[i] == line[i + 1]:
                count = count + 1
                i = i + 1

            j += str(count) + line[i]
            i = i + 1
        
        file_write(j)
        print(line + " >> " + j)
    input_txt.close

def file_read_decode():
    input_txt = open('output.txt', 'r')
    j = ""
    i = 0
    for line in input_txt:
        col = 0
        while i < len(line):
            try:
                col = int(line[i])
                #print("попытка " + line[i])
                
                i = i + 1
            except:
                #print("Исключение " + line[i])
                while col != 0:
                    j = j + (line[i]) 
                    col = col - 1
                col = 0
                i = i + 1
        
        file_write_decode(j)
        print(line + " >> " + j)
    input_txt.close

def file_write(text):
   file_write = open('output.txt', 'w')
   file_write.write(text)
   file_write.close

def file_write_decode(text):
   file_write = open('input.txt', 'w')
   file_write.write(text)
   file_write.close

def main():

    do = int(input("Введите 0 для сжатия или 1 для восстановления: "))
    if do == 0:
        file_read_code()
    elif do == 1:
        file_read_decode()
    else:
        print("Выбрано не правильное значение")

main()