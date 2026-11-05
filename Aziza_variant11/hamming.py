"""Seminar 8: universal Hamming code encoder and single-bit error corrector."""

def parity_count(data_length):
    r = 0
    while 2 ** r < data_length + r + 1:
        r += 1
    return r


def encode(data):
    if not data or any(bit not in '01' for bit in data):
        raise ValueError('Ақпараттық комбинация тек 0 және 1 сандарынан тұруы керек.')
    r = parity_count(len(data))
    n = len(data) + r
    bits = [0] * (n + 1)
    iterator = iter(map(int, data))
    for pos in range(1, n + 1):
        if pos & (pos - 1):
            bits[pos] = next(iterator)
    print(f'Ақпараттық биттер: {len(data)}, бақылау биттері: {r}, жалпы ұзындық: {n}')
    print('Бақылау позициялары:', [2 ** i for i in range(r)])
    print('Бастапқы макет:', ''.join('_' if i & (i - 1) == 0 else str(bits[i]) for i in range(1, n + 1)))
    for i in range(r):
        p = 2 ** i
        positions = [j for j in range(1, n + 1) if j & p and j != p]
        values = [bits[j] for j in positions]
        bits[p] = sum(values) % 2
        print(f'a{p} = ' + ' ⊕ '.join(f'a{j}' for j in positions) + ' = ' + ' ⊕ '.join(map(str, values)) + f' = {bits[p]}')
    return ''.join(map(str, bits[1:]))


def flip_bit(code, position):
    if not 1 <= position <= len(code):
        raise ValueError('Қате позициясы код ұзындығынан аспауы керек.')
    chars = list(code)
    chars[position - 1] = '1' if chars[position - 1] == '0' else '0'
    return ''.join(chars)


def decode(received):
    if not received or any(bit not in '01' for bit in received):
        raise ValueError('Код тек 0 және 1 сандарынан тұруы керек.')
    bits = [0] + list(map(int, received))
    syndrome = 0
    checks = []
    p = 1
    while p <= len(received):
        positions = [j for j in range(1, len(bits)) if j & p]
        values = [bits[j] for j in positions]
        check = sum(values) % 2
        checks.append(check)
        syndrome += p * check
        print(f'E{p} = ' + ' ⊕ '.join(f'a{j}' for j in positions) + ' = ' + ' ⊕ '.join(map(str, values)) + f' = {check}')
        p *= 2
    print('Синдром:', ''.join(map(str, reversed(checks))), '(екілік) =', syndrome, '(ондық)')
    if syndrome == 0:
        print('Қате табылмады.')
        return received
    if syndrome > len(received):
        print('Синдром код ұзындығынан тыс: бірнеше қате болуы мүмкін.')
        return received
    corrected = flip_bit(received, syndrome)
    print('Қате позициясы:', syndrome)
    print('Түзетілген код:', corrected)
    return corrected


def main():
    print('8-СЕМИНАР | ХЭММИНГ КОДЫ | 11-НҰСҚА')
    data = input('Ақпараттық комбинация [11001010]: ').strip() or '11001010'
    code = encode(data)
    print('Дұрыс C:', code)
    default_error = 3
    error_text = input('Қате енгізілетін позиция [3], қатесіз тексеру үшін 0: ').strip()
    error_position = int(error_text) if error_text else default_error
    received = flip_bit(code, error_position) if error_position else code
    print('Қабылданған C*:', received)
    corrected = decode(received)
    print('Тексеру нәтижесі:', 'СӘТТІ' if corrected == code else 'СӘТСІЗ')


if __name__ == '__main__':
    main()
