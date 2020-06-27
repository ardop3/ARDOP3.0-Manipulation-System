import numpy as np 
from numpy.linalg import inv
import matplotlib.pyplot as plt 

t0 = 0
tf = 60


def time_domain ():
	a1 = t0**3
	a2 = t0**2
	a3 =  t0
	a4 = 1

	a5 = 3*t0**2
	a6 = 2*t0
	a7 =1
	a8 =0

	a9 =tf**3
	a10 = tf**2
	a11 = tf
	a12 =1

	a13 = 3*tf**2
	a14 =2*tf
	a15 =1
	a16 =0

	A = np.array([  [a1 , a2 , a3 , a4 ] ,     [a5 , a6 , a7 , a8 ] , [a9 , a10 , a11 , a12 ],  [a13 , a14 , a15 , a16 ]    ])
	inv_A = inv(A)
	
	return inv_A




def angle_matrix():

	q0 = 0
	q1 = 0
	q2 = 0
	q3 = 0
	q4 =0
	q5= 0


	q6 = 0
	q7 = 0
	q8 = 0
	q9 = 0
	q10 =0
	q11= 0


	q12 = 45
	q13 = 30
	q14 = 60
	q15 = 15
	q16=  25
	q17= 0


	q18 = 0
	q19 = 0
	q20 = 0
	q21 = 0
	q22 =0
	q23= 0

	angle_B = np.array ( [    [q0,q1,q2,q3,q4,q5]  , [q6,q7,q8,q9,q10,q11] , [q12,q13,q14,q15,q16,q17] , [q18,q19,q20,q21,q22,q23]])
	

	return angle_B



def plot_angle(param):
	angle0 = []
	angle1 = []
	angle2 = []
	angle3 = []
	angle4 = []
	angle5 = []

	time = []

	for t in range (t0 , tf):
		p = param[0][0]*(t**3) + param[1][0]*(t**2) + param[2][0]*(t) + param[3][0]
		q = param[0][1]*(t**3) + param[1][1]*(t**2) + param[2][1]*(t) + param[3][1]
		r = param[0][2]*(t**3) + param[1][2]*(t**2) + param[2][2]*(t) + param[3][2]
		s = param[0][3]*(t**3) + param[1][3]*(t**2) + param[2][3]*(t) + param[3][3]
		l3 = param[0][4]*(t**3) + param[1][4]*(t**2) + param[2][4]*(t) + param[3][4]
		u =param[0][5]*(t**3) + param[1][5]*(t**2) + param[2][5]*(t) + param[3][5]

		angle0.append(p)
		angle1.append(q)
		angle2.append(r)
		angle3.append(s)
		angle4.append(l3)
		angle5.append(u)

		time.append(t)


	plt.plot(angle0 , time ,  label = "theta0")
	plt.plot(angle1 , time ,  label = "theta1")
	plt.plot(angle2 , time ,  label = "theta2")
	plt.plot(angle3 , time ,  label = "theta3")
	plt.plot(angle4 , time ,  label = "theta4")
	plt.plot(angle5 , time ,  label = "theta5")

	plt.xlabel('angle')
	plt.ylabel('time')
	plt.legend()
	plt.show()





def plot_velocity(param):

	vel_angle0 =[]
	vel_angle1 =[]
	vel_angle2 =[]
	vel_angle3 =[]
	vel_angle4 =[]
	vel_angle5 =[]

	time_vel = []

	for t1 in range(t0, tf):

		x1 = 3*param[0][0]*(t1**2) + 2*param[1][0]*t1   + param[2][0]
		x2 = 3*param[0][1]*(t1**2) + 2*param[1][1]*t1   + param[2][1]
		x3 = 3*param[0][2]*(t1**2) + 2*param[1][2]*t1  + param[2][2]
		x4 = 3*param[0][3]*(t1**2) + 2*param[1][3]*t1   + param[2][3]
		x5 = 3*param[0][4]*(t1**2) + 2*param[1][4]*t1   + param[2][4]
		x6 = 3*param[0][5]*(t1**2) + 2*param[1][5]*t1   + param[2][5]

		vel_angle0.append(x1)
		vel_angle1.append(x2)
		vel_angle2.append(x3)
		vel_angle3.append(x4)
		vel_angle4.append(x5)
		vel_angle5.append(x6)

		time_vel.append(t1)


	plt.plot(vel_angle0 , time_vel ,  label = "vel_theta0")
	plt.plot(vel_angle1 , time_vel ,  label = "vel_theta1")
	plt.plot(vel_angle2 , time_vel ,  label = "vel_theta2")
	plt.plot(vel_angle3 , time_vel ,  label = "vel_theta3")
	plt.plot(vel_angle4 , time_vel ,  label = "vel_theta4")
	plt.plot(vel_angle5 , time_vel ,  label = "vel_theta5")

	plt.xlabel('velocity')
	plt.ylabel('time')
	plt.legend()
	plt.show()









inverse_A = time_domain()
B = angle_matrix()


parameters = np.matmul(inverse_A, B)

plot_angle(parameters)

plot_velocity(parameters)


print(parameters)


