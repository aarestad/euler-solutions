import itertools

#   0
#    \
#     1   2
#    / \ /
#   3   4
#  /\  /
# 5 6-7--8
#    \
#     9


def magic_5_gon(nums):
    line1 = [nums[0], nums[1], nums[4]]
    line2 = [nums[2], nums[4], nums[7]]
    line3 = [nums[8], nums[7], nums[6]]
    line4 = [nums[9], nums[6], nums[3]]
    line5 = [nums[5], nums[3], nums[1]]

    line1_sum = sum(line1)

    if (
        line1_sum == sum(line2)
        and line1_sum == sum(line3)
        and line1_sum == sum(line4)
        and line1_sum == sum(line5)
    ):

        beginning_line = sorted(
            [line1, line2, line3, line4, line5], lambda x, y: cmp(x[0], y[0])
        )[0]

        if beginning_line == line1:
            return "".join(
                [
                    "".join([str(d) for d in line])
                    for line in [line1, line2, line3, line4, line5]
                ]
            )
        if beginning_line == line2:
            return "".join(
                [
                    "".join([str(d) for d in line])
                    for line in [line2, line3, line4, line5, line1]
                ]
            )
        if beginning_line == line3:
            return "".join(
                [
                    "".join([str(d) for d in line])
                    for line in [line3, line4, line5, line1, line2]
                ]
            )
        if beginning_line == line4:
            return "".join(
                [
                    "".join([str(d) for d in line])
                    for line in [line4, line5, line1, line2, line3]
                ]
            )
        if beginning_line == line5:
            return "".join(
                [
                    "".join([str(d) for d in line])
                    for line in [line5, line1, line2, line3, line4]
                ]
            )

    return None


for p in itertools.permutations(list(range(1, 11))):
    possible_5gon = magic_5_gon(p)
    if (
        possible_5gon is not None
        and len(possible_5gon) == 16
        and possible_5gon[0:2] == "65"
    ):  # this last "and" clause comes from eyeballing all the possible 16-length reprs
        print(possible_5gon)  # only one answer, printed 5 times

# the answer:
#    6
#     \
#      5    10
#    /  \  /
#   2    3
#  / \  /
# 7  4-1--9
#     \
#      8
# or "6531031914842725"
