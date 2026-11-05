# 8-нұсқа. Хэмминг (7,4) коды
# Биттер солдан оңға қарай 1-ден 7-ге дейін нөмірленеді.

info = '1000'
code = [0] * 7

# Ақпараттық биттер: 3, 5, 6, 7
for pos, bit in zip((3, 5, 6, 7), info):
    code[pos - 1] = int(bit)

# Жұптық бақылау биттері: 1, 2, 4
code[0] = code[2] ^ code[4] ^ code[6]
code[1] = code[2] ^ code[5] ^ code[6]
code[3] = code[4] ^ code[5] ^ code[6]

print('1-есеп')
print('Ақпараттық комбинация:', info)
print('Бақылау биттері: p1 =', code[0], ', p2 =', code[1], ', p4 =', code[3])
print('Дұрыс C:', ''.join(map(str, code)))

received = code.copy()
received[6] ^= 1  # 7-разрядты инверсиялау

# Синдром: s1, s2, s4
s1 = received[0] ^ received[2] ^ received[4] ^ received[6]
s2 = received[1] ^ received[2] ^ received[5] ^ received[6]
s4 = received[3] ^ received[4] ^ received[5] ^ received[6]
error_pos = s1 + 2 * s2 + 4 * s4

print('\n2-есеп')
print('Қабылданған C*:', ''.join(map(str, received)))
print(f'Тексеру мәндері: s1={s1}, s2={s2}, s4={s4}')
print(f'Синдром (s4s2s1): {s4}{s2}{s1}')
print('Синдром ондық жүйеде:', error_pos)

if error_pos:
    received[error_pos - 1] ^= 1
    print('Қате разряд:', error_pos)
else:
    print('Қате табылған жоқ')

print('Түзетілген C:', ''.join(map(str, received)))
