# 12-nusqa
# Hemming kodyn kuru jane kateni tuzetu

akparat = "10110101"
n = 12
bakylau = [1, 2, 4, 8]

# 1-esep

kod = [0] * (n + 1)

j = 0
for i in range(1, n + 1):
    if i not in bakylau:
        kod[i] = int(akparat[j])
        j += 1

for p in bakylau:
    kosyndy = 0
    for i in range(1, n + 1):
        if (i & p) and i != p:
            kosyndy ^= kod[i]
    kod[p] = kosyndy

C = "".join(str(kod[i]) for i in range(1, n + 1))

print("1-esep")
print("Akparat:", akparat)
print("Bakylau poziciyalary:", bakylau)
print("Durys kod C:", C)

# 2-esep

kabyl = kod.copy()
kabyl[5] = 1 - kabyl[5]

C_star = "".join(str(kabyl[i]) for i in range(1, n + 1))

print("\n2-esep")
print("Kabyl etilgen kod C*:", C_star)

sindrom = 0

for p in bakylau:
    kosyndy = 0
    for i in range(1, n + 1):
        if i & p:
            kosyndy ^= kabyl[i]
    if kosyndy == 1:
        sindrom += p

print("Sindrom:", format(sindrom, "04b"))
print("Sindrom (ondyq):", sindrom)

if 1 <= sindrom <= n:
    kabyl[sindrom] = 1 - kabyl[sindrom]

tuzetilgen = "".join(str(kabyl[i]) for i in range(1, n + 1))

print("Qate razryad:", sindrom)
print("Tuzetilgen kod:", tuzetilgen)
