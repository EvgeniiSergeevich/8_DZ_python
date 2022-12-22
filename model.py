import codecs
import csv

def add_people(data):                                 # Добавление нового пользователя(работника)
    with codecs.open('base.csv', 'a', 'utf_8') as f:
        writer = csv.writer(f,delimiter=';')
        writer.writerows([data.split()])

def read_file():                                        # Метод для чтения в список
    with codecs.open('base.csv', 'r', 'utf_8') as f:
        base = f.readlines()
        return base

def write_file(data):                                   # Метод для перезаписи списка в файл
    with codecs.open('base.csv', 'w', 'utf_8') as f:
        writer = csv.writer(f,delimiter=';')
        writer.writerows(data)


def remove_people(data):                        # Можно удалять по id или по строке целиком
    base = read_file()
    count = 0
    data = data.split(';')
    for i in range(1, len(base)):
        base1 = base[i].split(';')
        for j in range(len(data)):
            if data[j] == base1[j]:
                count = i
                break
    if count != 0:
        base.pop(count)
        new_base = []
        for k in base:
            new_base.append(k.split(';'))
        
        print(new_base)
        write_file(new_base)
   

# remove_people('3')



def find_people(data):
    data = str(data)
    base = read_file()
    matches = [match for match in base if data in match]
    if len(matches) > 1:
        for i in range(len(matches)):
            if matches[i][0] == data:
                matches = matches[i]
    return matches
            

# print(find_people('2'))

def edit_people(id, new_data):              # Редактирует данные по id
    base = read_file()
    tmp = find_people(id)
    for i in range( len(base)):
        l = []
        if tmp == base[i]:
            l = base[i].split(';')
            if type(new_data) == int:
                l[2] = new_data
                # print('1 if ', l)
                base[i] = ';'.join(map(str, l))
                break
            elif "@" in new_data:
                l[4] = new_data
                print('2 if ', l)
                base[i] = ';'.join(map(str, l))
                break
            elif len(new_data.split()) == 2 and new_data.istitle():
                l[1] = new_data
                # print('3 if ', l)
                base[i] = ';'.join(map(str, l))
                break
            else:
                l[4] = new_data
                # print('4 if ', l)
                base[i] = ';'.join(map(str, l))
                break
    new_base = [i.split(';') for i in base]
    write_file(new_base)




# edit_people(1, 'asfasf@asd.com')