import numpy as np

'''
unction qout = ch_qconj(qin)
% 四元数取逆
qout = [qin(1); -qin(2:4)];
'''
def ch_qconj(qin):
    # return [qin[0], -qin[1:3]]
    return np.concatenate([[qin[0]], -qin[1:]])

'''
function q = ch_qnormlz(q)
% 四元数归一化
    q = q/norm(q);
    if(q(1)<0)
        q(1) = -q(1);
        q(2) = -q(2);
        q(3) = -q(3);
        q(4) = -q(4);
    end
'''
from numpy.linalg import norm   #norm(V,2)

def ch_qnormlz(q):
    q = q / norm(q,2)
    if q[0] < 0:
        q[0] = -q[0]
        q[1] = -q[1]
        q[2] = -q[2]
        q[3] = -q[3]
    return q

'''
function q = ch_qmul(q1, q2)
% 四元数相乘
%
% Inputs: Q1 Q2, 四元数和矩阵一样，不满足交换律
% Outputs: Q
%
    q = [ q1(1) * q2(1) - q1(2) * q2(2) - q1(3) * q2(3) - q1(4) * q2(4);
          q1(1) * q2(2) + q1(2) * q2(1) + q1(3) * q2(4) - q1(4) * q2(3);
          q1(1) * q2(3) + q1(3) * q2(1) + q1(4) * q2(2) - q1(2) * q2(4);
          q1(1) * q2(4) + q1(4) * q2(1) + q1(2) * q2(3) - q1(3) * q2(2) ];
'''
def ch_qmul(q1, q2):
    q = np.array([ q1[0] * q2[0] - q1[1] * q2[1] - q1[2] * q2[2] - q1[3] * q2[3],
                   q1[0] * q2[1] + q1[1] * q2[0] + q1[2] * q2[3] - q1[3] * q2[2],
                   q1[0] * q2[2] + q1[2] * q2[0] + q1[3] * q2[1] - q1[1] * q2[3],
                   q1[0] * q2[3] + q1[3] * q2[0] + q1[1] * q2[2] - q1[2] * q2[1] ], dtype=np.float64)
    return q

'''
function Cb2n = ch_q2m(Qb2n)
% 四元数转姿态阵
%
% Input: Qb2n
% Output: Cb2n
%
    q11 = Qb2n(1)*Qb2n(1); q12 = Qb2n(1)*Qb2n(2); q13 = Qb2n(1)*Qb2n(3); q14 = Qb2n(1)*Qb2n(4); 
    q22 = Qb2n(2)*Qb2n(2); q23 = Qb2n(2)*Qb2n(3); q24 = Qb2n(2)*Qb2n(4);     
    q33 = Qb2n(3)*Qb2n(3); q34 = Qb2n(3)*Qb2n(4);  
    q44 = Qb2n(4)*Qb2n(4);
    Cb2n = [ q11+q22-q33-q44,  2*(q23-q14),     2*(q24+q13);
            2*(q23+q14),      q11-q22+q33-q44, 2*(q34-q12);
            2*(q24-q13),      2*(q34+q12),     q11-q22-q33+q44 ];
'''
def ch_q2m(Qb2n):
    q11 = Qb2n[0]*Qb2n[0]; q12 = Qb2n[0]*Qb2n[1]; q13 = Qb2n[0]*Qb2n[2]; q14 = Qb2n[0]*Qb2n[3]
    q22 = Qb2n[1]*Qb2n[1]; q23 = Qb2n[1]*Qb2n[2]; q24 = Qb2n[1]*Qb2n[3]
    q33 = Qb2n[2]*Qb2n[2]; q34 = Qb2n[2]*Qb2n[3]
    q44 = Qb2n[3]*Qb2n[3]
    Cb2n = np.array([[ q11+q22-q33-q44,  2*(q23-q14),     2*(q24+q13)],
                     [2*(q23+q14),      q11-q22+q33-q44, 2*(q34-q12)],
                     [2*(q24-q13),      2*(q34+q12),     q11-q22-q33+q44 ]], dtype=np.float64)
    return Cb2n

'''
function Qb2n = ch_m2q(Cb2n)
% 姿态阵转四元数
%
% Input: Cb2n
% Output: Qb2n
%
    C11 = Cb2n(1,1); C12 = Cb2n(1,2); C13 = Cb2n(1,3); 
    C21 = Cb2n(2,1); C22 = Cb2n(2,2); C23 = Cb2n(2,3); 
    C31 = Cb2n(3,1); C32 = Cb2n(3,2); C33 = Cb2n(3,3); 
    if C11>=C22+C33
        q1 = 0.5*sqrt(1+C11-C22-C33);
        q0 = (C32-C23)/(4*q1); q2 = (C12+C21)/(4*q1); q3 = (C13+C31)/(4*q1);
    elseif C22>=C11+C33
        q2 = 0.5*sqrt(1-C11+C22-C33);
        q0 = (C13-C31)/(4*q2); q1 = (C12+C21)/(4*q2); q3 = (C23+C32)/(4*q2);
    elseif C33>=C11+C22
        q3 = 0.5*sqrt(1-C11-C22+C33);
        q0 = (C21-C12)/(4*q3); q1 = (C13+C31)/(4*q3); q2 = (C23+C32)/(4*q3);
    else
        q0 = 0.5*sqrt(1+C11+C22+C33);
        q1 = (C32-C23)/(4*q0); q2 = (C13-C31)/(4*q0); q3 = (C21-C12)/(4*q0);
    end
    Qb2n = [q0; q1; q2; q3];
'''

