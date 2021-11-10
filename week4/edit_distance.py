
def Edit_Distance(x, y):  # transform
    xlen, ylen = len(x), len(y)
    insert_cost = 1
    delete_cost = 1
    # replace는 비교하는 문자가 다를 경우 1
    c = [[0]*(ylen+1) for _ in range(xlen+1)]
    for i in range(xlen, -1, -1):
        for j in range(ylen, -1, -1):
            if i == xlen and j == ylen:
                continue
            temp = int(1e9)
            if i < xlen:
                temp = min(temp, delete_cost+c[i+1][j])  # delete cost = 1
            if j < ylen:
                temp = min(temp, insert_cost + c[i][j+1])  # insert cost = 1
            if i < xlen and j < ylen:
                # replace cost = 0
                # 같지 않으면 교체 비용 발생
                temp = min(temp, c[i+1][j+1] + (x[i] != y[j]))
            c[i][j] = temp
    return c[0][0]


print(Edit_Distance("hello", "world"))
print(Edit_Distance('Hi', "world"))
print(Edit_Distance('beautiful', 'day'))
print(Edit_Distance('Idontknowand', 'dontunderstand'))
