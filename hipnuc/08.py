import numpy as np
pi = np.pi
sin = np.sin
cos = np.cos

# ------------------------- Exercises1: ------------------------------
# def ch_eul2m(i):
#     alpha = pi * i[2] / 180     # (Alpha Z)
#     beta = pi * i[0] / 180      # (Beta X)
#     gamma = pi * i[1] / 180     # (Gamma Y)
#
#     s_z_alpha = sin(alpha); s_x_beta = sin(beta); s_y_gamma = sin(gamma)
#     c_z_alpha = cos(alpha); c_x_beta = cos(beta); c_y_gamma = cos(gamma)
#
#     Cb2n_312 = np.array([[ c_y_gamma*c_z_alpha-s_x_beta*s_y_gamma*s_z_alpha, -c_x_beta*s_z_alpha,  s_y_gamma*c_z_alpha+s_x_beta*c_y_gamma*s_z_alpha],
#                          [c_y_gamma*s_z_alpha+s_x_beta*s_y_gamma*c_z_alpha,  c_x_beta*c_z_alpha,  s_y_gamma*s_z_alpha-s_x_beta*c_y_gamma*c_z_alpha],
#                          [-c_x_beta*s_y_gamma,           s_x_beta,     c_x_beta*c_y_gamma           ]])
#
#     Cb2n_321 = np.array([[ c_y_gamma*c_z_alpha, s_x_beta*s_y_gamma*c_z_alpha-c_x_beta*s_z_alpha, c_x_beta*s_y_gamma*c_z_alpha+s_x_beta*s_z_alpha],
#                          [c_y_gamma*s_z_alpha, s_x_beta*s_y_gamma*s_z_alpha+c_x_beta*c_z_alpha, c_x_beta*s_y_gamma*s_z_alpha-s_x_beta*c_z_alpha],
#                          [-s_y_gamma,    s_x_beta*c_y_gamma,          c_x_beta*c_y_gamma            ]])
#
#     return Cb2n_312, Cb2n_321
#
#
# eul321 = np.array([-30, 30, 45])
# # print("已知欧拉角(321顺序)为:\n", eul321)
# print("Euler angles (321):\n", eul321)
# # [-30  30  45]
#
# _, Cb2n = ch_eul2m(eul321)
# # print("欧拉角转姿态阵Cb2n:\n", Cb2n)
# print("Euler angle rotation attitude matrix Cb2n:\n", Cb2n)
# # [[ 0.61237244 -0.78914913 -0.04736717]
# #  [ 0.61237244  0.43559574  0.65973961]
# #  [-0.5        -0.4330127   0.75      ]]
#
# def ch_m2q(Cb2n):
#     C11 = Cb2n[0,0]; C12 = Cb2n[0,1]; C13 = Cb2n[0,2]
#     C21 = Cb2n[1,0]; C22 = Cb2n[1,1]; C23 = Cb2n[1,2]
#     C31 = Cb2n[2,0]; C32 = Cb2n[2,1]; C33 = Cb2n[2,2]
#
#     if C11 >= C22+C33:
#         q1 = 0.5*np.sqrt(1+C11-C22-C33)
#         q0 = (C32-C23)/(4*q1); q2 = (C12+C21)/(4*q1); q3 = (C13+C31)/(4*q1)
#     elif C22>= C11+C33:
#         q2 = 0.5*np.sqrt(1-C11+C22-C33)
#         q0 = (C13-C31)/(4*q2); q1 = (C12+C21)/(4*q2); q3 = (C23+C32)/(4*q2)
#     elif C33>=C11+C22:
#         q3 = 0.5*np.sqrt(1-C11-C22+C33)
#         q0 = (C21-C12)/(4*q3); q1 = (C13+C31)/(4*q3); q2 = (C23+C32)/(4*q3)
#     else:
#         q0 = 0.5*np.sqrt(1+C11+C22+C33)
#         q1 = (C32-C23)/(4*q0); q2 = (C13-C31)/(4*q0); q3 = (C21-C12)/(4*q0)
#     Qb2n = np.array([q0, q1, q2, q3], dtype=np.float64)
#     return Qb2n
#
# Qb2n = ch_m2q(Cb2n)
# # print("欧拉角转四元数:\n", Qb2n)
# print("Euler angle to quaternion:\n", Qb2n)
# # [0.83635641 - 0.32664074  0.13529903  0.4189367]
#
# # ------------------------- Exercises2: ------------------------------
atan2 = np.arctan2
asin = np.arcsin
pi = np.pi
#
# Cb2n = np.array([[0.612372, -0.78915, -0.04737],
#                  [0.612372, 0.435596, 0.65974],
#                  [-0.5, -0.43301, 0.75]], dtype=np.float64)
#
# # print("已知姿态阵Cb2n:\n", Cb2n)
# print("attitude array Cb2n:\n", Cb2n)
# # [[0.612372 - 0.78915 - 0.04737]
# #  [0.612372  0.435596  0.65974]
# # [-0.5 - 0.43301 0.75]]
#
# np.set_printoptions(suppress=True)
# # print("姿态阵乘以自己的转置=单位阵。想想为什么？>~\n", Cb2n.dot(Cb2n.T))
# print("Attitude matrix multiplied by own transpose = unit matrix. Think about why?>~\n", Cb2n.dot(Cb2n.T))
# # [[1.00000111 - 0.000003 - 0.00000366]
# #  [-0.000003    1.00000021  0.00000158]
# # [-0.00000366 0.00000158 0.99999766]]
#
def ch_m2eul_321(Cb2n):
    beta = atan2(Cb2n[2,1], Cb2n[2,2])
    alpha = asin(-Cb2n[2,0])
    gamma = atan2(Cb2n[1,0],Cb2n[0,0])
    return beta, alpha, gamma
