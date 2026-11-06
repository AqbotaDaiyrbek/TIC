
# 1-нұсқа. Хэмминг коды

data = "0100"
n_i = len(data)
n_k = 3
n = n_i + n_k

print("=== 1-ЕСЕП ===")
print("Ақпараттық комбинация:", data)
print("Ақпараттық биттер саны:", n_i)
print("Бақылау биттер саны:", n_k)
print("Жалпы биттер саны:", n)

# Бақылау позициялары: 1, 2, 4
code = [0] * (n + 1)
j = 0

for i in range(1, n + 1):
    if i not in [1, 2, 4]:
        code[i] = int(data[j])
        j += 1

# Жұптық ережесі
code[1] = code[3] ^ code[5] ^ code[7]
code[2] = code[3] ^ code[6] ^ code[7]
code[4] = code[5] ^ code[6] ^ code[7]

print("a1 =", code[1])
print("a2 =", code[2])
print("a4 =", code[4])

C = "".join(map(str, code[1:]))
print("Хэмминг коды C =", C)

print("\n=== 2-ЕСЕП ===")

# 3-разрядты бұрмалау
received = code.copy()
received[3] ^= 1

C_star = "".join(map(str, received[1:]))
print("Қабылданған C* =", C_star)

# Синдром есептеу
E1 = received[1] ^ received[3] ^ received[5] ^ received[7]
E2 = received[2] ^ received[3] ^ received[6] ^ received[7]
E3 = received[4] ^ received[5] ^ received[6] ^ received[7]

syndrome = f"{E3}{E2}{E1}"
error_pos = int(syndrome, 2)

print("E1 =", E1)
print("E2 =", E2)
print("E3 =", E3)
print("Синдром (екілік) =", syndrome)
print("Синдром (ондық) =", error_pos)
print("Қате позициясы =", error_pos)

# Қатені түзету
if error_pos != 0:
    received[error_pos] ^= 1

corrected = "".join(map(str, received[1:]))
print("Түзетілген код =", corrected)
