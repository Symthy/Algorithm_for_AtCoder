

def main():
    s = input()
    result = True
    while len(s) > 0:
        if s.endswith('dreamer'):
            s = s[:-7]
        elif s.endswith('dream'):
            s = s[:-5]
        elif s.endswith('eraser'):
            s = s[:-6]
        elif s.endswith('erase'):
            s = s[:-5]
        else:
            result = False
            break
    print('YES' if result else 'NO')


main()
