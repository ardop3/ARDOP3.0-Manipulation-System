
# this code does not consider end effector it has to be modelled seperately
#!/usr/bin/env python

from __future__ import print_function
import numpy as np
import math
from numpy.linalg import inv
import serial




import rospy

from geometry_msgs.msg import Twist

import sys, select, termios, tty


def forward(new_angle):
     

     theta0 = new_angle.item(0)  
     theta1 = new_angle.item(1) 
     theta2 = new_angle.item(2) 
     
     l= a3*math.sin(theta1) +a4*math.sin(theta1+theta2)
     x= l*math.sin(theta0)
     y = l*math.cos(theta0)
     z = (a3*math.cos(theta1) + a4*math.cos(theta1+theta2)) 

     co = np.array([x,y,z])
     #print("forward")
     return co

def inverse(x,y,z):

    error = 0 
    
    theta0 = math.atan(x/y) + error 

    r2 = math.sqrt(x*x + y*y)
    r1 = z#+a1
    phi2 = math.atan(r2/r1)
    r3 = math.sqrt(r1*r1 + r2*r2)
    p = a3*a3 +r3*r3 -a4*a4
    q = 2*a3*r3
    phi1 = math.acos(p/q)
    theta1 = phi2 - phi1  + error  

    r = a3*a3+a4*a4-r3*r3
    s= 2*a3*a4

    phi3 = math.acos(r/s)

    theta2 = pi - phi3  + error 
    deg = np.array([theta0,theta1,theta2])
    #print("inv")
    return deg

def delta(target_co,cur_co):

    i1 = np.array([target_co - cur_co])
    i = i1.transpose()
    #print("delta")
    return i 

def inverse_jacobian(new_angle):

    a0 = new_angle.item(0)
    a1 = new_angle.item(1)
    a2 = new_angle.item(2)

    jx0 = (a3*math.sin(a1) +a4*math.sin(a1+a2)) * math.cos(a0)
    jx1 = (a3*math.cos(a1) + a4*math.cos(a1+a2))*math.sin(a0)
    jx2 = (a4*math.cos(a1 +a2))*math.cos(a0)

    jy0 = -(a3*math.sin(a1) +a4*math.sin(a1+a2))*math.sin(a0)
    jy1 = (a3*math.cos(a1) +a4 *math.cos(a1+a2)) *math.cos(a0)
    jy2 = (a4*math.cos(a1 +a2)) *math.cos(a0)

    jz0 = 0
    jz1 = (-a3*math.sin(a1) -a4*math.sin(a1+a2))
    jz2 = -a4*math.sin(a1+a2)

    jacobian = np.array([[jx0,jx1,jx2],[jy0,jy1,jy2],[jz0,jz1,jz2]])
    inv_jacobian = inv(jacobian)
    #print("inv_jaco")
    return inv_jacobian

    
    

#if __name__ == 'main' :




def error_correction(in_angle):

    '''
    b1 = 4.77
    b2 = 1.94*in_angle
    b3 = -0.34*(in_angle**2)
    b4 = 0.0394*(in_angle**3)
    b5  = -1.22*(10**-3)*(in_angle**4)
    '''


    b1 = -0.756
    b2 = 0.751*in_angle
    b3 = -0.0231*(in_angle**2)
    b4 = 3.57*(10**-4)*(in_angle**3)
    b5 = -1.94*(10**-6)*(in_angle**4) 


    correction_factor = b1+b2+b3+b4+b5

    return correction_factor


def jacobian_start(x,y,z):

    target_co = np.array([x,y,z])
    angle = inverse(x,y,z) # determine approx value
    new_angle = np.array([angle])

    #print(new_angle)
    for k in range(300):

        cur_co = forward(new_angle)
        diff_co = delta(target_co, cur_co)
        diff_angle1 = inverse_jacobian(new_angle)
        diff_angle = np.matmul(diff_angle1,diff_co)
        #diff_angle = diff_angle1 * diff_co
        new_angle = np.add(new_angle,diff_angle)
        #new_angle = new_angle + diff_angle
        #print(new_angle[0,0]*180/pi , new_angle[0,1]*180/pi, new_angle[0,2]*180/pi)
        #print(cur_co)
        return new_angle[0,0]*180/pi , new_angle[0,1]*180/pi, new_angle[0,2]*180/pi
 



if __name__=="__main__":

    a3 = 20
    a4 =35
    a1 =5  
              ## link lengths will be updated
    pi =3.14


    with open('place_coordinates.dat','r') as f:
        output_list1 = f.read().strip().split(',')
        x_co1, y_co1, z_co1, arm_num = float(output_list1[1]) ,float(output_list1[2]) , float(output_list1[3])


    pub = rospy.Publisher('servo_angle', Twist, queue_size = 1)
    rospy.init_node('arm_angle')

    in1 , in2 , in3 = jacobian_start(x_co1,y_co1,z_co1)

    correction = error_correction(in2)

    final_angle  = [in1 , in2+correction, in3]


    with open("place_ik.dat", "w+") as f: 
        f.write(str(("place_ik",final_angle[0] , final_angle[1], final_angle[2],arm_num,"place_ik")))

    
    '''
    print(final_angle)
    twist = Twist()
    twist.linear.x = final_angle[0]; twist.linear.y = final_angle[1]; twist.linear.z = final_angle[2];
    twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
    pub.publish(twist)
    '''
    







'''

with open('pick_coordinates.dat','r') as f:
    output_list1 = f.read().strip().split(',')
    x_co1, y_co1, z_co1 = float(output_list1[1]) ,float(output_list1[2]) , float(output_list1[3])

    jacobian_start(x_co1, y_co1, z_co1)


with open('place_coordinates.dat','r') as f:
    output_list2 = f.read().strip().split(',')
    x_co2, y_co2, z_co2 = float(output_list2[1]) ,float(output_list2[2]) , float(output_list2[3])

    jacobian_start(x_co1, y_co1, z_co1)
'''





 
