![image](https://user-images.githubusercontent.com/99313947/154220840-05476774-6760-444a-9a2a-03990c19e27b.png)

Input data
- x = [ left forearm, right forearm, left lower leg, right lower leg, head, pelvis(root) ]
- x = [ larm, rarm, lleg, rleg, head, root ]

Accelerations
[ a_larm, a_rarm, a_lleg, a_rleg, a_head, a_root ] ∈ R 3 × 6

>       ...
>       [[ 1.0883e+00,  2.7423e+00,  1.7926e+00],        a larm  [3 x 1]
>        [-5.8708e-01,  1.0961e+00, -2.3861e+00],        a rarm  [3 x 1]
>        [ 9.7838e+00, -5.0318e-01, -1.2231e+01],        a lleg  [3 x 1]
>        [-1.4591e-01, -2.3153e+00, -2.9268e+00],        a rleg  [3 x 1]
>        [-4.0718e+00,  1.0248e+00, -5.1928e-02],        a head  [3 x 1]
>        [ 4.2117e+00,  5.0769e-01,  2.4204e-01]]        a root  [3 x 1]
>       ...

Rotations
[ R_larm, R_rarm, R_lleg, R_rleg, R_head, R_root ] ∈ R 3 × 3 × 6

>       ...
>       [[[[ 0.2445,  0.1298,  0.9609],       R_larm  [3 x 3]
>          [-0.9482,  0.2391,  0.2090],
>          [-0.2026, -0.9623,  0.1815]],
>          
>         [[-0.6387,  0.3131,  0.7029],       R_rarm  [3 x 3]
>          [ 0.7657,  0.1683,  0.6208],
>          [ 0.0761,  0.9347, -0.3473]],
>          
>         [[-0.4953,  0.3525,  0.7940],       R_lleg  [3 x 3]
>          [-0.0647,  0.8965, -0.4383],
>          [-0.8663, -0.2685, -0.4212]],
>          
>         [[-0.5527, -0.0621,  0.8310],       R_rleg  [3 x 3]
>          [ 0.0439,  0.9937,  0.1035],
>          [-0.8322,  0.0937, -0.5465]],
>          
>         [[-0.0883,  0.6607,  0.7454],       R_head  [3 x 3]
>          [-0.0799,  0.7413, -0.6664],
>          [-0.9929, -0.1184, -0.0127]],
>          
>         [[-0.5511, -0.0337,  0.8337],       R_root  [3 x 3]
>          [-0.1052,  0.9940, -0.0294],
>          [-0.8278, -0.1039, -0.5514]]]
>       ...

Normalize and concat
- x = [ a_larm, a_rarm, a_lleg, a_rleg, a_head, a_root, R_larm, R_rarm, R_lleg, R_rleg, R_head, R_root ] ∈ R 72
