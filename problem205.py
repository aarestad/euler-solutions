import itertools

pp_probs = {}
cc_probs = {}

for pp_combo in itertools.product(range(1, 5), repeat=9):
    combo_sum = sum(pp_combo)

    if combo_sum in pp_probs:
        pp_probs[combo_sum] += 1
    else:
        pp_probs[combo_sum] = 1

for cc_combo in itertools.product(range(1, 7), repeat=6):
    combo_sum = sum(cc_combo)

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
