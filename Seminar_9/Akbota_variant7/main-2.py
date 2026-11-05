"""9-семинар: біркелкі екілік код және Фано шарты (7-нұсқа)."""


def min_bits(alphabet_size):
    """2**k >= N шартын қанағаттандыратын ең кіші k мәні."""
    if alphabet_size <= 0:
        raise ValueError("Алфавиттегі символ саны оң болуы керек")
    k = 0
    while 2 ** k < alphabet_size:
        k += 1
    return k


def check_fano(codes):
    """Бір код басқа кодтың басы емес екенін тексереді."""
    words = list(codes.values())
    if not words or any(not w or set(w) - {"0", "1"} for w in words):
        return False
    if len(words) != len(set(words)):
        return False
    for i, first in enumerate(words):
        for j, second in enumerate(words):
            if i != j and second.startswith(first):
                return False
    return True


def decode_message(message, codes):
    """Хабарды солдан оңға қарай декодтайды."""
    if not check_fano(codes):
        raise ValueError("Фано шарты орындалмайды")
    if set(message) - {"0", "1"}:
        raise ValueError("Хабар тек 0 және 1 цифрларынан тұруы керек")

    reverse = {code: symbol for symbol, code in codes.items()}
    buffer = ""
    parts = []
    result = []
    for bit in message:
        buffer += bit
        if buffer in reverse:
            parts.append(buffer)
            result.append(reverse[buffer])
            buffer = ""
    if buffer:
        raise ValueError(f"Хабардың соңындағы {buffer!r} тізбегі толық код емес")
    return parts, "".join(result)


def main():
    print("=== 9-СЕМИНАР, 7-НҰСҚА ===")
    n = 121
    codes = {"A": "0", "B": "10", "C": "110", "D": "111"}
    message = "111011010"

    print("\n1-ЕСЕП. БІРКЕЛКІ КОДТАУ")
    k = min_bits(n)
    print(f"Алфавиттегі символ саны: N = {n}")
    if k > 0:
        print(f"2^{k - 1} = {2 ** (k - 1)} < {n}")
    print(f"2^{k} = {2 ** k} >= {n}")
    print(f"Жауап: {k} бит")

    print("\n2-ЕСЕП. ФАНО ШАРТЫ")
    print("Кодтар:", ", ".join(f"{s}={c}" for s, c in codes.items()))
    print("Хабар:", message)
    is_prefix = check_fano(codes)
    print("Фано шарты:", "орындалады" if is_prefix else "орындалмайды")
    parts, decoded = decode_message(message, codes)
    print("Бөлінуі:", " | ".join(parts))
    print("Символдары:", " | ".join({v: k for k, v in codes.items()}[p] for p in parts))
    print("Жауап:", decoded)


if __name__ == "__main__":
    main()
