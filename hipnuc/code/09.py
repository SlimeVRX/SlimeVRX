'''
clear;
clc
close all;

%% 已知
w = [2 -3 5]';
dt = 0.01; %姿态更新周期: 0.01s = 100Hz
dur = 100; %积分时长 单位s


N = dur / dt; %积分次数
eul = zeros(N, 3);
fprintf("已知b系角速度(陀螺仪输出为):%.3fdeg/s %.3fdeg/s %.3fdeg/s\n", w(1), w(2), w(3));


Cb2n = eye(3);
theta = deg2rad(w)*dt; %定轴转动下: 等效旋转矢量 = 角增量 = 角速度*dt


for i = 1:N
    C_m2m_1 = ch_rv2m(theta);
    Cb2n = Cb2n * C_m2m_1;

    %单位阵正交化
    Cb2n = ch_mnormlz(Cb2n);

    %记录每一步的欧拉角
    eul(i,:) = rad2deg(ch_m2eul(Cb2n));
end


plot(eul)
legend("PITCH(deg)", "ROLL(deg)", "YAW(deg)");

tmp =eul(end,:);
fprintf("最终欧拉角: pich:%.4f° roll:%.4f° yaw:%.4f°\n", tmp(1), tmp(2), tmp(3));
'''

import numpy as np

sin = np.sin
cos = np.cos
atan2 = np.arctan2
asin = np.arcsin

def ch_askew(v):
    m = np.array([[0,     -v[2],   v[1]],
                  [v[2],   0,     -v[0]],
                  [-v[1],   v[0],   0]], dtype=np.float64)
    return m

def ch_rv2m(rv):
    nm2 = rv.dot(rv)
    if nm2 < 1.e-8:     #không hiểu
        a = 1 - nm2 * (1 / 6 - nm2 / 120)
        b = 0.5 - nm2 * (1 / 24 - nm2 / 720)
    else:
        nm = np.sqrt(nm2)
        a = sin(nm) / nm
        b = (1 - cos(nm)) / nm2
    VX = ch_askew(rv)
    m = np.identity(3) + a * VX + b * VX.dot(VX)
    return m

def ch_mnormlz(Cb2n):
    for i in range(4):
        # Cnb = 0.5 * (Cnb + (Cnb')^-1)                       # Algorithm 1
        Cb2n = 1.5*Cb2n - 0.5*(Cb2n.dot(Cb2n.T)).dot(Cb2n)    # Algorithm 2
    return Cb2n

def ch_m2eul_321(Cb2n):
    beta = atan2(Cb2n[2,1], Cb2n[2,2])
    alpha = asin(-Cb2n[2,0])
    gamma = atan2(Cb2n[1,0],Cb2n[0,0])
    return beta, alpha, gamma

def ch_m2eul_312(Cb2n):
    beta = asin(Cb2n[2,1])
    alpha = atan2(-Cb2n[2,0], Cb2n[2,2])
    gamma = atan2(-Cb2n[0,1], Cb2n[1,1])
    return beta, alpha, gamma

w = np.array([2, -3, 5])
dt = 0.01   # Thời gian cập nhật thái độ: 0,01 giây = 100Hz
dur = 100   # Thời lượng duration

N = int(dur / dt)   # điểm points
eul = np.zeros((N, 3), dtype=np.float64)
# vận tốc góc hệ b (đầu ra con quay hồi chuyển)
print("Angular velocity (gyro output is): %.3fdeg/s %.3fdeg/s %.3fdeg/s\n" %(w[0], w[1], w[2]))

Cb2n = np.identity(3)
theta = np.deg2rad(w)*dt    # Theo trục quay cố định: Vectơ quay tương đương = gia số góc = vận tốc góc * dt

for i in range(N):
    C_m2m_1 = ch_rv2m(theta)
    Cb2n = Cb2n.dot(C_m2m_1)
    Cb2n = ch_mnormlz(Cb2n)
    # a, b, c = ch_m2eul_312(Cb2n)
    # print("Quaternion to Euler angles: %.3f %.3f %.3f " % (np.rad2deg(a), np.rad2deg(b), np.rad2deg(c)))
    eul[i,:] = np.rad2deg(ch_m2eul_312(Cb2n))

