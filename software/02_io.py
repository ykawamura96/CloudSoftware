import argparse
import time
import random
import string
import pickle
import subprocess
import numpy as np
from datetime import datetime
from collections import namedtuple
from matplotlib import pyplot as plt
MeasuredData = namedtuple('MeasuredData',
                          ['os', 'title', 'x_data', 'y_data', 'x_label', 'y_label'])

def randomname(n):
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
   return ''.join(randlst)

def write_file(fname, size):
    s = randomname(size)
    with open(fname, 'wb') as f:
        f.write(s)

def read_file(fname):
    with open(fname, 'r') as f:
       s = f.read()
       a = len(s)
        

def init_file(fname):
    com1 = 'rm {} -rf'.format(fname)
    com2 = 'touch {}'.format(fname)
    subprocess.call(com1.split(' '))
    subprocess.call(com2.split(' '))
    
def mesure_time(fname, size, n_trial):
    elapsed = []
    for i in range (n_trial):
        init_file(fname)
        before = time.time()
        write_file(fname, size)
        read_file(fname)
        elapsed.append(time.time() - before)
    return elapsed

def save_time(max_size, n_trial, step=10, hosttype='Linux'):
   start = time.time()
   print("start")
   fname = '/tmp/tmp.txt'
   averages = []
   stds = []
   x = np.arange(0, max_size, step)
   # fig = plt.figure()
   for i in range(0, max_size, step):
      elapsed = mesure_time(fname, size=i, n_trial=n_trial)
      averages.append(np.average(elapsed))
      stds.append(np.std(elapsed))
   print("finished, total time: {}".format(time.time() - start))
   averages = np.array(averages)
   stds = np.array(stds)
   # plt.plot(x, averages)
   # plt.fill_between(x, averages-stds, averages+stds, alpha=0.5)
   # plt.show()
   now = datetime.now()
   m = MeasuredData(hosttype, 'IO', x, [averages, stds], 'size of file', 'time')
   fname = '{}-{}-{}{}{}{}{}'.format(m.os, m.title, now.year, now.month, now.day, now.hour, now.minute)
   with open('resources/{}.pkl'.format(fname), 'wb') as f:
      pickle.dump(m , f)
    

if __name__ == '__main__':
   parser = argparse.ArgumentParser(description='Plot results.')
   parser.add_argument("-t", dest="hosttype", required=True,
                       help="host os type", metavar="FILE")
   args = parser.parse_args()
   hosttype = args.hosttype   
   save_time(max_size=10000, n_trial=10, step=100, hosttype=hosttype)