#
# a,b,c = ch_m2eul_321(Cb2n)
# # print("姿态阵转欧拉角:\n %.3f %.3f %.3f " %(a/pi * 180, b/pi * 180, c/pi * 180))
# print("Attitude array to Euler angle:\n %.3f %.3f %.3f " %(a/pi * 180, b/pi * 180, c/pi * 180))
# # -30.000 30.000 45.000
#
# Qb2n = ch_m2q(Cb2n)
# # print("欧拉角转四元数:\n", Qb2n)
# print("Euler angle to quaternion:\n", Qb2n)
# # [0.83635638 - 0.32664006  0.13529818  0.41893684]

# ------------------------- Exercises3: ------------------------------
Qb2n = np.array([0.836356, -0.32664, 0.135299, 0.418937])
# print("已知四元数Qb2n:\n", Qb2n)
print("quaternion Qb2n:\n", Qb2n)
# [0.836356 - 0.32664   0.135299  0.418937]

def ch_q2m(Qb2n):
    q11 = Qb2n[0]*Qb2n[0]; q12 = Qb2n[0]*Qb2n[1]; q13 = Qb2n[0]*Qb2n[2]; q14 = Qb2n[0]*Qb2n[3]
    q22 = Qb2n[1]*Qb2n[1]; q23 = Qb2n[1]*Qb2n[2]; q24 = Qb2n[1]*Qb2n[3]
    q33 = Qb2n[2]*Qb2n[2]; q34 = Qb2n[2]*Qb2n[3]
    q44 = Qb2n[3]*Qb2n[3]
    Cb2n = np.array([[ q11+q22-q33-q44,  2*(q23-q14),     2*(q24+q13)],
                     [2*(q23+q14),      q11-q22+q33-q44, 2*(q34-q12)],
                     [2*(q24-q13),      2*(q34+q12),     q11-q22-q33+q44 ]], dtype=np.float64)
    return Cb2n

Cb2n = ch_q2m(Qb2n)
# print("Qb2n四元数转姿态阵Cb2n: ", Cb2n)
print("Qb2n Quaternion to Attitude Array Cb2n\n", Cb2n)
# [[0.61237102 - 0.78914908 - 0.0473669]
#  [0.61237282  0.43559528  0.65973816]
# [-0.49999942 - 0.43301113 0.75000006]]

a,b,c = ch_m2eul_321(Cb2n)
# print("四元数转欧拉角:\n %.3f %.3f %.3f " %(a/pi * 180, b/pi * 180, c/pi * 180))
print("Quaternion to Euler angles:\n %.3f %.3f %.3f " %(a/pi * 180, b/pi * 180, c/pi * 180))
# -30.000 30.000 45.000