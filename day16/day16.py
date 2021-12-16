from math import prod

operations = {
    0: sum,
    1: prod,
    2: min,
    3: max,
    5: (lambda a: int(a[0] > a[1])),
    6: (lambda a: int(a[0] < a[1])),
    7: (lambda a: int(a[0] == a[1]))
}


def hex_to_bit_list(hex_str: str) -> list[int]:
    bit_list = []
    for char in hex_str:
        bit_list.extend(int(i) for i in str(bin(int(char, 16))[2:].zfill(4)))
    return bit_list


def to_literal(bits: list[int]) -> int:
    return int("".join(map(str, bits)), 2)


def read_bits(bits: list, n: int, return_literal: bool = False) -> list:
    # removes first n bits from bit list and returns them
    # converts removed bits to literal if literal = True.
    bit_chunk = [bits.pop(0) for _ in range(n)]
    if return_literal:
        return to_literal(bit_chunk)
    return bit_chunk


def parse(bits: list[int], version_sum: int = 0) -> tuple[int, int]:
    # Read packet header
    version = read_bits(bits, 3, return_literal=True)
    version_sum += version
    type_id = read_bits(bits, 3, return_literal=True)

    if type_id == 4:
        # packet is a literal value
        value_bits = []
        while True:
            chunk = read_bits(bits, 5)
            value_bits.extend(chunk[1:])
            if chunk[0] == 0:
                break
        value = to_literal(value_bits)
    else:
        # packet is a operation
        length_type_id = read_bits(bits, 1, return_literal=True)
        subpacket_values = []
        if length_type_id == 0:
            # parse subpackets from next x bits
            subpacket_total_len = read_bits(bits, 15, return_literal=True)
            bit_length_before = len(bits)
            while len(bits) > (bit_length_before - subpacket_total_len):
                subpacket_result, version_sum = parse(bits, version_sum)
                subpacket_values.append(subpacket_result)
        else:
            # parse x subpackets
            subpacket_number = read_bits(bits, 11, return_literal=True)
            for _ in range(subpacket_number):
                subpacket_result, version_sum = parse(bits, version_sum)
                subpacket_values.append(subpacket_result)
        
        value = operations[type_id](subpacket_values)
    
    return value, version_sum
        

def main():
    with open("day16/input.txt", "r", encoding="utf-8") as f:
        puzzle_input = f.read()

    bits = hex_to_bit_list(puzzle_input)
    result, version_sum = parse(bits)
    print("Part 1:", version_sum)
    print("Part 2:", result)

    
if __name__ == "__main__":
    main()
