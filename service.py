class AnswerOne():
    def get_combinations(total):
        output = { "count" : 0,
                "combinations" : []
                }

        def helper(current_total, index, coins, potential_combination):
            if current_total == 0:
                output["count"] += 1
                output["combinations"].append({
                "quarters" : potential_combination[0],
                "dimes" : potential_combination[1],
                "nickels" : potential_combination[2],
                "pennies" : potential_combination[3]
                })
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
        
        helper(total, 0, [25, 10, 5, 1], [0, 0, 0, 0])
        return output
    total = 100
    get_combinations(total)
