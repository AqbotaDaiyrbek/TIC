"""Seminar 8: Hamming code with even parity, positions counted from left."""
import argparse

# Information words and intentionally corrupted positions from the seminar PDF.
VARIANTS = {
    1: ('0100', 3), 2: ('0111', 5), 3: ('1001', 6),
    4: ('1010', 7), 5: ('1100', 3), 6: ('0011', 5),
    7: ('1110', 6), 8: ('1000', 7), 9: ('0110', 3),
    10: ('1011', 5), 11: ('11001010', 3), 12: ('10110101', 5),
    13: ('01101011', 6), 14: ('10011100', 7),
    15: ('11100101', 9), 16: ('01011010', 10),
    17: ('10101101', 11), 18: ('00110110', 12),
    19: ('11010011', 6), 20: ('01110100', 9),
}


def check_bits_count(info_length):
    r = 0
    while (1 << r) < info_length + r + 1:
        r += 1
    return r


def parity_positions(length):
    return [1 << i for i in range(length.bit_length()) if (1 << i) <= length]


def validate_bits(bits):
    if not bits or any(c not in '01' for c in bits):
        raise ValueError('Ақпарат тек 0 мен 1 таңбаларынан тұруы тиіс.')


def encode(data):
    validate_bits(data)
    r = check_bits_count(len(data))
    n = len(data) + r
    controls = parity_positions(n)
    code = ['0'] * n
    iterator = iter(data)
    for position in range(1, n + 1):
        if position not in controls:
            code[position - 1] = next(iterator)
    equations = []
    for p in controls:
        positions = [i for i in range(1, n + 1) if i & p and i != p]
        bits = [int(code[i - 1]) for i in positions]
        value = sum(bits) % 2
        code[p - 1] = str(value)
        equations.append((p, positions, bits, value))
    return ''.join(code), equations


def syndrome(received):
    validate_bits(received)
    checks = []
    for p in parity_positions(len(received)):
        positions = [i for i in range(1, len(received) + 1) if i & p]
        result = sum(int(received[i - 1]) for i in positions) % 2
        checks.append((p, positions, result))
    error_position = sum(p for p, _, result in checks if result)
    return error_position, checks


def decode(received):
    position, checks = syndrome(received)
    corrected = list(received)
    if 1 <= position <= len(corrected):
        corrected[position - 1] = '1' if corrected[position - 1] == '0' else '0'
    fixed = ''.join(corrected)
    data = ''.join(ch for i, ch in enumerate(fixed, 1)
                   if i not in parity_positions(len(fixed)))
    return position, fixed, data, checks


def show(data, broken_position):
    code, equations = encode(data)
    n = len(code)
    if not 1 <= broken_position <= n:
        raise ValueError(f'Қате позициясы 1 мен {n} аралығында болуы тиіс.')
    r = check_bits_count(len(data))
    print('=== 8-СЕМИНАР: ХЭММИНГ КОДЫ ===')
    print(f'Ақпараттық сөз: {data}')
    print(f'nᵢ={len(data)}, nₖ={r}, n={n}')
    print(f'Бақылау позициялары: {parity_positions(n)}')
    print('\n1-ЕСЕП: КОДТАУ')
    for p, positions, bits, value in equations:
        print(f'a{p} = ' + ' XOR '.join(map(str, bits)) + f' = {value} '
              + f'(позициялар: {positions})')
    print('Дұрыс код C:', code)
    received = list(code)
    received[broken_position - 1] = '1' if received[broken_position - 1] == '0' else '0'
    received = ''.join(received)
    print('\n2-ЕСЕП: ҚАТЕНІ ТАБУ ЖӘНЕ ТҮЗЕТУ')
    print(f'Бұрмаланған разряд: {broken_position}')
    print('Қабылданған код C*:', received)
    error, corrected, decoded, checks = decode(received)
    for index, (p, positions, result) in enumerate(checks, 1):
        print(f'E{index} = {result} (позициялар: {positions})')
    print(f'Синдром S = {error:0{r}b}₂ = {error}₁₀')
    print('Табылған қате разряд:', error)
    print('Түзетілген код:', corrected)
    print('Қалпына келген ақпарат:', decoded)
    print('Тексеру:', 'СӘТТІ' if corrected == code and decoded == data else 'ҚАТЕ')


def main():
    parser = argparse.ArgumentParser(description='Хэмминг коды: 8-семинар, барлық нұсқаға ортақ')
    parser.add_argument('--variant', type=int, default=7, help='Нұсқа нөмірі (1-20), әдепкісі 7')
    parser.add_argument('--data', help='Өз ақпараттық сөзіңіз, мысалы 1110')
    parser.add_argument('--error', type=int, help='Қате разрядтың нөмірі (солдан бастап)')
    args = parser.parse_args()
    if args.variant not in VARIANTS:
        parser.error('Нұсқа 1-20 аралығында болуы керек.')
    data, error = VARIANTS[args.variant]
    show(args.data if args.data is not None else data,
         args.error if args.error is not None else error)


if __name__ == '__main__':
    main()
