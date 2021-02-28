#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4200- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv

#reading the training data
#--> add your Python code here
training = []

with open("weather_training.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            training.append (row)

#transform the original training features to numbers and add to the 4D array X. For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
# X =
transformFeatures = {
    "Sunny": 1,
    "Overcast": 2,
    "Rain": 3,
    "Hot": 4,
    "Mild": 5,
    "Cool": 6,
    "High": 7,
    "Normal": 8,
    "Weak": 9,
    "Strong": 10
}

X = []

for i in range(len(training)):
    X.append([])
    for j in range(1,len(training[0])-1):
        X[i].append(transformFeatures[training[i][j]])

#transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
# Y =
transformClass = {
    "Yes": 1,
    "No": 2
}

Y = []

for i in range(len(training)):
    Y.append(transformClass[training[i][len(training[0])-1]])

#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the data in a csv file
#--> add your Python code here
testing = []
transformedTesting = []

with open("weather_test.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            testing.append (row)

for i in range(len(testing)):
    transformedTesting.append([])
    for j in range(1,len(testing[0])-1):
        transformedTesting[i].append(transformFeatures[testing[i][j]])

#printing the header os the solution
print ("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) + "Humidity".ljust(15) + "Wind".ljust(15) + "PlayTennis".ljust(15) + "Confidence".ljust(15))

#use your test samples to make probabilistic predictions.
#--> add your Python code here
#-->predicted = clf.predict_proba([[3, 1, 2, 1]])[0]
for i in range(len(transformedTesting)):
    predicted = clf.predict_proba([transformedTesting[i]])
    if(predicted[0][0] >= 0.75):
        print(testing[i][0].ljust(15) + testing[i][1].ljust(15) + testing[i][2].ljust(15) + testing[i][3].ljust(15) + testing[i][4].ljust(15) + "Yes".ljust(15) + str(predicted[0][0]).ljust(15))
    if(predicted[0][1] >= 0.75):
        print(testing[i][0].ljust(15) + testing[i][1].ljust(15) + testing[i][2].ljust(15) + testing[i][3].ljust(15) + testing[i][4].ljust(15) + "No".ljust(15) + str(predicted[0][1]).ljust(15))




