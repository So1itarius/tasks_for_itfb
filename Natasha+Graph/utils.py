import matplotlib.pyplot as plt
import numpy as np
import time

d = {"Name(first='уильям', middle=None, last=None, nick=None)": 3,
     "Name(first='анастасия', middle=None, last='заворотнюк', nick=None)": 1}


def diagram(d):
    #colors = list("rgbcmyk")
    #x = d.keys()
    #y = d.values()
    #plt.scatter(x, y, color=colors.pop())
    #plt.legend(d.keys())
    #plt.show()

    jet = plt.cm.jet
    colors = jet(np.linspace(0, 1, len(d)))

    fig, ax = plt.subplots()
    for color in colors:
        x = d.keys()
        y = d.values()
        ax.scatter(x, y, color=color, s=90, marker='.')
        plt.ylabel("Errors", fontsize=18, color="Green")
        plt.xlabel("Occured on", fontsize=18, color="Green")
        plt.title("DDN23b", fontsize=25, color="Blue")
        ax.get_xaxis().get_major_formatter()
        plt.xticks(rotation='vertical')

    plt.xticks(plt.xticks()[0],
               [time.strftime("%m/%d/%y, %H:%M:%S", time.localtime(item))
                for item in plt.xticks()[0] * 3600])
    plt.legend(d.keys())
    plt.subplots_adjust(bottom=.24, right=.98, left=0.03, top=.89)
    plt.grid()
    plt.show()

diagram(d)