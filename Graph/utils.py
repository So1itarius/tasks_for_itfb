import matplotlib.pyplot as plt


def diagram(d):
    colors = list("rgbcmyk")
    x = d.keys()
    y = d.values()
    plt.scatter(x, y, color=colors.pop())
    plt.legend(d.keys())
    plt.show()
