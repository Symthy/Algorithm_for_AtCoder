def main():
    N = int(input())
    yes = 0
    no = 0
    for i in range(N):
        s = input()
        if s == "For":
            yes += 1
        if s == "Against":
            no += 1
    out = "No"
    if yes > no:
        out = "Yes"
    print(out)

main()
