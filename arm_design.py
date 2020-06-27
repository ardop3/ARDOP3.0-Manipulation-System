import numpy as np
from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt

L1= []
L2 = []

T1= []
T2	= []

'''

for j in range(42):

	L1.append(j)
	L2.append(42-j)



for i in range(len(L1)):



		t1_1 =     9.974*(10**-3)*( L1[i]**2 ) + 26.98 + 0.065* L1[i]  #(4.86)*(10**-3)*(L1[i]**2)
		t1_2 =  0#0.065*L1[i]
		t1_3 = 0#(9.72)*(10**-3)*(42- L1[i])*(L1[i]+( (42- L1[i])  /2))
		t1_4 =0 #0.195*(L1[i]+42-L1[i])
		t1_5 = 0#0.2 *( L1[i]+42-L1[i] + 8)  


		t1 =   t1_1+t1_2+t1_3+t1_4+t1_5      #(  (4.86)*(10**-3)*(i**2) + 0.065*i + (9.72)*(10**-3)*(p)*(i+(p/2)) + 0.195*(i+p)  + 0.2 ( i+p + 8)  )

		t2 = (  (4.86)*(10**-3)*L2[i]  + ( 3*0.065)*L2[i]+ (0.2* ( L2[i]+8 ))  )


		T1.append(t1)
		T2.append(t2)


T1 = np.array(T1)
T2 = np.array(T2)
L1 = np.array(L1)
L2 = np.array(L2)


#print( T1[20])

ax = plt.axes(projection='3d')
ax.scatter3D(L1, L2, T1, color = 'Blue' ,  label = T1)
ax.scatter3D(L1, L2, T2, color = 'green' ,  label =T2 )
ax.set_title(' Torque Requirement for Motor S1 and S2 ');
plt.xlabel('L1') 
# naming the y axis 
plt.ylabel('L2') 

ax.set_zlabel('T1 , T2')

plt.show()




T1 = T1*1.5
T2 = T2*1.5


print(T1[20] , T2[22])

T1 = np.where( T1> 52.5  , -10 , T1)


ax = plt.axes(projection='3d')
ax.scatter3D(L1, L2, T1, color = 'Blue' ,  label = T1)
ax.scatter3D(L1, L2, T2, color = 'green' ,  label =T2 )
ax.set_title(' Practical Considerations ');
plt.xlabel('L1') 
# naming the y axis 
plt.ylabel('L2') 

ax.set_zlabel('T1 , T2')

plt.show()








diff= []

for r in range (len(L1)):

	g = T1[r] - T2[r]
	diff.append(g)



ax1 = plt.axes(projection='3d')
ax1.scatter3D(T1, T2, diff, color = 'Blue' ,  label = T1)
#ax1.scatter3D(L1, L2, T2, color = 'green' ,  label =T2 )
ax1.set_title(' Torque difference plot');
plt.xlabel('T1') 
# naming the y axis 
plt.ylabel('T2') 

ax.set_zlabel('T1 - T2')

plt.show()




plt.xlabel('L1') 
# naming the y axis 
plt.ylabel('T1') 
plt.plot( L1, T1 , label='l1' , color = 'Green' )

#plt.plot( L1, T2, label='l2' )
plt.show()



'''


for j in range(1, 42):

	L1.append(j)
	L2.append(42-j)

'''

for l in L1:

	k = 9.72*(10**-3)*l

	torque1 =    (0.065)*l +26.763
	
                                                                       
	T1.append(torque1) 
	 

for l in L2:

	torque2 = 0.5*(l)**2 + (l)*0.395 +1.6
	T2.append(torque2)



'''

#print ( L1, L2)


for l in range(len(L1)):

	k1 = 9.72*(10**-3)*L1[l]
	k2 = 9.72*(10**-3)*(42- L1[l])

	m = 0.065

	l1 = L1[l]
	l2 =(42- L1[l])

	ml1 = k1
	ml2 = k2
	mp = 0.2

	torque1 = ml1*(l1/2) + m*(l1) + ml2*(l1 + .5*l2) + 3*m*(42) + 0.2*(50)
	torque2 = ml2*(l2/2) + 3*m*(l2) + 0.2*(l2+ 8 )
	T1.append(torque1) 
	T2.append(torque2)





#T1 = 1.5*T1



plt.xlabel('L1') 
# naming the y axis 
plt.ylabel('T1') 
plt.plot( L1, T1 , label='t1' , color = 'Green' )
plt.plot( L1, T2 , label='t2' , color = 'Blue' )
#plt.plot( L1, T2, label='l2' )
plt.show()



T1 = np.array(T1)
T2 = np.array(T2)

T1= 1.74*T1
T2= 1.74*T2

plt.xlabel('L1') 
# naming the y axis 
plt.ylabel('T1') 
plt.plot( L1, T1 , label='t1' , color = 'Green' )
plt.plot( L1, T2 , label='t2' , color = 'Blue' )
#plt.plot( L1, T2, label='l2' )
plt.show()

T1 = np.where( T1> 49.1  , -10 , T1)
T2 = np.where( T2> 24.5  , -10 , T2)

plt.xlabel('L1') 
# naming the y axis 
plt.ylabel('T1') 
plt.plot( L1, T1 , label='t1' , color = 'Green' )
plt.plot( L1, T2 , label='t2' , color = 'Blue' )
#plt.plot( L1, T2, label='l2' )
plt.show()
