#decoding=utf-8
#array的创建和属性
import numpy as np
x=np.array([1,2,3,4,5,6,7,8])
X=np.array([[1,2,3,4],[5,6,7,8]])
y=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])


print(x.shape)
print(x.size)
print(x.ndim)
print(x.dtype)

print(X.shape)
print(X.size)
print(X.ndim)
print(X.dtype)

print(y.ndim)
