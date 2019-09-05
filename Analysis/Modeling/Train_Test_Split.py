import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


##### Read CSV file
df = pd.read_csv("Data/carprices.csv")
print(df.head())

##### Plot scatter graph###
plt.scatter(df['Mileage'],df['Sell Price($)'])
plt.show()
plt.scatter(df['Age(yrs)'],df['Sell Price($)'])
plt.show()



X = df[['Mileage','Age(yrs)']]
y = df['Sell Price($)']

##### Splitting test and train data
## random_state=10
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)

print (X_train)

### LinearRegression
from sklearn.linear_model import LinearRegression

clf = LinearRegression()
clf.fit(X_train, y_train)

print (clf.predict(X_test))
print (y_test)

#### Score
print (clf.score(X_test, y_test))