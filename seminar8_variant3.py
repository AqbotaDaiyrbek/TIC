# Семинар 8, 3-нұсқа — Хэмминг коды (7,4)
data = "1001"
error_pos = 6

r = 0
while 2**r < len(data) + r + 1:
    r += 1

n = len(data) + r
code = [0] * (n + 1)
j = 0

for i in range(1, n + 1):
    if i & (i - 1):
        code[i] = int(data[j])
        j += 1

for k in range(r):
    p = 2**k
    for i in range(1, n + 1):
        if i & p and i != p:
            code[p] ^= code[i]

print("1-есеп")
print("Бақылау биттері:", [code[2**k] for k in range(r)])
print("Хэмминг коды:", "".join(map(str, code[1:])))

received = code.copy()
received[error_pos] ^= 1
print("\n2-есеп")
print("Қате код:", "".join(map(str, received[1:])))

syndrome = 0
for k in range(r):
    p = 2**k
    check = 0
    for i in range(1, n + 1):
        if i & p:
            check ^= received[i]
    syndrome += check * p

print("Синдром:", format(syndrome, f"0{r}b"))
print("Қате позициясы:", syndrome)
if 1 <= syndrome <= n:
    received[syndrome] ^= 1
print("Түзетілген код:", "".join(map(str, received[1:])))
