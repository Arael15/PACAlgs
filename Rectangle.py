import numpy as np
from math import ceil, log
import time

# m = 100


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
    26: (np.random.normal, (5000, 2500)),
    27: (np.random.normal, (5000, 1000)),
    28: (np.random.normal, (5000, 100)),
    29: (pareto_10000, (3,)),
    30: (pareto_10000, (5,)),
    31: (pareto_10000, (10,)),
    32: (np.random.rayleigh, (5000,)),
    33: (np.random.rayleigh, (2500,)),
    34: (np.random.uniform, (0, 10000)),
    35: (np.random.wald, (5000, 1000)),
    36: (np.random.wald, (5000, 100)),
    37: (np.random.wald, (5000, 10)),
    38: (np.random.zipf, (1.5,)),
    39: (np.random.zipf, (2,))
}

def sample_test(m):

    for x in range(len(distributions)):
        for y in range(len(distributions)):
            print('Now running distribution', x, y)
            x_var, x_args = distributions[x]
            y_var, y_args = distributions[y]
            f = open(str(m) + '_results/' + str(x) + '_' + str(y) + '.txt', 'w')
            fu = open(str(m) + '_results/' + str(x) + '_' + str(y) + '_uniform.txt', 'w')
            for z in range(1000):
                # print('Now running distribution pair', x, y, 'Trial:', z+1)
                if len(x_args) == 2:
                    rect_x = sorted(x_var(x_args[0], x_args[1], 2))
                    train_x = x_var(x_args[0], x_args[1], m)
                    test_x = x_var(x_args[0], x_args[1], 10000)
                else:
                    rect_x = sorted(x_var(x_args[0], 2))
                    train_x = x_var(x_args[0], m)
                    test_x = x_var(x_args[0], 10000)
                if len(y_args) == 2:
                    rect_y = sorted(y_var(y_args[0], y_args[1], 2))
                    train_y = y_var(y_args[0], y_args[1], m)
                    test_y = y_var(y_args[0], y_args[1], 10000)
                else:
                    rect_y = sorted(y_var(y_args[0], 2))
                    train_y = y_var(y_args[0], m)
                    test_y = y_var(y_args[0], 10000)
                train_xy = list(zip(train_x, train_y))
                pos_train = [((a, b), 1) for (a, b) in train_xy if rect_x[0] < a < rect_x[1] and rect_y[0] < b < rect_y[1]]
                if len(pos_train) < 2:
                    predict_x, predict_y = ((0, 0), (0, 0))
                else:
                    sort_x = sorted(pos_train, key=lambda n: n[0][0])
                    sort_y = sorted(pos_train, key=lambda n: n[0][1])
                    predict_x = (sort_x[0][0][0], sort_x[-1][0][0])
                    predict_y = (sort_y[0][0][1], sort_y[-1][0][1])
                rect_x_uniform = sorted(np.random.uniform(0, 10000, 2))
                rect_y_uniform = sorted(np.random.uniform(0, 10000, 2))
                pos_train_uniform = [((a, b), 1) for (a, b) in train_xy
                                     if rect_x_uniform[0] < a < rect_x_uniform[1]
                                     and rect_y_uniform[0] < b < rect_y_uniform[1]]
                if len(pos_train_uniform) < 2:
                    predict_x_uniform, predict_y_uniform = ((0, 0), (0, 0))
                else:
                    sort_x_uniform = sorted(pos_train_uniform, key=lambda l: l[0][0])
                    sort_y_uniform = sorted(pos_train_uniform, key=lambda l: l[0][1])
                    predict_x_uniform = (sort_x_uniform[0][0][0], sort_x_uniform[-1][0][0])
                    predict_y_uniform = (sort_y_uniform[0][0][1], sort_y_uniform[-1][0][1])

                test_xy = list(zip(test_x, test_y))
                # predict_true = set([(a, b) for (a, b) in test_xy if
                #                     predict_x[0] < a < predict_x[1] and predict_y[0] < b < predict_y[1]])
                # predict_false = set([(a, b) for (a, b) in test_xy if
                #                      not (predict_x[0] < a < predict_x[1] and predict_y[0] < b < predict_y[1])])
                # real_true = set([(a, b) for (a, b) in test_xy if
                #                  rect_x[0] < a < rect_x[1] and rect_y[0] < b < rect_y[1]])
                # real_false = set([(a, b) for (a, b) in test_xy if
                #                   not (rect_x[0] < a < rect_x[1] and rect_y[0] < b < rect_y[1])])
                # predict_true_u = set([(a, b) for (a, b) in test_xy if
                #                       predict_x_uniform[0] < a < predict_x_uniform[1]
                #                       and predict_y_uniform[0] < b < predict_y_uniform[1]])
                # predict_false_u = set([(a, b) for (a, b) in test_xy if
                #                        not (predict_x_uniform[0] < a < predict_x_uniform[1]
                #                             and predict_y_uniform[0] < b < predict_y_uniform[1])])
                # real_true_u = set([(a, b) for (a, b) in test_xy if
                #                    rect_x_uniform[0] < a < rect_x_uniform[1]
                #                    and rect_y_uniform[0] < b < rect_y_uniform[1]])
                # real_false_u = set([(a, b) for (a, b) in test_xy if
                #                     not (rect_x_uniform[0] < a < rect_x_uniform[1]
                #                          and rect_y_uniform[0] < b < rect_y_uniform[1])])
                # correct = [i for i in predict_true if i in real_true] + [i for i in predict_false if i in real_false]
                # correct_u = [i for i in predict_true_u if i in real_true_u] \
                #             + [i for i in predict_false_u if i in real_false_u]
                predict_wrong = [(a, b) for (a, b) in test_xy if
                                 not (predict_x[0] < a < predict_x[1] and predict_y[0] < b < predict_y[1])
                                 and (rect_x[0] < a < rect_x[1] and rect_y[0] < b < rect_y[1])]
                predict_wrong_u = [(a, b) for (a, b) in test_xy if
                                   not (predict_x_uniform[0] < a < predict_x_uniform[1]
                                        and predict_y_uniform[0] < b < predict_y_uniform[1])
                                   and (rect_x_uniform[0] < a < rect_x_uniform[1]
                                        and rect_y_uniform[0] < b < rect_y_uniform[1])]
                # print(predict_true)
                # print(predict_false)
                # print(real_true)
                # print(real_false)
                # print(predict_x)
                # print(predict_y)
                # print(rect_x)
                # print(rect_y)
                # print(len(predict_true))
                # f.write(str(len(correct)) + '\n')
                # fu.write(str(len(correct_u)) + '\n')
                f.write(str(10000 - len(predict_wrong)) + '\n')
                fu.write(str(10000 - len(predict_wrong_u)) + '\n')
            f.close()
            fu.close()


def pac_test(delta, epsilon):
    samples = ceil((4/epsilon) * log(4/delta))
    print(samples)
    sample_test(samples)


if __name__ == '__main__':
    start = time.time()
    pac_test(0.05, 0.05)
    pac_test(0.01, 0.01)
    end = time.time()
    print(end - start)
