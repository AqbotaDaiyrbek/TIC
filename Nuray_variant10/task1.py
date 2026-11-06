# 10-нұсқа. 1-есеп: Хэмминг 

data = "1011"
code = [0] * 8  

# Ақпараттық биттер: 3, 5, 6, 7
for pos, bit in zip([3, 5, 6, 7], data):
    code[pos] = int(bit)

# Бақылау биттері: 1, 2, 4 (N = 2^i)
code[1] = code[3] ^ code[5] ^ code[7]
code[2] = code[3] ^ code[6] ^ code[7]
code[4] = code[5] ^ code[6] ^ code[7]

C = "".join(str(bit) for bit in code[1:])

print("10-нұсқа, 1-есеп")
print("Ақпараттық комбинация:", data)
print("n_i = 4, n_k = 3, n = 7")
print("Бақылау позициялары: 1, 2, 4")
print("p1 = b3 XOR b5 XOR b7 =", code[1])
print("p2 = b3 XOR b6 XOR b7 =", code[2])
print("p4 = b5 XOR b6 XOR b7 =", code[4])
print("Соңғы C кодтық комбинациясы:", C)
