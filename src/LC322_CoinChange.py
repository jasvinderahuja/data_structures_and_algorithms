## Leetcode 322. Coin Change
## I know there is a better more succinct way, but this is what I can come up with..
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int: 
        # bottom up, start from lowest denomination coin and go to mount
        # on the way figure out every value with least coins
        # before that, set the default values in list to 'inf' so that the number of coins can be less than it
        # ith number in the list is the least number of coins that make up amount
        coins = sorted(coins)
        if amount == 0:
            return 0
        elif coins[0] > amount:
            return -1
        elif amount in coins:
            return 1
        else:
            coins = [coin for coin in coins if coin < amount] ## this saves me from memory limit!!
            pseudo_inf = amount+1
            lst = [pseudo_inf]*(amount+coins[-1]) ## I ought to be able to make this shorter!
            lst[0] =0

            for i in range(1,pseudo_inf):
                
                for coin in coins:
                    lst[i] = min(lst[i], 1+lst[i-coin])
                    ## this magic statement is copied
                    ## we take minimum of existing value versus target(~i) and subtract coin denomination!! +1 (for the coin)
                if i == amount and lst[i] < pseudo_inf:
                    return lst[i]

        return -1
