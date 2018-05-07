import matplotlib
import matplotlib.pyplot as plt
#
# fig, axes = plt.subplots(2, 2)
# # plt.axhline(y=2, color='r', linestyle=':')
# # plt.axhline(y=7, color='r', linestyle=':')
# # plt.axvline(x=1, color='r', linestyle=':')
# # plt.axvline(x=6, color='r', linestyle=':')
# for x in [axes[0, 0], axes[0, 1], axes[1, 0], axes[1, 1]]:
#     x.plot([2, 8], [2, 2], 'b-')
#     x.plot([2, 2], [2, 8], 'b-')
#     x.plot([8, 2], [8, 8], 'b-')
#     x.plot([8, 8], [8, 2], 'b-')
#     # plt.plot([3, 6.5, 8, 7, 2], [8, 1, 4, 9, 1], 'ro')
#     # plt.plot([3, 4, 5], [4, 6, 3], 'bo')
#     x.plot([2.5, 7.5], [2.5, 2.5], 'g-')
#     x.plot([2.5, 2.5], [2.5, 7.5], 'g-')
#     x.plot([7.5, 2.5], [7.5, 7.5], 'g-')
#     x.plot([7.5, 7.5], [7.5, 2.5], 'g-')
#     # plt.plot([3, 5], [3, 3], 'g-')
#     # plt.plot([3, 3], [6, 3], 'g-')
#     # plt.plot([5, 3], [6, 6], 'g-')
#     # plt.plot([5, 5], [6, 3], 'g-')
#     # plt.fill_between([2, 8], 7.5, 8, color='g')
#     x.axis([1, 9, 1, 9])
# axes[0, 0].fill_between([2, 8], 7.5, 8, color='g')
# axes[0, 1].fill_between([2, 8], 2, 2.5, color='g')
# axes[1, 0].fill_between([2, 2.5], 2, 8, color='g')
# axes[1, 1].fill_between([7.5, 8], 2, 8, color='g')
# plt.savefig('rectangle_1.png')
# # plt.show()

f = open('351_results/39_39.txt')
lines = f.readlines()
f.close()
lines = [int(line.strip()) for line in lines]
plt.hist(lines, 100, (9000, 10000))
plt.show()



