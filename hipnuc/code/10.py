import scipy.io as sio
import numpy as np
cos = np.cos
sin = np.sin
asin = np.arcsin
atan2 = np.arctan2

def ch_rv2q(rv):
    nm2 = rv.dot(rv)
    if nm2 < 1.e-8:
        q0 = 1-nm2*(1/8-nm2/384)
        s = 1/2-nm2*(1/48-nm2/3840)
    else:
        nm = np.sqrt(nm2)
        q0 = cos(nm/2)
        s = sin(nm/2)/nm
    q = np.concatenate([[q0],s*rv])
    return q

def ch_qmul(q1, q2):
    q = np.array([ q1[0] * q2[0] - q1[1] * q2[1] - q1[2] * q2[2] - q1[3] * q2[3],
                   q1[0] * q2[1] + q1[1] * q2[0] + q1[2] * q2[3] - q1[3] * q2[2],
                   q1[0] * q2[2] + q1[2] * q2[0] + q1[3] * q2[1] - q1[1] * q2[3],
                   q1[0] * q2[3] + q1[3] * q2[0] + q1[1] * q2[2] - q1[2] * q2[1] ], dtype=np.float64)
    return q

from numpy.linalg import norm
def ch_qnormlz(q):
    q = q / norm(q,2)
    if q[0] < 0:
        q[0] = -q[0]
        q[1] = -q[1]
        q[2] = -q[2]
        q[3] = -q[3]
    return q

def ch_q2m(Qb2n):
    q11 = Qb2n[0]*Qb2n[0]; q12 = Qb2n[0]*Qb2n[1]; q13 = Qb2n[0]*Qb2n[2]; q14 = Qb2n[0]*Qb2n[3]
    q22 = Qb2n[1]*Qb2n[1]; q23 = Qb2n[1]*Qb2n[2]; q24 = Qb2n[1]*Qb2n[3]
    q33 = Qb2n[2]*Qb2n[2]; q34 = Qb2n[2]*Qb2n[3]
    q44 = Qb2n[3]*Qb2n[3]
    Cb2n = np.array([[ q11+q22-q33-q44,  2*(q23-q14),     2*(q24+q13)],
                     [2*(q23+q14),      q11-q22+q33-q44, 2*(q34-q12)],
                     [2*(q24-q13),      2*(q34+q12),     q11-q22-q33+q44 ]], dtype=np.float64)
    return Cb2n

def ch_m2eul_312(Cb2n):
    beta = asin(Cb2n[2,1])
    alpha = atan2(-Cb2n[2,0], Cb2n[2,2])
    gamma = atan2(-Cb2n[0,1], Cb2n[1,1])
    return beta, alpha, gamma

annots = sio.loadmat('gyroReading__.mat')
gyroReading = np.array([item for item in annots['gyroReading']], dtype=np.float64)

dt = 0.01
N = len(gyroReading)

eul = np.zeros((N, 3), dtype=np.float64)

Qb2n = np.array([1, 0, 0, 0])

for i in range(N):
    theta = np.deg2rad(gyroReading[i]) * dt

    Q_m2m_1 = ch_rv2q(theta)

    Qb2n = ch_qmul(Qb2n, Q_m2m_1)

    Qb2n = ch_qnormlz(Qb2n)

    Cb2n = ch_q2m(Qb2n)

    eul[i,:] = np.rad2deg(ch_m2eul_312(Cb2n))
    # a, b, c = np.rad2deg(ch_m2eul_312(Cb2n))
    # print("Quaternion to Euler angles: %.3f %.3f %.3f " % (a, b, c))

import matplotlib.pyplot as plt
plt.plot(eul)
ax = plt.subplot()
ax.legend(["PITCH(deg)", "ROLL(deg)", "YAW(deg)"])
plt.show()