import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('runway_set.csv')
# print(df.info())
# print(df.shape)
# print(df.columns.values)

X = df[["Time(ms)","length_ft"]]    # independent variable
Y = df["Lane"]                      # dependent variable

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.25, random_state=50)

acr = LogisticRegression()
acr.fit(X_train,Y_train)            # train the dataset
print(acr.score(X_test,Y_test))     # print the accuracy



pred = acr.predict(X_train)         # prediction


Y_test = np.array(list(Y_test))
t = np.resize(Y_test, (1,2000))     # resize Y_test
Y_pred = np.array(pred)
p = np.rese(Y_pred, (1,2000))     # # resize Y_pred


comp = pd.DataFrame({'Actual':t.flatten(),
                     'Predict':p.flatten()})

graph = comp.head(20)    # take top 20 valus in graph
graph.plot(kind = 'bar') # shor bar chart of graph
