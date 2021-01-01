import sys

# Input
high_cost = [2, 9, 4, 5, 1, 6, 10]
num = len(high_cost)

# def main():
#   dp = [sys.maxsize] * num
#   dp[0] = 0
#   for i in range(1, num):
#     if i == 1:
#       dp[i] = abs(high_cost[i] - high_cost[i - 1])
#     else:
#       dp[i] = min(dp[i-1] + abs(high_cost[i] - high_cost[i - 1]),
#                   dp[i-2] + abs(high_cost[i] - high_cost[i - 2]))
#   print(dp)
#   return dp[num-1]


def main():
  dp = [sys.maxsize] * num
  dp[0] = 0
  for i in range(1, num):
    if i == 1:
      dp[i] = abs(high_cost[i] - high_cost[i - 1])
    else:
      dp[i] = min(dp[i-1] + abs(high_cost[i] - high_cost[i - 1]),
                  dp[i-2] + abs(high_cost[i] - high_cost[i - 2]))
  print(dp)
  return dp[num-1]

result = main()
print(result)
