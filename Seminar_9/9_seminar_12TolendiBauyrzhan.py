# 9-seminar, 12-nusqa
# Prefix kod jane Fano sharty

# 1-esep

N = 150
k = 0

while 2 ** k < N:
    k += 1

print("1-esep")
print("Alfavit sany:", N)
print("Bir simvolga kerek bit sany:", k)


# 2-esep

kodtar = {
    "0": "A",
    "10": "B",
    "110": "C",
    "111": "D"
}

habar = "01101110110"
natizhe = ""
basy = ""

for bit in habar:
    basy += bit

    if basy in kodtar:
        natizhe += kodtar[basy]
        basy = ""

print("\n2-esep")
print("Berilgen habar:", habar)
print("Dekodtalgan habar:", natizhe)

if basy == "":
    print("Dekodtau satti ayaqtaldy")
else:
    print("Qate: kodtalmağan bit bar")
