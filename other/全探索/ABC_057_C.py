def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def f(a, b):
    a_len = len(str(a))
    b_len = len(str(b))
    return a_len if a_len >= b_len else b_len


def main():
    n = int(input())
    divisors = make_divisors(n)
    divisors_num = len(divisors)
    mid = divisors_num // 2
    print(f(divisors[mid], n//divisors[mid]))


main()
