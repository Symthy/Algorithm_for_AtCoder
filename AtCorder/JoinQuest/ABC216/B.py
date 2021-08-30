def main():
    N = int(input())
    p_map = {}
    is_same = False
    for i in range(N):
        s_t = input()
        p_map[s_t] = ''
    if len(p_map) == N:
        print('No')
    else:
        print('Yes')


main()
