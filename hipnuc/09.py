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
pi = np.pi

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

from numpy.linalg import norm
def ch_mnormlz(q):
    q = q / norm(q,2)
    if q[0][0] < 0:
        q = -q
    return q

def ch_m2eul_321(Cb2n):
    beta = atan2(Cb2n[2,1], Cb2n[2,2])
    alpha = asin(-Cb2n[2,0])
    gamma = atan2(Cb2n[1,0],Cb2n[0,0])
    return beta, alpha, gamma

w = np.array([2, -3, 5])
dt = 0.01
dur = 100
N = int(dur / dt)
eul = np.zeros((N, 3), dtype=np.float64)
# print("已知b系角速度(陀螺仪输出为):%.3fdeg/s %.3fdeg/s %.3fdeg/s\n" %(w[0], w[1], w[2]))
print("Angular velocity (gyro output is): %.3fdeg/s %.3fdeg/s %.3fdeg/s\n" %(w[0], w[1], w[2]))

Cb2n = np.identity(3)   #eye(3)
theta = np.deg2rad(w)*dt   #gia tốc góc = vận tốc góc * dt
print(theta)

# for i in range(N):
for i in range(1000):
    # print(i)
    C_m2m_1 = ch_rv2m(theta)
    # print(C_m2m_1)
    Cb2n = Cb2n.dot(C_m2m_1)
    # print(Cb2n)
    Cb2n = ch_mnormlz(Cb2n)
    # print(Cb2n)
    # a, b, c = np.rad2deg(ch_m2eul_321(Cb2n))
    a, b, c = ch_m2eul_321(Cb2n)
    # print("Quaternion to Euler angles:\n %.3f %.3f %.3f " % (a / pi * 180, b / pi * 180, c / pi * 180))
    print("Quaternion to Euler angles: %.3f %.3f %.3f " % (a / pi * 180, b / pi * 180, c / pi * 180))
    # break
# for i = 1:N
# C_m2m_1 = ch_rv2m(theta);
# Cb2n = Cb2n * C_m2m_1;
#
# % 单位阵正交化
# Cb2n = ch_mnormlz(Cb2n);
#
# % 记录每一步的欧拉角
# eul(i,:) = rad2deg(ch_m2eul(Cb2n));
# end