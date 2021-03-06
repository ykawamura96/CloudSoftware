import argparse
from matplotlib import pyplot as plt
import pickle
from datetime import datetime
from collections import namedtuple

MeasuredData = namedtuple('MeasuredData',
                          ['os', 'title', 'x_data', 'y_data', 'x_label', 'y_label'])

def plot(ms):
    fig = plt.figure()
    for m in ms:
        x = m.x_data
        ave = m.y_data[0]
        std = m.y_data[1]
        if "hyp" in m.os:
            plt.plot(x, ave*1000, label="virtualbox_4cpu")
        else:
            plt.plot(x, ave*1000, label=m.os)
        plt.fill_between(x, (ave-std)*1000, (ave+std)*1000, alpha=0.4)
        print(m.os)
    plt.legend()
    plt.title(m.title)
    plt.xlabel("size of file [bytes]")
    plt.ylabel("time [ms]")
    plt.ylim(0, 10)
    # plt.show()
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Plot results.')
    parser.add_argument("-i", dest="filenames", required=True, nargs='+',
                        help="input file with two matrices", metavar="FILE")
    args = parser.parse_args()
    files = args.filenames
    ms = [pickle.load(open(f, 'rb')) for f in files]
    plot(ms)
    plt.show()
