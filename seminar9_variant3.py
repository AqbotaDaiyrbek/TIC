# Семинар 9, 3-нұсқа — Біркелкі және префикстік кодтар
N = 79
message = "10110111010"
codes = {"A": "0", "B": "10", "C": "110", "D": "111"}

# 1-есеп: ең аз бит саны
k = 0
while 2**k < N:
    k += 1
print("1-есеп")
print("Алфавит саны:", N)
print("Қажетті бит саны:", k)
print(f"Тексеру: 2^{k} = {2**k} >= {N}")

# 2-есеп: Фано шартын тексеру және декодтау
fano = True
for a in codes:
    for b in codes:
        if a != b and codes[b].startswith(codes[a]):
            fano = False

print("\n2-есеп")
print("Фано шарты:", "Орындалады" if fano else "Орындалмайды")

result = ""
parts = []
temp = ""
for bit in message:
    temp += bit
    for letter, code in codes.items():
        if temp == code:
            result += letter
            parts.append(temp)
            temp = ""
            break

print("Бастапқы хабар:", message)
print("Кодтарға бөліну:", " | ".join(parts))
print("Декодталған хабар:", result)
if temp:
    print("Декодталмаған бөлік:", temp)
