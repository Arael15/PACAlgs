import matplotlib.pyplot as plt

bad = [24, 25, 38, 39]

all = []

for x in range(40):
    for y in range(40):
        if x not in bad and y not in bad:
            f = open('351_results/' + str(x) + '_' + str(y) + '.txt')
            lines = f.readlines()
            f.close()
            lines = [int(line.strip()) for line in lines]
            wrong = sum([1 for l in lines if l < 9500])
            all.append((wrong, (x, y)))
        # lines.sort()
        # if lines[0] < 9500:
        #     print("Found bad in", x, y)

counted = [a for (a, b) in all]
bad_counts = {x:0 for x in range(40)}
for (a, (x, y)) in all:
    if a > 50:
        bad_counts[x] += 1
        bad_counts[y] += 1



plt.hist(counted + [0]*158 + [1] + [10], 50)
plt.savefig('bad_counts_351.png')
plt.show()

# f = open('2397_results/0_0_uniform.txt')
# lines = f.readlines()
# f.close()
# lines = [int(line.strip()) for line in lines]
# # plt.hist(lines, 50, (9500, 10000))
# fig, axes = plt.subplots(2, 2)
# axes[0, 0].hist(lines, 50, (9900, 10000))
# f = open('2397_results/0_24_uniform.txt')
# lines = f.readlines()
# f.close()
# lines = [int(line.strip()) for line in lines]
# axes[0, 1].hist(lines, 50, (9900, 10000))
# f = open('2397_results/24_24_uniform.txt')
# lines = f.readlines()
# f.close()
# lines = [int(line.strip()) for line in lines]
# axes[1, 0].hist(lines, 50, (9900, 10000))
# f = open('2397_results/24_39_uniform.txt')
# lines = f.readlines()
# f.close()
# lines = [int(line.strip()) for line in lines]
# axes[1, 1].hist(lines, 50, (9900, 10000))
# plt.savefig('rect_2397u.png')
# f = open('2397_results/23_23.txt')
# lines = f.readlines()
# f.close()
# lines = [int(line.strip()) for line in lines]
# plt.hist(lines, 50)
# plt.savefig('bad_2397_23_23.png')
plt.show()
