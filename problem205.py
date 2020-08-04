# Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
# Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

# Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.

# What is the probability that Pyramidal Pete beats Cubic Colin?
# Give your answer rounded to seven decimal places in the form 0.abcdefg
import itertools

pp_probs = { }
cc_probs = { }

for d1 in range(1, 5):
    for d2 in range(1, 5):
        for d3 in range(1, 5):
            for d4 in range(1, 5):
                for d5 in range(1, 5):
                    for d6 in range(1, 5):
                        for d7 in range(1, 5):
                            for d8 in range(1, 5):
                                for d9 in range(1, 5):
                                    combo_sum = d1+d2+d3+d4+d5+d6+d7+d8+d9

                                    if combo_sum in pp_probs:
                                        pp_probs[combo_sum] += 1
                                    else:
                                        pp_probs[combo_sum] = 1

for d1 in range(1, 7):
    for d2 in range(1, 7):
        for d3 in range(1, 7):
            for d4 in range(1, 7):
                for d5 in range(1, 7):
                    for d6 in range(1, 7):
                        combo_sum = d1+d2+d3+d4+d5+d6

                        if combo_sum in cc_probs:
                            cc_probs[combo_sum] += 1
                        else:
                            cc_probs[combo_sum] = 1

print(pp_probs)
print(cc_probs)

total_pp_options = sum(pp_probs.values())
total_cc_options = sum(cc_probs.values())
print(total_pp_options)
print(total_cc_options)

denominator = total_pp_options * total_cc_options
print(denominator)

total_pp_ways_to_win = 0

for cc_sum, cc_sum_combos in cc_probs.items():
    pp_winners = (pp_sum for pp_sum in pp_probs if pp_sum > cc_sum)

    for winner in pp_winners:
        total_pp_ways_to_win += cc_sum_combos * pp_probs[winner]

print(total_pp_ways_to_win)

print(total_pp_ways_to_win / denominator)
