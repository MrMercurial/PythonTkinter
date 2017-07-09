#coding:utf-8
import pandas,matplotlib
import matplotlib.pyplot as plt
# import Scipy
import pandas as pd
import numpy as np
from numpy.random.mtrand import randn
import scipy

data={i:randn() for i in range(10)}
data1=[i**2 for i in xrange(10)]

arry1=np.array(data1)
data2=[[[1,2,3,3,],[34,234,43,34]],[[23,44,3,2],[23,44,3,2]],[[23,44,3,2],[2,4,6,4]]]
arry2=np.array(data2)
arry4=randn(20,3)
# plot(arry4)
# img=pd.DataFrame(arry4)
# # img=img.cumsum()
# img.plot()
# plt.show()

print arry2.ndim
print arry2.shape
print arry1.sort()
print arry2.sort()
print arry2.sort(1)


print np.zeros((3,2))
print np.eye(4,dtype=np.int32).dtype
print arry1==1
# help(np.eye)
arry3=np.array(data2)
print arry3
print arry3[1]
print arry3[0,1]

print arry1
print arry1*10
print arry1+arry1
# print arry1**10

# plot(range(20))
points=np.arange(-5,5,0.01)
xs,ys=np.meshgrid(points,points)
print ys
z=np.sqrt(xs**2+ys**2)
plt.imshow(z,cmap=plt.cm.gray)
plt.show()