import numpy as np


def prod_non_zero_diag(x):
    """Compute product of nonzero elements from matrix diagonal.

    input:
    x -- 2-d numpy array
    output:
    product -- integer number


    Vectorized implementation.
    """
    x = np.diag(x)
    data = x[x != 0]
    ans = np.prod(data)
    return ans
    pass


def are_multisets_equal(x, y):
    """Return True if both vectors create equal multisets.

    input:
    x, y -- 1-d numpy arrays
    output:
    True if multisets are equal, False otherwise -- boolean

    Vectorized implementation.
    """
    return np.array_equal(np.sort(x), np.sort(y))
    pass


def max_after_zero(x):
    """Find max element after zero in array.

    input:
    x -- 1-d numpy array
    output:
    maximum element after zero -- integer number

    Vectorized implementation.
    """
    left = x[:-1]
    mask = (left == 0)
    return np.max(x[1:][mask])
    pass


def convert_image(img, coefs):
    """Sum up image channels with weights from coefs array

    input:
    img -- 3-d numpy array (H x W x 3)
    coefs -- 1-d numpy array (length 3)
    output:
    img -- 2-d numpy array

    Vectorized implementation.
    """
    img = np.asarray(img)
    coefs = np.asarray(coefs)
    return (img * coefs).sum(axis=2)
    pass


def run_length_encoding(x):
    """Make run-length encoding.

    input:
    x -- 1-d numpy array
    output:
    elements, counters -- integer iterables

    Vectorized implementation.
    """
    if x.size == 0:
        return np.array([]), np.array([])
    change = x[1:] != x[:-1]
    starts = np.r_[0, np.where(change)[0] + 1]
    values = x[starts]
    counts = np.diff(np.r_[starts, x.size])
    return values, counts
    pass


def pairwise_distance(x, y):
    """Return pairwise object distance.

    input:
    x, y -- 2d numpy arrays
    output:
    distance array -- 2d numpy array

    Vctorized implementation.
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    x1 = np.sum(x * x, axis=1)[:, None]
    y1 = np.sum(y * y, axis=1)[None, :]
    s = x1 + y1 - 2 * x @ y.T
    s = np.maximum(s, 0)
    return np.sqrt(s)
    pass
