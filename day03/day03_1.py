with open("day03/input.txt", "r", encoding="utf-8") as f:
    diagnostic_report = f.read().splitlines()


def most_common_bit_at(bit_str: list[str], i: int) -> str:
    nums_at_i = [num[i] for num in bit_str]
    ones_at_i = nums_at_i.count("1")

    # Number of 1s greater than or equal to numbers of 0s.
    if ones_at_i >= (len(nums_at_i) - ones_at_i):
        return "1"
    return "0"


gamma_rate_str = ""
bit_length = len(diagnostic_report[0])

for i in range(bit_length):
    most_common_bit = most_common_bit_at(diagnostic_report, i)
    gamma_rate_str += most_common_bit

gamma_rate = int(gamma_rate_str, 2)
# epsilon rate is the gamma rate with inverted bits,
# formed by bitwise XOR with 1.
epsilon_rate = gamma_rate ^ int("1" * bit_length, 2)
print(gamma_rate * epsilon_rate)
