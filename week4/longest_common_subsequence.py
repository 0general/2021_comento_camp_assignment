
def recursive_LCS(x, y, i, j):
    xlen = len(x)
    ylen = len(y)

    if i == 0 and j == 0:
        return int(x[i] == y[j])
    elif i == 0:
        return recursive_LCS(x, y, i, j-1) + (x[i] == y[j])
    elif j == 0:
        return recursive_LCS(x, y, i-1, j) + (x[i] == y[j])
    if x[i] == y[j]:
        return recursive_LCS(x, y, i-1, j-1) + 1
    else:
        return max(recursive_LCS(x, y, i-1, j), recursive_LCS(x, y, i, j-1))


def memo_LCS(x, y, i, j):  # top-down
    xlen = len(x)
    ylen = len(y)

    c = [[0]*ylen for _ in range(xlen)]
    if i == 0 and j == 0:
        return c[i][j] + (x[i] == y[j])
    elif i == 0:
        return c[i][j-1] + (x[i] == y[j])
    elif j == 0:
        return c[i-1][j] + (x[i] == y[j])
    if x[i] == y[j]:
        c[i][j] = recursive_LCS(x, y, i-1, j-1) + 1
    else:
        c[i][j] = max(recursive_LCS(x, y, i-1, j), recursive_LCS(x, y, i, j-1))

    return c[-1][-1]


def LCS(x, y):  # bottom-up using DP table
    xlen = len(x)
    ylen = len(y)

    c = [[0]*ylen for _ in range(xlen)]
    for i in range(xlen):
        for j in range(ylen):
            if i == 0 and j == 0:
                c[i][j] += (x[i] == y[j])  # default value = 0
                continue
            elif i == 0:
                c[i][j] = c[i][j-1] + (x[i] == y[j])
                continue
            elif j == 0:
                c[i][j] = c[i-1][j] + (x[i] == y[j])
                continue
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
print(recursive_LCS(a, b, n, m))
print(memo_LCS(a, b, n, m))
print(LCS(a, b))

a = "IKNOWABOUTTHIS"
b = "IGOTTHISTOO"
n = len(a)-1
m = len(b)-1
print(recursive_LCS(a, b, n, m))
print(memo_LCS(a, b, n, m))
print(LCS(a, b))

a = "AAAAAAAAABAAA"
b = "AAAACAAAAAAAA"
n = len(a)-1
m = len(b)-1
print(recursive_LCS(a, b, n, m))
print(memo_LCS(a, b, n, m))
print(LCS(a, b))
