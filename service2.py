class AnswerTwo():
    def get_combinations(denoms, total):
        output = { "count" : 0,
                "combinations" : []
                }
        names = list(denoms.keys())
        vals = [int(total/value) for value in denoms.values()]
        def helper(current_total, index, coins, potential_combination):
            if current_total == 0:
                output["count"] += 1
                output["combinations"].append(
                dict(zip(names, potential_combination))
                )
                return
        
            if current_total < 0 or index >= len(coins):
                return

            # print(potential_combination)
        
            # subtract current coin and keep index
            potential_combination[index] += 1
            helper(current_total - coins[index], index, coins, potential_combination)
            # backtrack
            potential_combination[index] -= 1
            helper(current_total, index + 1, coins, potential_combination)
        
        helper(total, 0, vals, [0]*len(vals))
        return output


    # den = {"quarters": 4,"dimes": 10,"nickels": 20,"pennies": 100}
    total = 150
    den = {"Coin": 1.5,"Arrowhead": 3,"Button": 150}
    get_combinations(den, total)