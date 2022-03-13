'''
Accelerometer, Gyroscope, Magnetometer

function Cb2n = ch_rotx(theta)
% 3D初等旋转， theta为旋转角度，rad
Cb2n = [1 0 0; 0 cos(theta) -sin(theta); 0 sin(theta) cos(theta)];
end

function Cb2n = ch_roty(theta)
% 3D初等旋转， theta为旋转角度，rad
Cb2n = [cos(theta), 0 sin(theta); 0 1 0; -sin(theta) 0 cos(theta)];
end

function Cb2n = ch_rotz(theta)
% 3D初等旋转， theta为旋转角度，rad
Cb2n = [cos(theta) -sin(theta) 0; sin(theta) cos(theta) 0; 0 0 1];
end

b系到n系，绕X轴旋转30.000 ° 的旋转矩阵 Cb2nX 为

Cb2nX =

    1.0000         0         0
         0    0.8660   -0.5000
         0    0.5000    0.8660

b系到n系的，绕Y轴旋转40.000 °  的旋转矩阵 Cb2nX为

Cb2nY =

    0.7660         0    0.6428
         0    1.0000         0
   -0.6428         0    0.7660

b系到n系的，绕Z轴旋转50.000 °  的旋转矩阵 Cb2nX为

Cb2nZ =

    0.6428   -0.7660         0
    0.7660    0.6428         0
         0         0    1.0000
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

Cb2nX = ch_rotx(30)
# print("Rotate around the X axis %.1f ° the rotation matrix of Cb2nX: " %(i))
print(Cb2nX)

Cb2nY = ch_roty(40)
# print("Rotate around the Y axis %.1f ° the rotation matrix of Cb2nY: " %(i))
print(Cb2nY)

Cb2nZ = ch_rotz(50)
# print("Rotate around the Z axis %.1f ° the rotation matrix of Cb2nZ: " %(i))
print(Cb2nZ)

# Rotate around the X axis 30.0 ° the rotation matrix of Cb2nX:
# [[ 1.         0.         0.       ]
#  [ 0.         0.8660254 -0.5      ]
#  [ 0.         0.5        0.8660254]]
# Rotate around the Y axis 40.0 ° the rotation matrix of Cb2nY:
# [[ 0.76604444  0.          0.64278761]
#  [ 0.          1.          0.        ]
#  [-0.64278761  0.          0.76604444]]
# Rotate around the Z axis 50.0 ° the rotation matrix of Cb2nZ:
# [[ 0.64278761 -0.76604444  0.        ]
#  [ 0.76604444  0.64278761  0.        ]
#  [ 0.          0.          1.        ]]

'''
Ab = [0 0 1]';
fprintf("b系下有点 A:%.3f %.3f %.3f\n", Ab(1), Ab(2), Ab(3));

An = Cb2nX*Ab;
fprintf("b系下点A经过Cb2nX旋转到n系为: %.3f %.3f %.3f\n",An(1), An(2), An(3));

An = Cb2nY*Ab;
fprintf("b系下点A经过Cb2nY旋转到n系为: %.3f %.3f %.3f\n",An(1), An(2), An(3));

An = Cb2nZ*Ab;
fprintf("b系下点A经过Cb2nZ旋转到n系为: %.3f %.3f %.3f\n",An(1), An(2), An(3));
'''

Ab = np.array([0, 0, 1])
print("A", Ab)

An = ch_rotx(30).dot(Ab)
print("A Cb2nX", An)

An = ch_roty(40).dot(Ab)
print("A Cb2nY", An)

An = ch_rotz(50).dot(Ab)
print("A Cb2nZ", An)

# A [0 0 1]
# A Cb2nX [ 0.        -0.5        0.8660254]
# A Cb2nY [0.64278761 0.         0.76604444]
# A Cb2nZ [0. 0. 1.]

'''
Phép xoay 2D
    R(theta) = np.array([[cos(theta), - sin(theta)],
                          [sin(theta), cos(theta)]])
Phép xoay 3D
Xoay quanh trục Z
    ch_rotz(theta) = np.array([[cos(theta), -sin(theta), 0],
                                [sin(theta), cos(theta), 0],
                                 [0, 0, 1]])
Xoay quanh trục Y
    ch_roty(theta) = np.array([[cos(theta), 0, sin(theta)],
                                [0, 1, 0],
                                 [-sin(theta), 0, cos(theta)]])
Xoay quanh trục X
    ch_rotx(theta) = np.array([[1, 0, 0], 
                                [0, cos(theta), -sin(theta)],
                                 [0, sin(theta), cos(theta)]])                                 
    
'''