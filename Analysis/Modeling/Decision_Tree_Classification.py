import pandas as pd

####### Read file
df = pd.read_csv("salaries.csv")
df.head()

############3 Drop Column 'salary_more_then_100k'
inputs = df.drop('salary_more_then_100k',axis='columns')


target = df['salary_more_then_100k']


from sklearn.preprocessing import LabelEncoder
le_company = LabelEncoder()
le_job = LabelEncoder()
le_degree = LabelEncoder()


inputs['company_n'] = le_company.fit_transform(inputs['company'])
inputs['job_n'] = le_job.fit_transform(inputs['job'])
inputs['degree_n'] = le_degree.fit_transform(inputs['degree'])

print (inputs)



inputs_n = inputs.drop(['company','job','degree'],axis='columns')

print (inputs_n)

print (target)


from sklearn import tree
model = tree.DecisionTreeClassifier()

model.fit(inputs_n, target)

model.score(inputs_n,target)

#################   Is salary of Google, Computer Engineer, Bachelors degree > 100 k ?
model.predict([[2,1,0]])

######################    Is salary of Google, Computer Engineer, Masters degree > 100 k ?
model.predict([[2,1,1]])

