'''
clear;
clc;
close all;

X = [1, 0]';

for i = 0 : pi/4 :2*pi
    theta = i;
    R = [cos(theta) -sin(theta); sin(theta) cos(theta)];
    Y = R*X;
    fprintf("将X [%.3f %.3f]  逆时针旋转 %.1f° 后得到 %.3f %.3f\n", X(1), X(2), rad2deg(theta), Y(1), Y(2));
end

结果:

将X [1.000 0.000]  逆时针旋转 0.0° 后得到 1.000 0.000
将X [1.000 0.000]  逆时针旋转 45.0° 后得到 0.707 0.707
将X [1.000 0.000]  逆时针旋转 90.0° 后得到 0.000 1.000
将X [1.000 0.000]  逆时针旋转 135.0° 后得到 -0.707 0.707
将X [1.000 0.000]  逆时针旋转 180.0° 后得到 -1.000 0.000
将X [1.000 0.000]  逆时针旋转 225.0° 后得到 -0.707 -0.707
将X [1.000 0.000]  逆时针旋转 270.0° 后得到 -0.000 -1.000
将X [1.000 0.000]  逆时针旋转 315.0° 后得到 0.707 -0.707
将X [1.000 0.000]  逆时针旋转 360.0° 后得到 1.000 -0.000
'''

import numpy as np
pi = np.pi
cos = np.cos
sin = np.sin

X = np.array([1,0])

# for i in range(0,2*pi, pi/4):
for i in range(0,361, 45):
    theta = pi * i/180
    R = np.array([[cos(theta), - sin(theta)],
                  [sin(theta), cos(theta)]])
    Y = R.dot(X)
    print("X: [%.3f,%.3f] anticlockwise rotation %.1f get [%.3f %.3f] " % (X[0],X[1], i, Y[0], Y[1]))

# X: [1.000,0.000] anticlockwise rotation 0.0 get [1.000 0.000]
# X: [1.000,0.000] anticlockwise rotation 45.0 get [0.707 0.707]
# X: [1.000,0.000] anticlockwise rotation 90.0 get [0.000 1.000]
# X: [1.000,0.000] anticlockwise rotation 135.0 get [-0.707 0.707]
# X: [1.000,0.000] anticlockwise rotation 180.0 get [-1.000 0.000]
# X: [1.000,0.000] anticlockwise rotation 225.0 get [-0.707 -0.707]
# X: [1.000,0.000] anticlockwise rotation 270.0 get [-0.000 -1.000]
# X: [1.000,0.000] anticlockwise rotation 315.0 get [0.707 -0.707]
# X: [1.000,0.000] anticlockwise rotation 360.0 get [1.000 -0.000]