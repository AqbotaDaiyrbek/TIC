# 10-нұсқа. 2-есеп: 5-разрядтағы қатені тауып түзету
# 1-есептен алынған дұрыс код: 0110011

C = "0110011"
received = [int(bit) for bit in C]


received[4] = 1 - received[4]
C_star = "".join(str(bit) for bit in received)


s1 = received[0] ^ received[2] ^ received[4] ^ received[6]
s2 = received[1] ^ received[2] ^ received[5] ^ received[6]
s4 = received[3] ^ received[4] ^ received[5] ^ received[6]

syndrome_binary = f"{s4}{s2}{s1}"
error_position = int(syndrome_binary, 2)

print("10-нұсқа, 2-есеп")
print("Дұрыс C комбинациясы:", C)
print("5-разряд бұзылған C*:", C_star)
print("s1 =", s1, ", s2 =", s2, ", s4 =", s4)
print("Синдром (s4s2s1):", syndrome_binary)
print("Синдром (ондық):", error_position)

if error_position != 0:
    received[error_position - 1] = 1 - received[error_position - 1]
    print("Қате разряд:", error_position)
else:
    print("Қате табылмады")

corrected = "".join(str(bit) for bit in received)
print("Түзетілген комбинация:", corrected)
print("Бастапқы C-мен бірдей ме?", corrected == C)
