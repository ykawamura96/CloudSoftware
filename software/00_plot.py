import argparse
from matplotlib import pyplot as plt

import pickle
from datetime import datetime
from collections import namedtuple

MeasuredData = namedtuple('MeasuredData',
                          ['os', 'title', 'x_data', 'y_data', 'x_label', 'y_label'])


def plot(m):
    x = m.x_data
    ave = m.y_data[0]
    std = m.y_data[1]
    fig = plt.figure()
    plt.plot(x, ave)
    plt.fill_between(x, ave-std, ave+std, alpha=0.5)
    plt.title(m.title)
    plt.xlabel(m.x_label)
    plt.ylabel(m.y_label)
    # plt.show()

    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Plot results.')
    parser.add_argument("-i", dest="filename", required=True,
                        help="input file with two matrices", metavar="FILE")
    args = parser.parse_args()
    path = args.filename
    with open(path, 'r') as f:
        m = pickle.load(f)
        plot(m)
