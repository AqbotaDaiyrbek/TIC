codes = {
    "0": "A",
    "10": "B",
    "110": "C",
    "111": "D"
}

message = "1100111010"
result = ""
temp = ""

print("Берілген хабар:", message)

for bit in message:
    temp += bit

    if temp in codes:
        print(temp, "=", codes[temp])
        result += codes[temp]
        temp = ""

print("Декодталған хабар:", result)
