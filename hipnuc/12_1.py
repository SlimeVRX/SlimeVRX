import scipy.io as sio
import numpy as np
from HiPNUC.lib.ch_nav_equ_local_tan import ch_nav_equ_local_tan

annots = sio.loadmat('example_ins2.mat')

pos_gt = np.array(annots['pos_gt'], dtype=np.float64)
pos_gt = pos_gt - pos_gt[0,:]

acc = np.array(annots['acc'], dtype=np.float64)
gyr = np.array(annots['gyr'], dtype=np.float64)

Fs = 100

N = len(acc)

p = np.zeros((3), dtype=np.float64)
v = np.zeros((3), dtype=np.float64)
q = np.array([1, 0, 0, 0])

h_pos = np.zeros((N, 3), dtype=np.float64)

for i in range(N):
    [p ,v , q] = ch_nav_equ_local_tan(p, v, q, acc[i,:], gyr[i,:], 1/Fs, np.array([0, 0, 9.8]))
    h_pos[i,:] = p
    # h_att(i,:) = rad2deg(ch_q2eul(q))';
    # h_vel(i,:) = v;
    # h_eul(i,:) = ch_q2eul(q);

import matplotlib.pyplot as plt

plt.figure()
plt.plot(pos_gt[:,0], pos_gt[:,1], '.r')
plt.plot(h_pos[:,0], h_pos[:,1], '.g')

plt.show()
