'''
function [Cb2n_312, Cb2n_321] = ch_eul2m(att)
% 将欧拉角转换为姿态阵
% 复用严龚敏老师的a2mat
%
% Input: att  单位：rad
% 对于312((Z->X->Y))顺序，对应att = [pitch(绕X轴) roll(绕Y轴)  yaw(绕Z轴)]
% 对于3211(Z->Y->X)顺序，对应att = [roll(绕X轴) pitch(绕Y轴)  yaw(绕Z轴)]
% Outputs:
% Cb2n_312:  312欧拉角顺序下转换后的Cb2n
% Cb2n_321:  321欧拉角顺序下转换后的Cb2n

    s = sin(att); c = cos(att);
    si = s(1); sj = s(2); sk = s(3);
    ci = c(1); cj = c(2); ck = c(3);
    Cb2n_312 = [ cj*ck-si*sj*sk, -ci*sk,  sj*ck+si*cj*sk;
            cj*sk+si*sj*ck,  ci*ck,  sj*sk-si*cj*ck;
           -ci*sj,           si,     ci*cj           ];
    if nargout==2  % dual Euler angle DCM
        Cb2n_321 = [ cj*ck, si*sj*ck-ci*sk, ci*sj*ck+si*sk;
                 cj*sk, si*sj*sk+ci*ck, ci*sj*sk-si*ck;
                -sj,    si*cj,          ci*cj            ];
    end
'''

import numpy as np
sin = np.sin
cos = np.cos
pi = np.pi
asin = np.arcsin
atan2 = np.arctan2

eul_312 = [30, 40, 50]  # [pitch(绕X轴) roll(绕Y轴)  yaw(绕Z轴)]

# def ch_rotx(i):
#     theta = pi * i / 180
#     return np.array([[1, 0, 0],
#                      [0, cos(theta), -sin(theta)],
#                      [0, sin(theta), cos(theta)]])
#
# def ch_roty(i):
#     theta = pi * i / 180
#     return np.array([[cos(theta), 0, sin(theta)],
#                      [0, 1, 0],
#                      [-sin(theta), 0, cos(theta)]])
#
# def ch_rotz(i):
#     theta = pi * i / 180
#     return np.array([[cos(theta), -sin(theta), 0],
#                      [sin(theta), cos(theta), 0],
#                      [0, 0, 1]])

