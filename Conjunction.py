import numpy as np
from math import ceil, log
import time


def beta_10000(a, b, n):
    return 10000 * np.random.beta(a, b, n)


def pareto_10000(a, n):
    return 10000 * np.random.pareto(a, n)


distributions = {
    0: (beta_10000, (0.5, 0.5)),
    1: (beta_10000, (0.5, 2)),
    2: (beta_10000, (2, 0.5)),
    3: (beta_10000, (2, 2)),
    4: (beta_10000, (1, 5)),
    5: (beta_10000, (5, 1)),
    6: (np.random.gamma, (1, 5000)),
    7: (np.random.gamma, (5, 1000)),
    8: (np.random.gamma, (10, 500)),
    9: (np.random.gamma, (50, 100)),
    10: (np.random.geometric, (0.0005,)),
    11: (np.random.geometric, (0.001,)),
    12: (np.random.gumbel, (5000, 2000)),
    13: (np.random.gumbel, (5000, 1000)),
    14: (np.random.gumbel, (5000, 250)),
    15: (np.random.laplace, (5000, 1500)),
    16: (np.random.laplace, (5000, 500)),
    17: (np.random.logistic, (5000, 1500)),
    18: (np.random.logistic, (5000, 250)),
    19: (np.random.logistic, (5000, 750)),
    20: (np.random.lognormal, (5, 5)),
    21: (np.random.lognormal, (5, 3)),
    22: (np.random.lognormal, (2, 10)),
    23: (np.random.logseries, (0.9999,)),
    24: (np.random.logseries, (0.999,)),
    25: (np.random.logseries, (0.99,)),
    26: (pareto_10000, (3,)),
    27: (pareto_10000, (5,)),
    28: (pareto_10000, (10,)),
    29: (np.random.rayleigh, (5000,)),
    30: (np.random.rayleigh, (2500,)),
    31: (np.random.uniform, (0, 10000)),
    32: (np.random.wald, (5000, 1000)),
    33: (np.random.wald, (5000, 100)),
    34: (np.random.wald, (5000, 10)),
    35: (np.random.zipf, (1.5,)),
    36: (np.random.zipf, (2,))
}


def divide_two(array):
    new_array = list(map(lambda x: x/10000, array))
    return [0 if x < 1/2 else 1 for x in new_array]


def divide_three(array):
    return [-1 if x < 1/3 else 0 if 1/3 <= x < 2/3 else 1 for x in array]


def mark_sample(sample, sequence):
    for x in range(len(sequence)):
        if sequence[x] == 2:
            return (sample, False)
        if sequence[x] == 1:
            if sample[x] == 0:
                return (sample, False)
        elif sequence[x] == -1:
            if sample[x] == 1:
                return (sample, False)
    return (sample, True)


def train_hypothesis(labeled):
    pos_labeled = [l for l in labeled if l[1]]
    base = {x: {-1, 1} for x in range(len(labeled[0][0]))}
    for pos in pos_labeled:
        for x in range(len(base)):
            if pos[0][x] == 0:
                base[x].discard(1)
            elif pos[0][x] == 1:
                base[x].discard(-1)
    return [-1 if base[x] == {-1} else 1 if base[x] == {1} else 0 if not base[x] else 2 for x in sorted(base)]


def test_hypothesis(data, hypothesis, actual):
    marked_hypothesis = [mark_sample(d, hypothesis) for d in data]
    marked_actual = [mark_sample(d, actual) for d in data]
    compared = [x for x in range(len(marked_actual)) if marked_hypothesis[x] == marked_actual[x]]
    return len(compared)


def sample_test(m, n, s, trials):
    for x in range(len(distributions)):
        dist, args = distributions[x]
        f = open('n' + str(n) + '_results/' + str(x) + '.txt', 'w')
        for y in range(trials):
            print('Running distribution', x+1, 'trial', y+1)
            if len(args) == 2:
                train = dist(args[0], args[1], m*n)
                test = dist(args[0], args[1], s*n)
            else:
                train = dist(args[0], m*n)
                test = dist(args[0], s*n)
            seq = divide_three(np.random.uniform(0, 1, n))
            train = train.reshape(m, n)
            train = [tuple(divide_two(t)) for t in train]
            test = test.reshape(s, n)
            test = [tuple(divide_two(t)) for t in test]
            print('generated')
            train_set = set(train)
            hypothesis = train_hypothesis([mark_sample(t, seq) for t in train_set])
            print('trained')
            correct = test_hypothesis(test, hypothesis, seq)
            f.write(str(correct) + '\n')
        f.close()


def pac_test(delta, epsilon, n, test_samples, trials):
    samples = ceil((2*n/epsilon) * log(2*n/delta))
    sample_test(samples, n, test_samples, trials)


if __name__ == '__main__':
    start = time.time()
    pac_test(0.05, 0.05, 20, 10000, 1000)
    pac_test(0.05, 0.05, 50, 1000, 1000)
    # pac_test(0.01, 0.01, 10)
    end = time.time()
    print(end - start)
