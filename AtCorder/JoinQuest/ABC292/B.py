N, Q = map(int, input().split())

yellow_players = {}
red_players = {}

for _ in range(Q):
    event, player = input().split()
    if event == '1':
        if player in red_players:
            continue
        yellow_players[player] = yellow_players.get(player, 0) + 1
        if yellow_players[player] >= 2:
            red_players[player] = 1
    
    if event == '2':
        red_players[player] = 1
    if event == '3':
        if player in red_players:
            print('Yes')
        else:
            print('No')
    