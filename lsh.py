import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import sklearn
data = pd.read_csv("D:\\lsh.csv",delimiter=",")
print(data)
x = np.c_[data['xslc']]
y = np.c_[data['jg']]
data.plot(kind="scatter",x="xslc",y="jg")
plt.show()
from sklearn import linear_model
lr_model = linear_model.LinearRegression()
lr_model.fit(x,y)
print("斜率:%s,截距:%s" %(lr_model.coef_[0][0], lr_model.intercept_[0]))
print("估计模型为: y=%sx + %sy" %(lr_model.coef_[0][0], lr_model.intercept_[0]))
data.plot(kind="scatter",x="xslc",y="jg")
plt.plot(X,r_model.predict(X.reshape(-1,1)),color='red',linewidth=4)
plt.show()
X_new =[[100]]
print(lr_model.predict(X_new))
