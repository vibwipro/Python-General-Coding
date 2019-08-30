
from sklearn.datasets import load_iris
iris=load_iris()
'''
print (type(iris))
#print (iris.data)
print(iris.feature_names)
print(iris.target)
print(iris.target_names)
print(iris.data.shape)
print (iris.target.shape)
'''


X=iris.data
y=iris.target
#print(X.shape)
#print(y.shape)

##########################################

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=1)

knn.fit(X,y)

X_new=[[3,5,4,2],[5,4,3,2]]
Fl = knn.predict(X_new)
print ('Pridicted Flower type are :- ')
print (iris['target_names'][Fl])

##########################################

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(iris['data'],iris['target'],test_size=0.3,random_state=0)

knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train,y_train)
y_pred=knn.predict(X_test)

print (y_pred)
print (y_test)


