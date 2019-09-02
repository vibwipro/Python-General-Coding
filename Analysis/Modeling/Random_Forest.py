import pandas as pd
from sklearn.datasets import load_digits
digits = load_digits()

############# describe
print (dir(digits))

import matplotlib.pyplot as plt

plt.gray()
for i in range(2):
    plt.matshow(digits.images[i])
    plt.show()


############### Dataframe

df = pd.DataFrame(digits.data)
print(df.head())

############ Adding target field to dataframe
df['target'] = digits.target

print(df[0:12])


##############   Train and the model and prediction

X = df.drop('target',axis='columns')
y = df.target

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=20)
model.fit(X_train, y_train)

########### Score
print(model.score(X_test, y_test))

#############  predict
y_predicted = model.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_predicted)
print(cm)


########### Plotting
import matplotlib.pyplot as plt
import seaborn as sn
plt.figure(figsize=(10,7))
sn.heatmap(cm, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')
plt.show()
