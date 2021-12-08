with open("day08/input.txt", "r", encoding="utf-8") as f:
    puzzle_input = f.read().splitlines()


def determine_mapping(signals):
    # dict with all signals as values, length of them as keys.
    # All signals have either length 2 and 7.
    signals_by_len = dict()
    for n in range(2, 8):
        signals_by_len[n] = [s for s in signals if len(s) == n]

    mapping = dict()
    mapping[signals_by_len[3][0]] = 7  # only option with len 3: 7
    mapping[signals_by_len[7][0]] = 8  # only option with len 7: 8
    # The signals for 1 and 4 are stored in their own variables
    # because they are necessary in the next step to determine
    # the remaining signals.
    signal_for_1 = signals_by_len[2][0]  
    signal_for_4 = signals_by_len[4][0]  
    mapping[signal_for_1] = 1  # only option with len 2: 1
    mapping[signal_for_4] = 4  # only option with len 4: 4
    
    # The following described rules for subsets and intersections
    # become clear when looking at the rendering of the digits in the
    # description text for part 1: https://adventofcode.com/2021/day/8

    for signal in signals_by_len[5]:
        # only options with len 5: 2, 3 and 5

        # If the signal for 1 is a subset of a signal with length 5,
        # this signal must be the signal for 3.
        if signal_for_1.issubset(signal):
            mapping[signal] = 3
        # Otherwise, if the size of the intersection of a signal with
        # the length 5 with the signal for 4, equals two,
        # this signal must be the signal for 2.
        elif len(signal.intersection(signal_for_4)) == 2:
            mapping[signal] = 2
        # Otherwise, it must be the signal for 5.
        else:
            mapping[signal] = 5

    for signal in signals_by_len[6]:
        # only options with len 6: 0, 6 and 9

        # If the signal for 1 is not a subset of a signal with length 6,
        # this signal must be the signal for 6.
        if not signal_for_1.issubset(signal):
            mapping[signal] = 6
        # Otherwise, if the signal for 4 is a subset of a signal with
        # length 6, this signal must be the signal for 9.
        elif signal_for_4.issubset(signal):
            mapping[signal] = 9
        # Otherwise, it must be the signal for 0.
        else:
            mapping[signal] = 0

    return mapping


def solve(inp):
    output_value_sum = 0

    for line in inp:
        signals_str, output_signals_str = line.split(" | ")
        # Using frozensets instead of sets. Frozensets are immutable,
        # which is why they can be used as keys in dictionaries.
        signals = list(map(frozenset, signals_str.split(" ")))
        output_signals = list(map(frozenset, output_signals_str.split(" ")))
        mapping = determine_mapping(signals)
        decoded_outputs = (mapping[pattern] for pattern in output_signals)
        # Joining multiple digits into one output_value
        output_value = int("".join(map(str, decoded_outputs)))
        output_value_sum += output_value

    return output_value_sum


print(solve(puzzle_input))
