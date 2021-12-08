def decode_mapping(patterns):
    patterns = [set(p) for p in patterns]
    one = next(p for p in patterns if len(p) == 2)
    patterns.remove(one)
    seven = next(p for p in patterns if len(p) == 3)
    patterns.remove(seven)
    four = next(p for p in patterns if len(p) == 4)
    patterns.remove(four)
    eight = next(p for p in patterns if len(p) == 7)
    patterns.remove(eight)
    nine = next(p for p in patterns if seven.issubset(p) and four.issubset(p) and len(p - seven - four) == 1)
    patterns.remove(nine)
    three = next(p for p in patterns if p.issubset(nine) and len(four - p) == 1 and not (four - p).issubset(one))
    patterns.remove(three)
    five = next(p for p in patterns if p.issubset(nine) and len(four - p) == 1 and (four - p).issubset(one))
    patterns.remove(five)
    two = next(p for p in patterns if len(p) == 5)
    patterns.remove(two)
    zero = next(p for p in patterns if not (eight - p).issubset(one))
    patterns.remove(zero)
    six = patterns.pop()

    def to_string(digit_set):
        return ''.join(sorted(digit_set))

    return {
        to_string(zero): '0',
        to_string(one): '1',
        to_string(two): '2',
        to_string(three): '3',
        to_string(four): '4',
        to_string(five): '5',
        to_string(six): '6',
        to_string(seven): '7',
        to_string(eight): '8',
        to_string(nine): '9'
    }


if __name__ == "__main__":
    with open("input_files/input_day_8.txt", "r") as f:
        lines = f.read().splitlines()

    answer_a = 0
    for line in lines:
        patterns, value = line.split(" | ")
        value_digits = value.split()
        answer_a += sum(len(d) in {2, 3, 4, 7} for d in value_digits)
    print(answer_a)

    answer_b = 0
    for line in lines:
        patterns, value = line.split(" | ")
        mapping = decode_mapping(patterns.split())
        value_digits = value.split()
        value = int("".join(mapping["".join(sorted(digit))] for digit in value_digits))
        answer_b += value
    print(answer_b)