# BAI 1
def bai_1():
    string = input('Nhap vao 1 chuoi: ')
    num = 0
    char = 0
    for i in string:
        if str.isdigit(i):
            num += 1
        else: char += 1
    print(f'So chu so: {num}')
    print(f'So chu cai: {char}')

# BAI 2
def bai_2():
    check = int(input('Nhap vao 1 so: '))
    prime_list = []
    if check > 1:
        for i in range(2, check+1):
            while check % i == 0:
                check /= i
                prime_list.append(str(i))
    print(' x '.join(prime_list))

# BAI 3
def bai_3():
    n = int(input('Nhap so phan tu can nhap: '))
    num_list = []
    for i in range(n):
        num_list.append(int(input(f'Phan tu [{i}]: ')))
    dem = 0
    max = num_list[0]
    for value in num_list:
        if value % 2 != 0:
            dem += 1
        if value > max:
            max = value
    print(f'Tong so phan tu le: {dem}')
    print(f'Phan tu lon nhat: {max}')

# BAI 4
def bai_4():
    a = int(input('Nhap a: '))
    b = int(input('Nhap b: '))
    s = a*b
    while a != b:
        if a > b:
            a -= b
        else: b -= a
    print(f'UCLN: {a}')
    print(f'BCNN: {s/a}')

# BAI 5
def bai_5():
    n = int(input('Nhap so luong sinh vien can nhap: '))
    student_list = []
    for i in range(n):
        student_list.append(input(f'{i}. Ten sinh vien: '))
    find_ = input('Nhap ten sinh vien can tim: ')
    print(f'Vi tri sinh vien: {student_list.index(find_)}')

# BAI 6
def bai_6():
    f = open('D:/Neko/file_data.txt', 'w')
    f.write('MaSV - Hoten - Tuoi - Email\n')
    f.write('---------------------------\n')
    f.write(str.upper(input('Nhap ma SV: ')))
    f.write(' - ')
    f.write(str.title(input('Nhap ho ten SV: ')))
    f.write(' - ')
    f.write(input('Nhap tuoi: '))
    f.write(' - ')
    f.write(str.lower(input('Nhap email: ')))
    f.write(' - ')
    f.write(input('Nhap dia chi: '))
    f = open('D:/Neko/file_data.txt', 'r')
    print(f.read())
    f.close()

# BAI 7
def bai_7():
    n = int(input('Nhap so phan tu can nhap: '))
    num_list = []
    for i in range(n):
        num_list.append(int(input(f'[{i}]. Nhap so: ')))
    for i, v in enumerate(num_list):
        if v % 2 == 0:
            if i == 0:
                print(v, end='')
            else: print(f', {v}', end='')

# BAI 8
from math import sqrt
def bai_8():
    a = int(input('Nhap a: '))
    b = int(input('Nhap b: '))
    c = int(input('Nhap c: '))
    if a == 0:
        if b == 0:
            if c == 0:
                print('Phuong trinh vo so nghiem !')
            else: print('Phuong trinh vo nghiem !')
        else:
            print(f'Phong trinh co nghiem kep: {-c/b}')
    else:
        delta = b*b - 4*a*c
        if delta < 0:
            print("Phuong trinh vo nghiem !")
        elif delta == 0:
            print('Phuong trinh co nghiem kep')
        else:
            print('Phuong trinh co 2 nghiem:')
            print(f'x1: {(-b+sqrt(delta))/(2*a)}')
            print(f'x2: {(-b-sqrt(delta))/(2*a)}')

# BAI 9
def bai_9():
    n = int(input('Nhap so: '))
    if n < 0:
        print('Khong hop le !')
        return
    for i in range(2, n+1):
        if i == 2:
            print(i, end='')
            continue
        for j in range(2, i):
            if i % j == 0:
                break
        else: print(f', {i}', end='')

# BAI 10
def bai_10():
    n = int(input('Nhap so phan tu can nhap: '))
    num_list = []
    for i in range(n):
        num_list.append(int(input(f'[{i}]: ')))
    max = num_list[0]
    for i in num_list:
        if i > max:
            max = i
    nd_max = num_list[0]
    for i in num_list:
        if i > nd_max and i < max:
            nd_max = i
    print(f'So lon thu 2: {nd_max}')

# BAI 11
def xuat(num_list):
    for i in range(len(num_list)):
        if i == 0:
            print(num_list[i], end='')
        else: print(f', {num_list[i]}', end='')

def bai_11():
    n = int(input('Nhap so phan tu can nhap: '))
    num_list = []
    for i in range(n):
        num_list.append(int(input(f'[{i}]: ')))
    xuat(num_list)
    print('\n', end='')

    num_list.sort()
    xuat(num_list)
    
    even_num = []
    for i in num_list:
        if i % 2 == 0:
            even_num.append(i)
    print('\n', end='')
    xuat(even_num)

# BAI 12
def bai_12():
    n = int(input('Nhap so: '))
    if n < 0:
        print('Khong hop le !')
        return
    for i in range(2, n+1):
        if i == 2:
            print(i, end='')
            continue
        for j in range(2, i):
            if i % j == 0:
                break
        else: print(f', {i}', end='')