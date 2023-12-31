import numpy as np
from math import pi
from math import cos, sin
from numpy.linalg import multi_dot

def euler_zyz(x=0, y=0, z=0):
    '''
    (x, y, z) orientation values in degree, for more details check the link below:
    https://www.mecademic.com/academic_articles/space-orientation-euler-angles/
    '''
    
    # First we start by converting degree to rad
    x = np.deg2rad(x)
    y = -np.deg2rad(y)
    z = -np.deg2rad(z)
    
    # Now we create rotation matrices according to the rotation axis
    r_x = np.array([[1, 0, 0],
                     [0, cos(x), -sin(x)],
                     [0, sin(x), cos(x)]])
    r_y = np.array([[cos(y), 0, sin(y)],
                    [0, 1, 0],
                    [-sin(y), 0, cos(y)]])
    r_z = np.array([[cos(z), -sin(z), 0],
                     [sin(z), cos(z), 0],
                     [0, 0, 1]])
    # We calculate the total rotation matix (since the rotation is about fix global axis we do left multiplication '[r_z].[r_y].[r_x]')
    r_zyx = multi_dot([r_z, r_y, r_x])
    
    r11, r12, r13 = r_zyx[0]
    r21, r22, r23 = r_zyx[1]
    r31, r32, r33 = r_zyx[2]

    # Extract Euler angles with order 'ZYZ' the details are in the link below 
    '''https://math.stackexchange.com/questions/3328656/convert-rotation-matrix-to-euler-angles-zyz-y-convention-analytically'''
    z1 = np.arctan2(r23, -r13)
    z2 = np.arctan2(r32,r31)
    y = np.arctan2(r31*cos(z2)+r32*sin(z2), r33)
    
    
    return [np.rad2deg(z1), np.rad2deg(y), np.rad2deg(z2)]
