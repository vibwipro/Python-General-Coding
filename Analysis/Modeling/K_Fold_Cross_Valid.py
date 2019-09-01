from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
digits = load_digits()


##### Train test and split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(digits.data,digits.target,test_size=0.3)


#### Logistic Regression
lr = LogisticRegression(solver='liblinear',multi_class='ovr')
lr.fit(X_train, y_train)
print ('Logistic Regression Score is : ' + str(lr.score(X_test, y_test) ))

##### SVM
svm = SVC(gamma='auto')
svm.fit(X_train, y_train)
print ('SVM Score is : ' + str(svm.score(X_test, y_test)))

#####Random Forest
rf = RandomForestClassifier(n_estimators=40)
rf.fit(X_train, y_train)
print ('Random Forest Score is : ' + str(rf.score(X_test, y_test)))


##########################################    KFold cross validation
#### Example


from sklearn.model_selection import KFold
kf = KFold(n_splits=3)


for train_index, test_index in kf.split([1,2,3,4,5,6,7,8,9]):
    print(train_index, test_index)

###########   Use KFold for our digits example

def get_score(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    return model.score(X_test, y_test)

from sklearn.model_selection import StratifiedKFold
folds = StratifiedKFold(n_splits=3)

scores_logistic = []
scores_svm = []
scores_rf = []

for train_index, test_index in folds.split(digits.data,digits.target):
    X_train, X_test, y_train, y_test = digits.data[train_index], digits.data[test_index], \
                                       digits.target[train_index], digits.target[test_index]
    scores_logistic.append(get_score(LogisticRegression(solver='liblinear',multi_class='ovr'), X_train, X_test, y_train, y_test))

    scores_svm.append(get_score(SVC(gamma='auto'), X_train, X_test, y_train, y_test))

    scores_rf.append(get_score(RandomForestClassifier(n_estimators=40), X_train, X_test, y_train, y_test))

print ('LogisticRegression score is : ' + str(scores_logistic))
print ('SVC score is : ' + str(scores_svm))
print ('RandomForestClassifier score is : ' + str(scores_rf))

##########################   cross_val_score function

from sklearn.model_selection import cross_val_score

########## Logistic regression model performance using cross_val_score
clg= cross_val_score(LogisticRegression(solver='liblinear',multi_class='ovr'), digits.data, digits.target,cv=3)

print ('Logistic regression model performance using cross_val_score' + str(clg))


###### svm model performance using cross_val_score
csv = cross_val_score(SVC(gamma='auto'), digits.data, digits.target,cv=3)

print (csv)

####################### random forest performance using cross_val_score
crf = cross_val_score(RandomForestClassifier(n_estimators=40),digits.data, digits.target,cv=3)

print (crf)

########################## Parameter tunning using k fold cross validation

scores1 = cross_val_score(RandomForestClassifier(n_estimators=5),digits.data, digits.target, cv=10)
print (np.average(scores1))

scores3 = cross_val_score(RandomForestClassifier(n_estimators=30),digits.data, digits.target, cv=10)
print(np.average(scores3))
