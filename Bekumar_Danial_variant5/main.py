
from math import ceil, log2

def hamming(data):
    r = 0
    while 2**r < len(data) + r + 1:
        r += 1
    c = list(data)
    for p in [2**i for i in range(r)]:
        c.insert(p-1, "0")
    for p in [2**i for i in range(r)]:
        c[p-1] = str(sum(int(c[i-1]) for i in range(1,len(c)+1) if i & p) % 2)
    print("Хэмминг:", "".join(c))

def check(c):
    s = 0
    for p in [2**i for i in range(len(c).bit_length())]:
        if sum(int(c[i-1]) for i in range(1,len(c)+1) if i & p) % 2:
            s += p
    print("Ошибка:", s)
    if 0 < s <= len(c):
        c = list(c)
        c[s-1] = str(1-int(c[s-1]))
        print("Исправлено:", "".join(c))

def fano(c):
    return all(a == b or not b.startswith(a) for a in c for b in c) and len(c)==len(set(c))

while True:
    print("\n1. Хэмминг\n2. Исправление ошибки\n3. Расстояние")
    print("4. Минимум бит\n5. Фано\n6. Средняя длина\n7. Максимум символов\n0. Выход")
    x = input("Выбор: ")
    if x == "0":
        break
    try:
        if x == "1":
            hamming(input("Биты: "))
        elif x == "2":
            check(input("Код: "))
        elif x == "3":
            a, b = input("Два кода через пробел: ").split()
            print("Расстояние:", sum(i != j for i,j in zip(a,b)) if len(a)==len(b) else "Ошибка длины")
        elif x == "4":
            n = int(input("Символов: "))
            print("Бит:", ceil(log2(n)))
        elif x == "5":
            n = int(input("Количество букв: "))
            d = dict(input("Буква и код: ").split() for _ in range(n))
            if fano(list(d.values())):
                msg = input("Сообщение: ")
                res, buf = "", ""
                for bit in msg:
                    buf += bit
                    if buf in d.values():
                        res += next(k for k,v in d.items() if v==buf)
                        buf = ""
                print("Результат:", res)
            else:
                print("Условие Фано не выполняется")
        elif x == "6":
            n = int(input("Количество букв: "))
            s = 0
            for _ in range(n):
                p, l = map(float, input("Частота (%) и длина: ").split())
                s += p*l/100
            print("Средняя длина:", s)
        elif x == "7":
            print("Символов:", 2**int(input("Бит: ")))
    except (ValueError, StopIteration, IndexError):
        print("Ошибка ввода")
