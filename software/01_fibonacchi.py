import argparse
import time
import numpy as np
import pickle
from datetime import datetime
from collections import namedtuple

MeasuredData = namedtuple('MeasuredData',
                          ['os', 'title', 'x_data', 'y_data', 'x_label', 'y_label'])

def fibonacci (n):
    f =0; fn = 1; fnn = 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    for i in range(n-2):
        fnn_tmp = fn + fnn; fn = fnn; f = fn; fnn = fnn_tmp
    return fnn

def mesure_time(n_fib, n_trial):
    elapsed = []
    for i in range (n_trial):
        before = time.time()
        fibonacci(n_fib)
        after = time.time()
        elapsed.append(after - before)
    return elapsed

def save_time(max_fib, n_trial, step=10, hosttype='Linux'):
    averages = []
    stds = []
    x = np.arange(0, max_fib, step)
    for i in range(0, max_fib, step):
        elapsed = mesure_time(n_fib=i, n_trial=n_trial)
        averages.append(np.average(elapsed))
        stds.append(np.std(elapsed))
        # print('fib: {}, elapsed {}'.format(i, np.average(elapsed)))
    averages = np.array(averages)
    stds = np.array(stds)
    now = datetime.now()
    m = MeasuredData(hosttype, 'fibonacci', x, [averages, stds], 'fibonacci(n)', 'time')

    fname = '{}-{}-{}{}{}{}{}'.format(m.os, m.title, now.year, now.month, now.day, now.hour, now.minute)
    with open('resources/{}.pkl'.format(fname), 'wb') as f:
        pickle.dump(m , f)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot results.')
    parser.add_argument('-t', dest="hosttype", required=True,
                        help='host os type', metavar='FILE')
    args = parser.parse_args()
    hosttype = args.hosttype
    save_time(max_fib=10000, step=50, n_trial=100, hosttype=hosttype)
