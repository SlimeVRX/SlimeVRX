import numpy as np
cos = np.cos
sin = np.sin
asin = np.arcsin
atan2 = np.arctan2
from numpy.linalg import norm


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

def ch_qnormlz(q):
    q = q / norm(q,2)
    if q[0] < 0:
        q[0] = -q[0]
        q[1] = -q[1]
        q[2] = -q[2]
        q[3] = -q[3]
    return q

def ch_qmulv(q, vi):
    qo1 =              - q[1] * vi[0] - q[2] * vi[1] - q[3] * vi[2]
    qo2 = q[0] * vi[0]                + q[2] * vi[2] - q[3] * vi[1]
    qo3 = q[0] * vi[1]                + q[3] * vi[0] - q[1] * vi[2]
    qo4 = q[0] * vi[2]                + q[1] * vi[1] - q[2] * vi[0]
    vo = vi
    vo[0] = -qo1 * q[1] + qo2 * q[0] - qo3 * q[3] + qo4 * q[2]
    vo[1] = -qo1 * q[2] + qo3 * q[0] - qo4 * q[1] + qo2 * q[3]
    vo[2] = -qo1 * q[3] + qo4 * q[0] - qo2 * q[2] + qo3 * q[1]
    return vo

def ch_att_upt(in_, gyr, dt):
    rv = gyr * dt
    dq = ch_rv2q(rv)
    out = ch_qmul(in_, dq)
    out = ch_qnormlz(out)
    return out

def ch_nav_equ_local_tan(p, v, q ,acc, gyr, dt, gN):
    old_v = v
    sf = acc
    q = ch_att_upt(q, gyr, dt)

    sf = ch_qmulv(q, sf)
    sf = sf + gN
    v = old_v + dt * sf

    p = p + (old_v + v) * dt / 2
    return p, v, q
