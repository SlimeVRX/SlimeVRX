'''
eul = [30 40 50]';


fprintf("按312顺序(先转Z-然后X-最后Y)旋转，其中X,Y,Z旋转角度为%d° %d° %d° 得到对应的坐标变换矩阵：\n", eul(1), eul(2), eul(3));

eul_rad = deg2rad(eul);
Cb2n =  ch_rotz(eul_rad(3)) * ch_rotx(eul_rad(1)) * ch_roty(eul_rad(2));
Cb2n
'''

import numpy as np
cos = np.cos
sin = np.sin
pi = np.pi

def ch_rotx(i):
    theta = pi * i / 180
    return np.array([[1, 0, 0], [0, cos(theta), -sin(theta)], [0, sin(theta), cos(theta)]])

def ch_roty(i):
    theta = pi * i / 180
    return np.array([[cos(theta), 0, sin(theta)], [0, 1, 0], [-sin(theta), 0, cos(theta)]])

def ch_rotz(i):
    theta = pi * i / 180
    return np.array([[cos(theta), -sin(theta), 0], [sin(theta), cos(theta), 0], [0, 0, 1]])

eul = [30, 40, 50]
Cb2n = ch_rotz(eul[2]). dot(ch_rotx(eul[0])). dot(ch_roty(eul[1]))
print(Cb2n)

# [[ 0.24620194 -0.66341395  0.70658796]
#  [ 0.79341204  0.5566704   0.24620194]
#  [-0.5566704   0.5         0.66341395]]

print(Cb2n.T)
print(np.transpose(Cb2n))

Cn2b = ch_roty(-eul[1]). dot(ch_rotx(-eul[0])). dot(ch_rotz(-eul[2]))
print(Cn2b)

# print(Cn2b == Cb2n.T)

# [[ 0.24620194  0.79341204 -0.5566704 ]
#  [-0.66341395  0.5566704   0.5       ]
#  [ 0.70658796  0.24620194  0.66341395]]

# Cb2n = ch_rotz(eul[2]).dot(ch_roty(eul[1])).dot(ch_rotx(eul[0]))
# print(Cb2n)
#
# # [[ 0.49240388 -0.45682599  0.74084306]
# #  [ 0.58682409  0.80287234  0.10504046]
# #  [-0.64278761  0.38302222  0.66341395]]

Ab = np.array([0, 0, 1])

ch_roty(40). dot(ch_rotx(30). dot(ch_rotx(50). dot(Ab)))

ch_rotx(30). dot(ch_roty(40). dot(ch_rotx(50). dot(Ab)))

'''
eul = [30 40 50] [X, Y, Z]

Xoay 312 Z - X - Y
    Cb2n = ch_rotz(eul[2]). dot(ch_rotx(eul[0])). dot(ch_roty(eul[1]))
    Cn2b = ch_roty(-eul[1]). dot(ch_rotx(-eul[0]). dot(ch_rotz(-eul[2]))
Xoay 321 Z - Y - X
    Cb2n = ch_rotz(eul[2]). dot(ch_roty(eul[1])). dot(ch_rotx(eul[0]))

'''