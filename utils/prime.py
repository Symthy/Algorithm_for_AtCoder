"""
素数判定
"""


def is_prime(n):
    prime_list = [2]  # 素数リスト
    for i in range(3, n+1):
        for j in prime_list:
            if i % j == 0:
                return False
    return True
