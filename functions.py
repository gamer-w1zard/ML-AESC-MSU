def prod_non_zero_diag(x):
    """Compute product of nonzero elements from matrix diagonal.

    input:
    x -- 2-d numpy array
    output:
    product -- integer number


    Not vectorized implementation.
    """
    n = len(x)
    m = len(x[0])
    ans = 1
    for i in range(min(n, m)):
        if (x[i][i] != 0):
            ans *= x[i][i]
    return ans


def are_multisets_equal(x, y):
    """Return True if both vectors create equal multisets.

    input:
    x, y -- 1-d numpy arrays
    output:
    True if multisets are equal, False otherwise -- boolean

    Not vectorized implementation.
    """
    x1.sort()
    y1.sort()
    return (x1 == y1)


def max_after_zero(x):
    """Find max element after zero in array.

    input:
    x -- 1-d numpy array
    output:
    maximum element after zero -- integer number

    Not vectorized implementation.
    """
    ans = -1000000000
    for i in range(1, len(x)):
        if (x[i - 1] == 0 and x[i] > ans):
            ans = x[i]
    return ans


def convert_image(img, coefs):
    """Sum up image channels with weights from coefs array

    input:
    img -- 3-d numpy array (H x W x 3)
    coefs -- 1-d numpy array (length 3)
    output:
    img -- 2-d numpy array

    Not vectorized implementation.
    """
    n = len(img);
    m = len(img[0])
    k = len(coefs)
    ans = [[0.0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            cnt = 0.0
            for q in range(k):
                cnt += img[i][j][q] * coefs[q]
            ans[i][j] = cnt
    return ans


def run_length_encoding(x):
    """Make run-length encoding.

    input:
    x -- 1-d numpy array
    output:
    elements, counters -- integer iterables

    Not vectorized implementation.
    """
    if (len(x) == 0):
        return [], []
    values = []
    counts = []
    cnt = 1
    values.append(x[0])
    for i in range(1, len(x)):
        if (x[i] == x[i - 1]):
            cnt += 1
        else:
            counts.append(cnt)
            cnt = 1
            values.append(x[i])
    counts.append(cnt)
    return values, counts


def pairwise_distance(x, y):
    """Return pairwise object distance.

    input:
    x, y -- 2d numpy arrays
    output:
    distance array -- 2d numpy array

    Not vectorized implementation.
    """
    from math import sqrt
    n = len(x)
    m = len(y)
    k = len(x[0])
    ans = [[0.0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            s = 0.0
            for q in range(k):
                s += (x[i][q] - y[j][q]) ** 2
            ans[i][j] = sqrt(s)
    return ans
