import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt

cos = np.cos
sin = np.sin
asin = np.arcsin
atan2 = np.arctan2

from numpy.linalg import norm


def ch_qnormlz(q):
    q = q / norm(q, 2)
    if q[0] < 0:
        q[0] = -q[0]
        q[1] = -q[1]
        q[2] = -q[2]
        q[3] = -q[3]
    return q


def ch_rv2q(rv):
    nm2 = rv.dot(rv)
    if nm2 < 1.e-8:
        q0 = 1 - nm2 * (1 / 8 - nm2 / 384)
        s = 1 / 2 - nm2 * (1 / 48 - nm2 / 3840)
    else:
        nm = np.sqrt(nm2)
        q0 = cos(nm / 2)
        s = sin(nm / 2) / nm
    q = np.concatenate([[q0], s * rv])
    return q


def ch_qmul(q1, q2):
    q = np.array([q1[0] * q2[0] - q1[1] * q2[1] - q1[2] * q2[2] - q1[3] * q2[3],
                  q1[0] * q2[1] + q1[1] * q2[0] + q1[2] * q2[3] - q1[3] * q2[2],
                  q1[0] * q2[2] + q1[2] * q2[0] + q1[3] * q2[1] - q1[1] * q2[3],
                  q1[0] * q2[3] + q1[3] * q2[0] + q1[1] * q2[2] - q1[2] * q2[1]], dtype=np.float64)
    return q


def ch_att_upt(in_, gyr, dt):
    # Véc tơ quay đơn nguyên
    rv = gyr * dt
    dq = ch_rv2q(rv)

    out = ch_qmul(in_, dq)
    out = ch_qnormlz(out)
    return out

def ch_qconj(qin):
    return np.concatenate([[qin[0]], -qin[1:]])

def ch_qmulv(q, vin):
    qi = np.concatenate([[0], vin])
    qo = ch_qmul(ch_qmul(q,qi),ch_qconj(q))
    vout = qo[1:]
    return vout

def ch_nav_equ_local_tan(p, v, q ,acc, gyr, dt, gN):
    # Cập nhật giải pháp điều hướng quán tính, hệ tọa độ Descartes cục bộ, không phụ thuộc vào lực hấp dẫn của Trái đất
    # p vị trí XYZ đơn vị m
    # v tốc độ XYZ đơn vị m/s
    # q Attitude Qb2n, Quaternion
    # acc đối chiếu, Phép đo gia tốc kế đơn vị (m/s^2)
    # gyr vận tốc góc đơn vị (rad/s)
    # dt khoảng thời gian tích phân 0.01s
    # gn véc tơ trọng lực cục bộ
    old_v = v
    sf = acc

    # Attitude ...
    q = ch_att_upt(q, gyr, dt)

    # Giải pháp vận tốc / Velocity
    sf = ch_qmulv(q, sf)
    sf = sf + gN
    v = old_v + dt * sf

    # Giải pháp vị trí
    p = p + (old_v + v) * dt / 2
    return p, v, q

def ch_q2eul_312(Qb2n):
    q0 = Qb2n[0]
    q1 = Qb2n[1]
    q2 = Qb2n[2]
    q3 = Qb2n[3]

    roll = -atan2(2 * (q1 * q3 - q0 * q2), q0 * q0 - q1 * q1 - q2 * q2 + q3 * q3)
    pitch = asin(2 * (q0 * q1 + q2 * q3))
    yaw = -atan2(2 * (q1 * q2 - q0 * q3), q0 * q0 - q1 * q1 + q2 * q2 - q3 * q3)
    return pitch, roll, yaw