def ch_eul2m(i):
    alpha = pi * i[2] / 180     # (Alpha Z)
    beta = pi * i[0] / 180      # (Beta X)
    gamma = pi * i[1] / 180     # (Gamma Y)

    s_z_alpha = sin(alpha); s_x_beta = sin(beta); s_y_gamma = sin(gamma)
    c_z_alpha = cos(alpha); c_x_beta = cos(beta); c_y_gamma = cos(gamma)

    # Cb2n_312
    # rotz * rotx * roty
    # Cb2n_312 = [ cj*ck-si*sj*sk, -ci*sk,  sj*ck+si*cj*sk;
    #         cj*sk+si*sj*ck,  ci*ck,  sj*sk-si*cj*ck;
    #        -ci*sj,           si,     ci*cj           ];
    #i = beta   j = gamma    k = alpha
    # Cb2n_312 = np.array([[c_z_alpha*c_y_gamma - s_z_alpha*s_x_beta*s_y_gamma, -s_z_alpha*c_x_beta, c_z_alpha*s_y_gamma + s_z_alpha*s_x_beta*c_y_gamma],
    #                      [s_z_alpha*c_y_gamma + c_z_alpha*s_x_beta*s_y_gamma, c_z_alpha*c_x_beta, s_z_alpha*s_y_gamma - c_z_alpha*s_x_beta*c_y_gamma],
    #                      [-c_x_beta*s_y_gamma, s_x_beta, c_x_beta*c_y_gamma]])

    Cb2n_312 = np.array([[ c_y_gamma*c_z_alpha-s_x_beta*s_y_gamma*s_z_alpha, -c_x_beta*s_z_alpha,  s_y_gamma*c_z_alpha+s_x_beta*c_y_gamma*s_z_alpha],
                         [c_y_gamma*s_z_alpha+s_x_beta*s_y_gamma*c_z_alpha,  c_x_beta*c_z_alpha,  s_y_gamma*s_z_alpha-s_x_beta*c_y_gamma*c_z_alpha],
                         [-c_x_beta*s_y_gamma,           s_x_beta,     c_x_beta*c_y_gamma           ]])
    # if nargout==2  % dual Euler angle DCM
    Cb2n_321 = np.array([[ c_y_gamma*c_z_alpha, s_x_beta*s_y_gamma*c_z_alpha-c_x_beta*s_z_alpha, c_x_beta*s_y_gamma*c_z_alpha+s_x_beta*s_z_alpha],
                         [c_y_gamma*s_z_alpha, s_x_beta*s_y_gamma*s_z_alpha+c_x_beta*c_z_alpha, c_x_beta*s_y_gamma*s_z_alpha-s_x_beta*c_z_alpha],
                         [-s_y_gamma,    s_x_beta*c_y_gamma,          c_x_beta*c_y_gamma            ]])

    # print(Cb2n_312)
    # [[0.24620194 - 0.66341395  0.70658796]
    #  [0.79341204  0.5566704   0.24620194]
    # [-0.5566704    0.5    0.66341395]]
    # print(Cb2n_321)
    # [[0.49240388 - 0.45682599  0.74084306]
    #  [0.58682409  0.80287234  0.10504046]
    # [-0.64278761    0.38302222    0.66341395]]

    return Cb2n_312, Cb2n_321

m_312, m_321 = ch_eul2m(eul_312)

'''
function [eul_312, eul_321] = ch_m2eul(Cb2n)
% 将姿态阵转为欧拉角
% 复用严龚敏老师的m2att
%
% Input: 姿态阵 b->n系的坐标变换矩阵
% Outputs: 
% att:   312(Z->X->Y)旋转顺序下的欧拉角:  att = [pitch(绕X轴) roll(绕Y轴) yaw(绕Z轴)]
% attr:  321(Z->Y->X)旋转顺序下的欧拉角:  att = [roll(绕X轴) pitch(绕Y轴)  yaw(绕Z轴)]
    eul_312 = [ asin(Cb2n(3,2));
            atan2(-Cb2n(3,1),Cb2n(3,3)); 
            atan2(-Cb2n(1,2),Cb2n(2,2)) ];
    if nargout==2  % dual Euler angles
        eul_321 = [ atan2(Cb2n(3,2),Cb2n(3,3)); 
                 asin(-Cb2n(3,1)); 
                 atan2(Cb2n(2,1),Cb2n(1,1)) ];
    end
'''

# alpha = pi * i[2] / 180  # (Alpha Z)
# beta = pi * i[0] / 180  # (Beta X)
# gamma = pi * i[1] / 180  # (Gamma Y)

def ch_m2eul_312(Cb2n):
    print(Cb2n)
    beta = asin(Cb2n[2,1])
    alpha = atan2(-Cb2n[2,0], Cb2n[2,2])
    gamma = atan2(-Cb2n[0,1], Cb2n[1,1])
    return beta, alpha, gamma

def ch_m2eul_321(Cb2n):
    print(Cb2n)
    beta = atan2(Cb2n[2,1], Cb2n[2,2])
    alpha = asin(-Cb2n[2,0])
    gamma = atan2(Cb2n[1,0],Cb2n[0,0])
    return beta, alpha, gamma

a,b,c = ch_m2eul_312(m_312)
print(a / pi * 180,
      b / pi * 180,
      c / pi * 180)

a,b,c = ch_m2eul_321(m_321)
print(a / pi * 180,
      b / pi * 180,
      c / pi * 180)



    # Cb2n_321
    # rotz * roty * rotx
    # Cb2n_321 =

# def Cb2n_321(i):
#     pass