# // int findCombinationsCount(int amount, int coins[]) {
#     return findCombinationsCount(amount, coins, 0);
# }
#
# int findCombinationsCount(int amount, int coins[], int checkFromIndex) {
#     if (amount == 0)
#         return 1;
#     else if (amount < 0 || coins.length == checkFromIndex)
#         return 0;
#     else {
#         int withFirstCoin = findCombinationsCount(amount-coins[checkFromIndex], coins, checkFromIndex);
#         int withoutFirstCoin = findCombinationsCount(amount, coins, checkFromIndex+1);
#         return withFirstCoin + withoutFirstCoin;
#     }
# }

coins = [1, 2, 5, 10, 20, 50, 100, 200]

def find_combination_count(amount, check_from_index):
	if amount == 0: return 1
	if amount < 0 or check_from_index == len(coins): return 0

	with_first_coin = find_combination_count(amount - coins[check_from_index], check_from_index)
	without_first_coin = find_combination_count(amount, check_from_index+1)
	return with_first_coin + without_first_coin

print find_combination_count(200, 0)