# annots = sio.loadmat('../dataset/example_ins2.mat')
# # annots = sio.loadmat('../dataset/example_ins3_hi226_static_30s.mat')
# # acc = np.array(annots['acc'], dtype=np.float64)
# # gyr = np.array(annots['gyr'], dtype=np.float64)
#
# pos_gt = np.array(annots['pos_gt'], dtype=np.float64)
# pos_gt = pos_gt - pos_gt[0,:]
#
# acc = np.array(annots['acc'], dtype=np.float64)
# gyr = np.array(annots['gyr'], dtype=np.float64)
#
# Fs = 100
#
# N = len(acc)
#
# p = np.zeros((3), dtype=np.float64)
# v = np.zeros((3), dtype=np.float64)
# q = np.array([1, 0, 0, 0])
#
# h_pos = np.zeros((N, 3), dtype=np.float64)
#
# for i in range(N):
#     [p ,v , q] = ch_nav_equ_local_tan(p, v, q, acc[i,:], gyr[i,:], 1/Fs, np.array([0, 0, 9.8]))
#     h_pos[i,:] = p
#     # h_att(i,:) = rad2deg(ch_q2eul(q))';
#     # h_vel(i,:) = v;
#     # h_eul(i,:) = ch_q2eul(q);
#
# import matplotlib.pyplot as plt
#
# plt.figure()
# plt.plot(pos_gt[:,0], pos_gt[:,1], '.r')
# plt.plot(h_pos[:,0], h_pos[:,1], '.g')
#
# plt.show()

# annots = sio.loadmat('../dataset/example_ins3_hi226_static_30s.mat')
#
# acc = np.array(annots['acc'], dtype=np.float64)
# gyr = np.array(annots['gyr'], dtype=np.float64)
#
# N = len(acc)
# Fs = 100
#
# # gyr = np.deg2rad(gyr)
# # acc = acc*9.795
#
# p = np.zeros((3), dtype=np.float64)
# v = np.zeros((3), dtype=np.float64)
# q = np.array([1, 0, 0, 0])
#
# pos = np.zeros((N, 3), dtype=np.float64)
#
# for i in range(N):
#     p, v, q = ch_nav_equ_local_tan(p, v, q, acc[i,:], gyr[i,:], 1/Fs, np.array([0, 0, -9.795]))
#     pos[i, :] = p
#
# print("Total %d data, time: %.3fs\n" %(N, N/Fs))
# print("Start position: %.3f %.3f, End position %.3f %.3f, Difference: %.3fm\n" %(pos[0,0], pos[0,1], pos[N-1,0], pos[N-1,1], norm(pos[N-1, 0:2] - pos[0, 0:2], 2)))
#
# plt.figure()
# ax = plt.axes(projection='3d')
# ax.plot3D([pos[0,0]], [pos[0,1]], [pos[0,2]], '-ks')
# ax.plot3D(pos[:,0], pos[:,1], pos[:,2], '.b')
# plt.show()

annots = sio.loadmat('../dataset/example_ins4.mat')

acc_x = np.array(annots['acc'], dtype=np.float64)[0]
acc_y = np.array(annots['acc'], dtype=np.float64)[1]
acc_z = np.array(annots['acc'], dtype=np.float64)[2]

gyr_x = np.array(annots['gyr'], dtype=np.float64)[0]
gyr_y = np.array(annots['gyr'], dtype=np.float64)[1]
gyr_z = np.array(annots['gyr'], dtype=np.float64)[2]

N = len(acc_x)
Fs = 100

# gyr = np.deg2rad(gyr)
# acc = acc*9.795

p = np.zeros((3), dtype=np.float64)
v = np.zeros((3), dtype=np.float64)
q = np.array([1, 0, 0, 0])

pos = np.zeros((N, 3), dtype=np.float64)

for i in range(N):
    p, v, q = ch_nav_equ_local_tan(p, v, q, np.array([acc_x[i], acc_y[i], acc_z[i]]), np.array([gyr_x[i], gyr_y[i], gyr_z[i]]), 1/ Fs, np.array([0, 0, -9.8]))
    pos[i, :] = p

print("Total %d data, time: %.3fs\n" %(N, N/Fs))
print("Start position: %.3f %.3f, End position %.3f %.3f, Difference: %.3fm\n" %(pos[0,0], pos[0,1], pos[N-1,0], pos[N-1,1], norm(pos[N-1, 0:2] - pos[0, 0:2], 2)))

plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D([pos[0,0]], [pos[0,1]], [pos[0,2]], '-ks')
ax.plot3D(pos[:,0], pos[:,1], pos[:,2], '.b')
plt.show()