def ch_m2q(Cb2n):
    C11 = Cb2n[0,0]; C12 = Cb2n[0,1]; C13 = Cb2n[0,2]
    C21 = Cb2n[1,0]; C22 = Cb2n[1,1]; C23 = Cb2n[1,2]
    C31 = Cb2n[2,0]; C32 = Cb2n[2,1]; C33 = Cb2n[2,2]

    if C11 >= C22+C33:
        q1 = 0.5*np.sqrt(1+C11-C22-C33)
        q0 = (C32-C23)/(4*q1); q2 = (C12+C21)/(4*q1); q3 = (C13+C31)/(4*q1)
    elif C22>= C11+C33:
        q2 = 0.5*np.sqrt(1-C11+C22-C33)
        q0 = (C13-C31)/(4*q2); q1 = (C12+C21)/(4*q2); q3 = (C23+C32)/(4*q2)
    elif C33>=C11+C22:
        q3 = 0.5*np.sqrt(1-C11-C22+C33)
        q0 = (C21-C12)/(4*q3); q1 = (C13+C31)/(4*q3); q2 = (C23+C32)/(4*q3)
    else:
        q0 = 0.5*np.sqrt(1+C11+C22+C33)
        q1 = (C32-C23)/(4*q0); q2 = (C13-C31)/(4*q0); q3 = (C21-C12)/(4*q0)
    Qb2n = np.array([q0, q1, q2, q3], dtype=np.float64)
    return Qb2n

Qb2n = np.array([0.981, 0.010, -0.191, 0.011])
Cb2n = ch_q2m(Qb2n)
# print("Qb2n四元数转姿态阵Cb2n: ", Cb2n)
print("Qb2n Quaternion to Attitude Array Cb2n\n", Cb2n)
# [[ 0.925859 -0.025402 -0.374522]
#  [ 0.017762  0.998621 -0.023822]
#  [ 0.374962  0.015418  0.925901]]

Qb2n = ch_m2q(Cb2n)
# print("姿态阵Cb2n转四元数Qb2n", Qb2n)
print("Attitude array Cb2n to quaternion Qb2n", Qb2n)
# [ 0.98111939  0.00999878 -0.19097676  0.01099866]

'''
function vout = ch_qmulv(q, vin)
% 向量通过四元数做3D旋转
% 
% Inputs: q - Qb2n
%            vi - 需要旋转的向量
% Output: vout - output vector, such that vout = q*vin*conjugation(q)
% 
% See also  q2mat, qconj, qmul.
    qi = [0; vin];
    qo = ch_qmul(ch_qmul(q,qi),ch_qconj(q));
    vout = qo(2:4,1);
'''
def ch_qmulv(q, vin):
    # qi = [0, vin]
    qi = np.concatenate([[0], vin])
    qo = ch_qmul(ch_qmul(q,qi),ch_qconj(q))
    # [0.00000000e+00 1.02681000e-03 7.46187000e-04 9.97285995e-01]
    vout = qo[1:]
    return vout

print("\nTest 1: b2n conversion")
Qb2n = np.array([0.919, 0.262,  -0.09, -0.282])

# accReading: 静止下加速度计读值, 相当于b系下的静止加速度值(b系下的三维向量)
# accReading: The reading value of the accelerometer at rest, which is equivalent to the static acceleration value under the b system (three-dimensional vector under the b system)
accReading = np.array([0.018, 0.531,  0.843])

Cb2n = ch_q2m(Qb2n)
Gn = Cb2n.dot(accReading)
# print("eg1: b系加速度通过Cb2n读值转到n系，结果: %.3f %.3f %.3f 可以看到接近于 0 0 1"%(Gn[0], Gn[1], Gn[2]))
print("eg1: The acceleration of the b system is transferred to the n system through the Cb2n reading, \nthe result: %.3f %.3f %.3f It can be seen that it is close to 0 0 1" %(Gn[0], Gn[1], Gn[2]))
# print(Gn)
Gn = ch_qmulv(Qb2n, accReading)
# print("eg2: 使用四元数转accReading，可以得到相同结果：  %.3f %.3f %.3f "%(Gn[0], Gn[1], Gn[2]))
print("eg2: Use Quaternion to accReading, you can get the same result: %.3f %.3f %.3f " %(Gn[0], Gn[1], Gn[2]))

'''
Gn = [0 0 1]'; %Gn: 静止下，N系下加速度值，应该是静止下的比力(和重力大小相等，方向相反):
Qn2b = ch_qconj(Qb2n);
Cn2b = ch_q2m(Qn2b);

accB =  Cn2b*Gn;
fprintf("eg1: (0 0 1)转到b系,结果: %.3f %.3f %.3f 接近于 accReading: %.3f %.3f %.3f\n", accB(1), accB(2), accB(3), accReading(1), accReading(2), accReading(3));

accB = ch_qmulv(Qn2b, Gn);
fprintf("eg2: 使用四元数旋转函数，可以得到相同结果：  
'''
print("\nTest 2: n2b conversion")
Gn = np.array([0, 0, 1])
Qn2b = ch_qconj(Qb2n)
Cn2b = ch_q2m(Qn2b)

accB = Cn2b.dot(Gn)
print("eg1: (0 0 1)转到b系,结果: %.3f %.3f %.3f 接近于 accReading: %.3f %.3f %.3f" %(accB[0], accB[1], accB[2], accReading[0], accReading[1], accReading[2]))
# eg1: (0 0 1)转到b系,结果: 0.018 0.532 0.847 接近于 accReading: 0.018 0.531 0.843

accB = ch_qmulv(Qn2b, Gn)
print("eg2: 使用四元数旋转函数，可以得到相同结果：  %.3f %.3f %.3f " %(accB[0], accB[1], accB[2]))
# eg2: 使用四元数旋转函数，可以得到相同结果：  0.018 0.532 0.847




