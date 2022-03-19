import numpy as np

# V1 = np.array([0.8147, 0.3249, 0.2462]).T
# V2 = np.array([0.3427, 0.3757, 0.5466]).T
#
# '''
# function m = ch_askew(v)
# % 生成反对称矩阵
# %
# % Input: v - 3x1 vector
# % Output: m - v的反对称阵
# %                    |  0   -v(3)  v(2) |
# %             m = | v(3)  0    -v(1) |
# %                    |-v(2)  v(1)  0    |
#     m = [ 0,     -v(3),   v(2);
#           v(3),   0,     -v(1);
#          -v(2),   v(1),   0     ];
# '''
#
def ch_askew(v):
    m = np.array([[0,     -v[2],   v[1]],
                  [v[2],   0,     -v[0]],
                  [-v[1],   v[0],   0]], dtype=np.float64)
    return m
#
# res = ch_askew(V1).dot(V2)
# print(res)
# #[ 0.085093   -0.36094228  0.19473956]
#
# print(-ch_askew(V1).T)
# # [[-0.     -0.2462  0.3249]
# #  [ 0.2462 -0.     -0.8147]
# #  [-0.3249  0.8147 -0.    ]]
#
# print(ch_askew(V1))
# # [[ 0.     -0.2462  0.3249]
# #  [ 0.2462  0.     -0.8147]
# #  [-0.3249  0.8147  0.    ]]

'''
clear;
clc;
close all;

V = [0.6096,  0.5747, 0.3260]';
n = norm(V);

R = eye(3) + (sin(n) / n )* ch_askew(V)  + ((1-cos(n)) / n^(2)) *ch_askew(V)^(2); %严龚敏2.1.20
# https://blog.csdn.net/Anchor_Yin/article/details/120238915
# https://blog.csdn.net/weixin_41855010/article/details/118969819
# https://en.wikipedia.org/wiki/Rodrigues%27_rotation_formula
fprintf("反对称矩阵幂指函数求解公式:\n");
R

R = expm(ch_askew(V)); 
fprintf("直接使用幂指函数求解: \n"); 
R
'''

from numpy.linalg import norm
sin = np.sin
cos = np.cos
exp2 = np.exp2
#
# V = np.array([0.6096,  0.5747, 0.3260]).T
# n = norm(V,2)   # modun L2 Norm "Euclidian Norm"
#
# print(n)
#
# R = np.identity(3) + (sin(n) / n) * (ch_askew(V)) + ((1-cos(n)) / (n**2)) * (ch_askew(V).dot(ch_askew(V)))
#
# print(R)
# # [[ 0.79603204 -0.12014543  0.59320996]
# #  [ 0.44751479  0.77672085 -0.44321012]
# #  [-0.40750887  0.6182797   0.67206156]]

'''
function m = ch_rv2m(rv) 
%  等效旋转矢量转换为旋转矩阵
%
% Input: rv - 旋转矢量
% Output: m -旋转矩阵 Cb2n 严龚敏 2.2.23
%     m = I + sin(|rv|)/|rv|*(rvx) + [1-cos(|rv|)]/|rv|^2*(rvx)^2
%     where rvx is the askew matrix or rv.

	nm2 = rv'*rv;  % 旋转矢量的模方
    if nm2<1.e-8   % 如果模方很小，则可用泰勒展开前几项求三角函数
        a = 1-nm2*(1/6-nm2/120); b = 0.5-nm2*(1/24-nm2/720);  % a->1, b->0.5
    else
        nm = sqrt(nm2);
        a = sin(nm)/nm;  b = (1-cos(nm))/nm2;
    end
    VX = ch_askew(rv);
    m = eye(3) + a*VX + b*VX^2;
'''


'''
mục tiêu:
quyết tâm hoàn thành
input: vecter quay (rv)
output: matran xoay Cb2n (m)

m = I + sin(|rv|)/|rv|*(rvx) + [1-cos(|rv|)]/|rv|^2*(rvx)^2

1. Tính mô đun

'''

V = np.array([0.6096,  0.5747, 0.3260])
# n = norm(V,2)
# R = np.identity(3) + (sin(n) / n) * (ch_askew(V)) + ((1-cos(n)) / (n**2)) * (ch_askew(V).dot(ch_askew(V)))
# # R = I + sin(theta) * M + (1-cos(theta)) * matmul(M,M)
# print(R)

'''
function m = ch_rv2m(rv) 
%  等效旋转矢量转换为旋转矩阵
%
% Input: rv - 旋转矢量
% Output: m -旋转矩阵 Cb2n 严龚敏 2.2.23
%     m = I + sin(|rv|)/|rv|*(rvx) + [1-cos(|rv|)]/|rv|^2*(rvx)^2
%     where rvx is the askew matrix or rv.

	nm2 = rv'*rv;  % 旋转矢量的模方
    if nm2<1.e-8   % 如果模方很小，则可用泰勒展开前几项求三角函数
        a = 1-nm2*(1/6-nm2/120); b = 0.5-nm2*(1/24-nm2/720);  % a->1, b->0.5
    else
        nm = sqrt(nm2);
        a = sin(nm)/nm;  b = (1-cos(nm))/nm2;
    end
    VX = ch_askew(rv);
    m = eye(3) + a*VX + b*VX^2;
'''
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

print(ch_rv2m(V))


