def mine_location(field):
    for i in range(len(field)):
        for u in range(len(field[i])):
            if field[i][u] == 1:
                return [i, u]


print(mine_location([[1, 0, 0], [0, 0, 0], [0, 0, 0]]))
print(mine_location([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(mine_location([[0, 0, 0], [0, 0, 0], [0, 1, 0]]))
