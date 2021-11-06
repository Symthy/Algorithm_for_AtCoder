import bisect
import heapq


def main():
    h, w, n = map(int, input().split())
    index_list = []
    gyo_set = []
    retu_set = []
    heapq.heapify(gyo_set)
    heapq.heapify(retu_set)
    for i in range(n):
        gyo, retu = map(int, input().split())
        index_list.append((gyo, retu))
        if not gyo in gyo_set:
            heapq.heappush(gyo_set, gyo)
        if not retu in retu_set:
            heapq.heappush(retu_set, retu)

    gyo_set = [heapq.heappop(gyo_set) for _ in range(len(gyo_set))]
    retu_set = [heapq.heappop(retu_set) for _ in range(len(retu_set))]

    for tup in index_list:
        gyo_index = bisect.bisect(gyo_set, tup[0])
        retu_index = bisect.bisect(retu_set, tup[1])
        print(gyo_index, retu_index)


main()
