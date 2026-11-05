"""Семинар 9. 11-нұсқа: біркелкі код және Фано шарты."""


def minimum_bits(alphabet_size: int) -> int:
    """2**k >= N шартын орындайтын ең кіші k мәні."""
    if alphabet_size < 1:
        raise ValueError("Алфавит өлшемі оң сан болуы тиіс")
    k = 0
    while 2 ** k < alphabet_size:
        k += 1
    return k


def is_prefix_free(codes: dict[str, str]) -> bool:
    words = list(codes.values())
    if len(set(words)) != len(words):
        return False
    return all(not second.startswith(first)
               for i, first in enumerate(words)
               for j, second in enumerate(words) if i != j)


def decode(message: str, codes: dict[str, str]) -> tuple[str, list[str]]:
    if not is_prefix_free(codes):
        raise ValueError("Фано шарты орындалмайды")
    reverse = {word: letter for letter, word in codes.items()}
    buffer = ""
    letters = []
    pieces = []
    for bit in message:
        if bit not in "01":
            raise ValueError("Хабар тек 0 және 1 сандарынан тұруы тиіс")
        buffer += bit
        if buffer in reverse:
            letters.append(reverse[buffer])
            pieces.append(buffer)
            buffer = ""
    if buffer:
        raise ValueError("Хабардың соңында толық емес кодтық сөз қалды")
    return "".join(letters), pieces


def main() -> None:
    print("9-СЕМИНАР | 11-НҰСҚА")
    print("1-есеп. Біркелкі екілік код")
    n = 135
    k = minimum_bits(n)
    print(f"Алфавит өлшемі: {n}")
    print(f"2^{k-1} = {2**(k-1)} < {n}")
    print(f"2^{k} = {2**k} >= {n}")
    print(f"Жауабы: {k} бит")

    print("\n2-есеп. Префикстік код және Фано шарты")
    codes = {"A": "0", "B": "10", "C": "110", "D": "111"}
    message = "1011100110"
    print("Кодтар:", codes)
    print("Фано шарты:", "орындалады" if is_prefix_free(codes) else "орындалмайды")
    result, pieces = decode(message, codes)
    print("Берілген хабар:", message)
    print("Бөлінуі:", " | ".join(pieces))
    print("Декодталған хабар:", result)


if __name__ == "__main__":
    main()
