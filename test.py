import matplotlib.pyplot as plt
import numpy as np

a=np.linspace(0,3,4)
print(a)
b=np.linspace(4,7,4)
c=np.concatenate((b,a))
c=np.sort(c)
print(c)
# x=[0,1,2,3,4,5]
# y1=[0,1,2,3,4,5]
# y2=[3,3,3,3,3,3]
# fig_1=plt.figure(1)
# fig_2=plt.figure(2)


# plt.plot(x,y1)
# plt.figure(1)
# plt.plot(x,y2)


# plt.show()