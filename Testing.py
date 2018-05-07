import matplotlib.pyplot as plt


for x in range(40):
    for y in range(40):
        f = open('351_results/' + str(x) + '_' + str(y) + '.txt')
        lines = f.readlines()
        f.close()
        lines = [int(line.strip()) for line in lines]
        lines.sort()
        if lines[0] < 9500:
            print("Found bad in", x, y)

f = open('351_results/0_23.txt')
lines = f.readlines()
f.close()
lines = [int(line.strip()) for line in lines]
plt.hist(lines)
plt.show()
