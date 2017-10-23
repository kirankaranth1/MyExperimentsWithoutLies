test = [[1,2,3],[4,5,6],[7,8,9]]
# 1 2 3
# 4 5 6
# 7 8 9

i=0
j=0
k=0
move_upward = True

while k < 3*3:
    print(test[i][j])

    if move_upward:
        if (i > 0 and j < 2):
            i += -1
            j += 1
        elif i == 0 and j< 3-1:
            j += 1
            move_upward = not move_upward
        elif j == 2:
            i += 1
            move_upward = not move_upward

    else:
        if (j > 0 and i < 2):
            j += -1
            i += 1
        elif j == 0 and i < 3 - 1:
            i += 1
            move_upward = not move_upward
        elif i == 2:
            j += 1
            move_upward = not move_upward
    k += 1
