import numpy as np
cos = np.cos
sin = np.sin
asin = np.arcsin
atan2 = np.arctan2
from numpy.linalg import norm

def ch_qnormlz(q):
    q = q / norm(q,2)
    if q[0] < 0:
        q[0] = -q[0]
        q[1] = -q[1]
        q[2] = -q[2]
        q[3] = -q[3]
    return q

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
'''
function out = ch_att_upt(in, gyr, dt)

%% 单子样旋转矢量
 rv = gyr*dt;
 dq = ch_rv2q(rv);

%% 不专业的做法
%                  dq(1) = 1;
%                  dq(2) = rv(1)*0.5;
%                  dq(3) = rv(2)*0.5;
%                  dq(4) = rv(3)*0.5;

 out = ch_qmul(in, dq);
 out = ch_qnormlz(out);

%% 使用旋转矩阵更新
% 
%  Cb2n = ch_q2m(in);
%  theta = gyr*dt;
% 
% %C = eye(3) + ch_askew(theta);
% C = ch_rv2m(theta);
% 
% Cb2n = Cb2n * C;
% 
% % 截断误差，保持正交化 GNSS与惯性及多传感器组合导航系统原理-第二版.pdf 公式 5.80
% c1 = Cb2n(1,:);
% c2 = Cb2n(2,:);
% c3 = Cb2n(3,:);
% c1 = 2 / (1 + dot(c1,c1))*c1;
% c2 = 2 / (1 + dot(c2,c2))*c2;
% c3 = 2 / (1 + dot(c3,c3))*c3;
% Cb2n = [c1; c2; c3];
% 
% out = ch_m2q(Cb2n);
end
'''
def ch_att_upt(in_, gyr, dt):
    rv = gyr * dt
    dq = ch_rv2q(rv)
    out = ch_qmul(in_, dq)
    out = ch_qnormlz(out)
    return out

def ch_qconj(qin):
    # return [qin[0], -qin[1:3]]
    return np.concatenate([[qin[0]], -qin[1:]])

def ch_qmulv(q, vin):
    # qi = [0, vin]
    qi = np.concatenate([[0], vin])
    qo = ch_qmul(ch_qmul(q,qi),ch_qconj(q))
    # [0.00000000e+00 1.02681000e-03 7.46187000e-04 9.97285995e-01]
    vout = qo[1:]
    return vout
'''
function [p, v, q] = ch_nav_equ_local_tan(p, v, q ,acc, gyr, dt, gN)
%  惯导解算更新，当地直角坐标系，不考虑地球重力
% p         位置 XYZ 单位 m
% v          速度 XYZ 单位 m/s
% q         Qb2n姿态,四元数表示
% acc      比力， 加速度计测量值 单位  (m/s^2), 
% gyr      角速度 (rad/s)]
% dt        dt (s) 积分间隔如 0.01s
% gn       当地重力向量

old_v = v;

sf = acc;

%  姿态结算
q = ch_att_upt(q, gyr, dt);


% 速度解算
sf = ch_qmulv(q, sf);
sf = sf + gN;
v = old_v + dt *sf;

% 位置解算
p = p + (old_v + v) *dt/2;

end
'''
def ch_nav_equ_local_tan(p, v, q ,acc, gyr, dt, gN):
    old_v = v
    sf = acc
    q = ch_att_upt(q, gyr, dt)

    sf = ch_qmulv(q, sf)
    sf = sf + gN
    v = old_v + dt * sf

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

Fs = 100
N = Fs*10

gyr = np.array([0.1, 0.2, 0.3])
acc = np.array([0, 0, 1])

acc = acc * 9.795
gyr = np.deg2rad(gyr)

# eul = np.zeros((N, 3), dtype=np.float64)
p = np.zeros((3), dtype=np.float64)   # p = zeros(3, 1);
v = np.zeros((3), dtype=np.float64)   # v = zeros(3, 1);
q= np.array([1, 0, 0, 0])

pos = np.zeros((N, 3), dtype=np.float64)
eul = np.zeros((N, 3), dtype=np.float64)

for i in range(N):
    p ,v, q = ch_nav_equ_local_tan(p, v, q, acc.T, gyr.T, 1 / Fs, np.array([0, 0, -9.795]).T)
    pos[i, :] = p

    # eul(i,:) = np.rad2deg(ch_q2eul(q))
    eul[i, :] = np.rad2deg(ch_q2eul_312(q))

print('纯积分测试: 陀螺bias(rad):%.3f %.3f %.3f\n' %(gyr[0], gyr[1], gyr[2]))
# 纯积分测试: 陀螺bias(rad):0.002 0.003 0.005

print('纯积分测试: 加计bias(m/s^(2)):%.3f %.3f %.3f\n' %(acc[0], acc[1], acc[2]))
# 纯积分测试: 加计bias(m/s^(2)):0.000 0.000 9.795

print('解算:%d次 总时间:%.3fs\n' %(N, N /Fs))
# 解算:1000次 总时间:10.000s

print('最终误差(m): %.3f %.3f %.3f\n' %(pos[N-1, 0],  pos[N-1, 1],  pos[N-1, 2]))
# 最终误差(m): 5.743 -2.778 -0.062

import matplotlib.pyplot as plt

plt.figure()
plt.subplot(211)
plt.plot(pos)
# ax = plt.subplot()
# ax.legend(["X", "Y", "Z"])

plt.subplot(212)
plt.plot(eul)
# ax = plt.subplot()
# ax.legend(["PITCH(deg)", "ROLL(deg)", "YAW(deg)"])

plt.show()

# plt.plot(pos)
# ax = plt.subplot()
# ax.legend(["X", "Y", "Z"])
#
# plt.plot(eul)
# ax = plt.subplot()
# ax.legend(["PITCH(deg)", "ROLL(deg)", "YAW(deg)"])
# plt.show()