import matplotlib.pyplot as plt
plt.plot(eul)
ax = plt.subplot()
ax.legend(["PITCH(deg)", "ROLL(deg)", "YAW(deg)"])
plt.show()

# def ch_rv2q(rv):
#     nm2 = rv.dot(rv)
#     if nm2 < 1.e-8:
#         q0 = 1-nm2*(1/8-nm2/384)
#         s = 1/2-nm2*(1/48-nm2/3840)
#     else:
#         nm = np.sqrt(nm2)
#         q0 = cos(nm/2)
#         s = sin(nm/2)/nm
#     q = np.concatenate([[q0],s*rv])
#     return q
#
# def ch_qmul(q1, q2):
#     q = np.array([ q1[0] * q2[0] - q1[1] * q2[1] - q1[2] * q2[2] - q1[3] * q2[3],
#                    q1[0] * q2[1] + q1[1] * q2[0] + q1[2] * q2[3] - q1[3] * q2[2],
#                    q1[0] * q2[2] + q1[2] * q2[0] + q1[3] * q2[1] - q1[1] * q2[3],
#                    q1[0] * q2[3] + q1[3] * q2[0] + q1[1] * q2[2] - q1[2] * q2[1] ], dtype=np.float64)
#     return q
#
# from numpy.linalg import norm
# def ch_qnormlz(q):
#     q = q / norm(q,2)
#     if q[0] < 0:
#         q[0] = -q[0]
#         q[1] = -q[1]
#         q[2] = -q[2]
#         q[3] = -q[3]
#     return q
#
# def ch_q2m(Qb2n):
#     q11 = Qb2n[0]*Qb2n[0]; q12 = Qb2n[0]*Qb2n[1]; q13 = Qb2n[0]*Qb2n[2]; q14 = Qb2n[0]*Qb2n[3]
#     q22 = Qb2n[1]*Qb2n[1]; q23 = Qb2n[1]*Qb2n[2]; q24 = Qb2n[1]*Qb2n[3]
#     q33 = Qb2n[2]*Qb2n[2]; q34 = Qb2n[2]*Qb2n[3]
#     q44 = Qb2n[3]*Qb2n[3]
#     Cb2n = np.array([[ q11+q22-q33-q44,  2*(q23-q14),     2*(q24+q13)],
#                      [2*(q23+q14),      q11-q22+q33-q44, 2*(q34-q12)],
#                      [2*(q24-q13),      2*(q34+q12),     q11-q22-q33+q44 ]], dtype=np.float64)
#     return Cb2n
#
#
# w = np.array([2, -3, 5])
# dt = 0.01  # Thời gian cập nhật thái độ: 0,01 giây = 100Hz
# dur = 100  # Thời lượng duration
#
# N = int(dur / dt)  # điểm points
# eul_ = np.zeros((N, 3), dtype=np.float64)
# # vận tốc góc hệ b (đầu ra con quay hồi chuyển)
# print("Angular velocity (gyro output is): %.3fdeg/s %.3fdeg/s %.3fdeg/s\n" % (w[0], w[1], w[2]))
#
# Qb2n = np.array([1, 0, 0, 0])
# theta = np.deg2rad(w) * dt  # Theo trục quay cố định: Vectơ quay tương đương = gia số góc = vận tốc góc * dt
#
# for i in range(N):
#     Q_m2m_1 = ch_rv2q(theta)
#     Qb2n = ch_qmul(Qb2n, Q_m2m_1)
#
#     # Quaternion unitization
#     Qb2n = ch_qnormlz(Qb2n)
#     Cb2n = ch_q2m(Qb2n)
#     eul_[i, :] = np.rad2deg(ch_m2eul_312(Cb2n))
#     # eul[i,:] = np.rad2deg(ch_q2eul(Qb2n))
#
# import matplotlib.pyplot as plt
# plt.plot(eul_)
# ax = plt.subplot()
# ax.legend(["PITCH(deg)", "ROLL(deg)", "YAW(deg)"])
# plt.show()