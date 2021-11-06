def main():
    N = int(input())
    array = list(map(int, input().split()))
    sorted_array = sorted(array)
    print(array.index(sorted_array[N-2]) + 1)


main()
