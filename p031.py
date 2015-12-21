def change_combos(coins, change):
    if change == 0:
        return 1
    if change < 0:
        return 0
    if change >=1 and len(coins) <= 0:
        return 0

    # try solving with one less coin and try solving with current coins
    return change_combos(coins[:-1], change) + change_combos(coins, change - coins[-1])

def solve_p030():
    coins = [1,2,5,10,20,50,100,200]
    return count_combos(coins, 200)

if __name__ == '__main__':
    print(solve_p030())
