import sys

# Input
high_cost = [2, 9, 4, 5, 1, 6, 10]
num = len(high_cost)
dp = [sys.maxsize] * num

def rec(i):
  if i == 0:
    return 0

  ret = rec(i - 1) + abs(high_cost[i] - high_cost[i - 1])

  if i > 1:
    comp_val = rec(i - 2) + abs(high_cost[i] - high_cost[i - 2])
    ret = comp_val if ret > comp_val else ret

  dp[i] = ret
  return ret


def main():
  dp[0] = 0
  result = rec(num - 1)
  print(dp)
  print(result)


main()
