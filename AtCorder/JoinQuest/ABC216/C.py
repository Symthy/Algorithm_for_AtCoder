

def main():
    N = int(input())
    reverse_ans = ''
    while N != 0:
        if N % 2 == 0:
            reverse_ans += 'B'
            N //= 2
        else:
            reverse_ans += 'A'
            N -= 1
    ans = reverse_ans[::-1]
    print(ans)


main()
