# Семинар 9. 8-нұсқа
# 1-есеп: Шеннон–Фано коды
# 2-есеп: Префикстік кодты декодтау

from collections import Counter


def shannon_fano(items, prefix="", codes=None):
    """Ықтималдықтары кему ретімен орналасқан символдарды екі топқа бөлу."""
    if codes is None:
        codes = {}
    if len(items) == 1:
        codes[items[0][0]] = prefix or "0"
        return codes

    total = sum(count for _, count in items)
    left_sum = 0
    best_split = 1
    best_diff = float("inf")
    for split in range(1, len(items)):
        left_sum += items[split - 1][1]
        diff = abs(total - 2 * left_sum)
        if diff < best_diff:
            best_diff = diff
            best_split = split

    shannon_fano(items[:best_split], prefix + "0", codes)
    shannon_fano(items[best_split:], prefix + "1", codes)
    return codes


def is_prefix_free(codes):
    values = list(codes.values())
    return all(not b.startswith(a)
               for i, a in enumerate(values)
               for j, b in enumerate(values) if i != j)


print("=== 1-ЕСЕП: ШЕННОН–ФАНО КОДЫ ===")
message1 = "123"
counts = Counter(message1)
items = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
codes1 = shannon_fano(items)

for symbol in sorted(counts):
    probability = counts[symbol] / len(message1)
    print(f"Символ: {symbol} | p = {probability:.3f} | код = {codes1[symbol]}")

encoded = "".join(codes1[ch] for ch in message1)
print("Бастапқы хабар:", message1)
print("Кодталған хабар:", encoded)
print("Префикстік шарт орындала ма?", "Иә" if is_prefix_free(codes1) else "Жоқ")

print("\n=== 2-ЕСЕП: ДЕКОДТАУ ===")
codes2 = {"A": "0", "B": "10", "C": "110", "D": "111"}
bitstream = "1011011110"
reverse_codes = {value: key for key, value in codes2.items()}
buffer = ""
letters = []
chunks = []

for bit in bitstream:
    buffer += bit
    if buffer in reverse_codes:
        chunks.append(buffer)
        letters.append(reverse_codes[buffer])
        buffer = ""

if buffer:
    raise ValueError(f"Толық декодталмаған биттер қалды: {buffer}")

print("Берілген кодтар:", codes2)
print("Кодталған хабар:", bitstream)
print("Бөлінуі:", " | ".join(chunks))
print("Декодталған хабар:", "".join(letters))
print("Префикстік шарт орындала ма?", "Иә" if is_prefix_free(codes2) else "Жоқ")
