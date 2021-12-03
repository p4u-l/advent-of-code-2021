with open("day03/input.txt", "r", encoding="utf-8") as f:
    diagnostic_report = f.read().splitlines()


def most_common_bit_at(bit_str: list[str], i: int) -> str:
    nums_at_i = [num[i] for num in bit_str]
    ones_at_i = nums_at_i.count("1")

    # Number of 1s greater than or equal to numbers of 0s.
    if ones_at_i >= (len(nums_at_i) - ones_at_i):
        return "1"
    return "0"


oxygen_ratings = diagnostic_report[:]
co2_ratings = diagnostic_report[:]
bit_length = len(diagnostic_report[0])

for i in range(bit_length):
    most_common_oxygen_bit = most_common_bit_at(oxygen_ratings, i)
    oxygen_ratings = [r for r in oxygen_ratings if r[i] == most_common_oxygen_bit]
    if len(oxygen_ratings) <= 1:
        break

for i in range(bit_length):
    most_common_co2_bit = most_common_bit_at(co2_ratings, i)
    co2_ratings = [r for r in co2_ratings if r[i] != most_common_co2_bit]
    if len(co2_ratings) <= 1:
        break

oxygen_rating = int(oxygen_ratings[0], 2)
co2_rating = int(co2_ratings[0], 2)
print(oxygen_rating * co2_rating)
