__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

def interpreter(conn):
    tspec = conn.readline().strip().split(' ')
    tspecint = [int(x) for x in tspec]
    tspecint.insert(0, 0)
    ttresh = int(conn.readline().strip())
    tmax = int(conn.readline().strip())
    return tspecint, ttresh, tmax


def calc_size(i, j):
    s = 0.0
    new_t = j - spectrum[i]
    if new_t < 0 or new_t > max_score:
        return s
    for aa in [57, 71, 87, 97, 99, 101, 103, 113, 113, 114, 115, 128, 128, 129, 131, 137, 147, 156, 163, 186]:
        if i - aa >= 0:
            s += proba[i-aa][new_t]
    s /= 20
    return s


if __name__ == '__main__':
    with open('dataset_11866_11.txt', 'r') as f:
        spectrum, threshold, max_score = interpreter(f)

    mass = len(spectrum) - 1
    proba = [[0 for _ in range(max_score+1)] for __ in range(mass+1)]
    proba[0][0] = 1
    for i in range(1, mass+1):
        for j in range(1, max_score+1):
            proba[i][j] = calc_size(i, j)
    total = sum(proba[mass][threshold:max_score])
    print(total)
