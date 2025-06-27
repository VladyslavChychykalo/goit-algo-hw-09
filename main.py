import time


def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    """
    Жадібний алгоритм: вибирає найбільші можливі монети
    """
    start_time = time.time()

    result = {}
    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count

    elapsed_time = time.time() - start_time
    print(f"[Greedy] Час виконання: {elapsed_time:.8f} секунд")
    return result


def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    """
    Динамічне програмування: знаходить мінімальну кількість монет
    """
    start_time = time.time()

    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    prev = [None] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                prev[i] = coin

    if dp[amount] == float('inf'):
        return {}

    result = {}
    while amount > 0:
        coin = prev[amount]
        if coin is None:
            break
        result[coin] = result.get(coin, 0) + 1
        amount -= coin

    elapsed_time = time.time() - start_time
    print(f"[DP] Час виконання: {elapsed_time:.8f} секунд")
    return result


sum_to_change = 113

greedy_result = find_coins_greedy(sum_to_change)
print("Greedy result:", greedy_result)

dp_result = find_min_coins(sum_to_change)
print("DP result:", dp_result)
