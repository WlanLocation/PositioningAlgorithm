#print "helloworld"
import numpy as np

def Crammer(xyz1,xyz2,xyz3,xyz4,L1,L2,L3,L4):
    '''
    :param xyz1: certain_coordinate1 //array
    :param xyz2: certain_coordinate2 //array
    :param xyz3: certain_coordinate3 //array
    :param l1: distance to xyz1
    :param l2: distance to xyz2
    :param l3: distance to xyz3
    :return: the unknown coordinate //array
    '''
    x1 = xyz1[0]
    y1 = xyz1[1]
    z1 = xyz1[2]
    x2 = xyz2[0]
    y2 = xyz2[1]
    z2 = xyz2[2]
    x3 = xyz3[0]
    y3 = xyz3[1]
    z3 = xyz3[2]
    x4 = xyz4[0]
    y4 = xyz4[1]
    z4 = xyz4[2]

#    for i in range(0,2,1):
    l1sq = x1**2 + y1**2 + z1**2
    l2sq = x2**2 + y2**2 + z2**2
    l3sq = x3**2 + y3**2 + z3**2
    l4sq = x4**2 + y4**2 + z4**2

    x12 = x1 - x2
    x23 = x2 - x3
    x34 = x3 - x4
    y12 = y1 - y2
    y23 = y2 - y3
    y34 = y3 - y4
    z12 = z1 - z2
    z23 = z2 - z3
    z34 = z3 - z4

    l12sq = l1sq - l2sq
    l23sq = l2sq - l3sq
    l34sq = l3sq - l4sq

    L12sq = L1 ** 2 - L2 ** 2
    L23sq = L2 ** 2 - L3 ** 2
    L34sq = L3 ** 2 - L4 ** 2


    D = 8 * np.linalg.det([[x12, y12, z12],
                           [x23, y23, z23],
                           [x34, y34, z34]])

    D1 = 4 * np.linalg.det([[l12sq-L12sq, y12, z12],
                            [l23sq-L23sq, y23, z23],
                            [l34sq-L34sq, y34, z34]])

    D2 = 4 * np.linalg.det([[x12, l12sq-L12sq, z12],
                            [x23, l23sq-L23sq, z23],
                            [x34, l34sq-L34sq, z34]])

    D3 = 4 * np.linalg.det([[x12, y12, l12sq-L12sq],
                            [x23, y23, l23sq-L23sq],
                            [x34, y34, l34sq-L34sq]])

    #print D1,D2,D3,D
    #print l1sq,l2sq,l3sq
    #print l12sq,l23sq,l31sq
    #print x12,x23,x34,y12,y23,y34,z12, z23, z34


    xyz=[-1,-1,-1]
    xyz[0] = D1/D
    xyz[1] = D2/D
    xyz[2] = D3/D
    return xyz

print Crammer([0,1,1],[1,1,0],[1,0,1],[0,0,0],1,1,1,3**0.5)


