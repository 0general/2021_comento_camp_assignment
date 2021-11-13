import time


def recursive_LCS(x, y, i, j):
    xlen = len(x)
    ylen = len(y)
    if i == 0 and j == 0:
        return int(x[i] == y[j])
    elif i == 0:
        return max(recursive_LCS(x, y, i, j-1), int(x[i] == y[j]))
    elif j == 0:
        return max(recursive_LCS(x, y, i-1, j), int(x[i] == y[j]))
    else:
        if x[i] == y[j]:
            return recursive_LCS(x, y, i-1, j-1) + 1
        else:
            return max(recursive_LCS(x, y, i-1, j), recursive_LCS(x, y, i, j-1))


def memo_LCS(x, y, c, i, j):  # top-down
    xlen = len(x)
    ylen = len(y)

    if c[i][j] == None:
        if i == 0 and j == 0:
            c[i][j] = int(x[i] == y[j])
            return c[i][j]
        elif i == 0:
            c[i][j] = max(memo_LCS(x, y, c, i, j-1), int(x[i] == y[j]))
            return c[i][j]
        elif j == 0:
            c[i][j] = max(memo_LCS(x, y, c, i-1, j), int(x[i] == y[j]))
            return c[i][j]
        else:
            if x[i] == y[j]:
                c[i][j] = memo_LCS(x, y, c, i-1, j-1) + 1
            else:
                c[i][j] = max(memo_LCS(x, y, c, i-1, j),
                              memo_LCS(x, y, c, i, j-1))

    return c[i][j]


def LCS(x, y):  # bottom-up using DP table
    xlen = len(x)
    ylen = len(y)

    c = [[0]*ylen for _ in range(xlen)]
    for i in range(xlen):
        for j in range(ylen):
            if i == 0 and j == 0:
                c[i][j] += (x[i] == y[j])  # default value = 0
            elif i == 0:
                c[i][j] = max(c[i][j-1], int(x[i] == y[j]))
            elif j == 0:
                c[i][j] = max(c[i-1][j], int(x[i] == y[j]))
            else:
                if x[i] == y[j]:
                    c[i][j] = c[i-1][j-1] + 1
                else:
                    c[i][j] = max(c[i-1][j], c[i][j-1])
    return c[xlen-1][ylen-1]


a = "BDCABA"
b = "BCBDAB"
n = len(a)-1
m = len(b)-1
ans1 = recursive_LCS(a, b, n, m)
c = [[None]*(len(b)) for _ in range(len(a))]
ans2 = memo_LCS(a, b, c, n, m)
ans3 = LCS(a, b)
print(ans1, ans2, ans3)

a = "IKNOWABOUTTHIS"
b = "IGOTTHISTOO"
n = len(a)-1
m = len(b)-1
ans1 = recursive_LCS(a, b, n, m)
c = [[None]*(len(b)) for _ in range(len(a))]
ans2 = memo_LCS(a, b, c, n, m)
ans3 = LCS(a, b)
print(ans1, ans2, ans3)

a = "AAAAAAAAABAAA"
b = "AAAACAAAAAAAA"
n = len(a)-1
m = len(b)-1
ans1 = recursive_LCS(a, b, n, m)
c = [[None]*(len(b)) for _ in range(len(a))]
ans2 = memo_LCS(a, b, c, n, m)
ans3 = LCS(a, b)
print(ans1, ans2, ans3)
