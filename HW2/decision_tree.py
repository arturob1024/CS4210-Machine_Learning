#-------------------------------------------------------------------------
# AUTHOR: Arturo Blandon
# FILENAME: decision_tree.py
# SPECIFICATION: Train, test, and output performance of models created using each dataset.
# FOR: CS 4200- Assignment #2
# TIME SPENT: 40 Minutes
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

transformFeatures = {
  "Young": 1,
  "Prepresbyopic": 2,
  "Presbyopic": 3,
  "Myope": 4,
  "Hypermetrope": 5,
  "No": 6,
  "Yes": 7,
  "Reduced": 8,
  "Normal": 9,
}

transformClass = {
  "Yes": 1,
  "No": 2
}

for ds in dataSets:

    dbTraining = []
    X = []
    Y = []
    accuracy_arr = []

    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)


    #transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    #--> add your Python code here
    # X =

    for i in range(len(dbTraining)):
        X.append([])
        for j in range(len(dbTraining[0])-1):
            X[i].append(transformFeatures[dbTraining[i][j]])

    #transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    #--> add your Python code here
    # Y =

    for i in range(len(dbTraining)):
        Y.append(transformClass[dbTraining[i][len(dbTraining[0])-1]])

    #loop your training and test tasks 10 times here
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    for i in range (10):

       #fitting the decision tree to the data setting max_depth=3
       clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
       clf = clf.fit(X, Y)

       #read the test data and add this data to dbTest
       #--> add your Python code here
       # dbTest =
       dbTest = []
       with open("contact_lens_test.csv", 'r') as csvfile:
         reader = csv.reader(csvfile)
         for j, row in enumerate(reader):
           if j > 0:
             dbTest.append(row)


       for data in dbTest:
           #transform the features of the test instances to numbers following the same strategy done during training, and then use the decision tree to make the class prediction. For instance:
           #class_predicted = clf.predict([[3, 1, 2, 1]])[0]           -> [0] is used to get an integer as the predicted class label so that you can compare it with the true label
           #--> add your Python code here

           transformedInstance = [ transformFeatures[data[0]] , transformFeatures[data[1]] , transformFeatures[data[2]] , transformFeatures[data[3]]]
           class_predicted = clf.predict([transformedInstance])[0]
           trueLabel = transformClass[data[4]]

           #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
           #--> add your Python code here
           if (class_predicted == trueLabel) and (trueLabel == 1):
             TP += 1
           elif (class_predicted == trueLabel) and (trueLabel == 2):
             TN += 1
           elif (class_predicted != trueLabel) and (class_predicted == 1):
             FP += 1
           elif (class_predicted != trueLabel) and (class_predicted == 2):
             FN += 1

       accuracy = (TP+TN)/(TP+TN+FP+FN)
       accuracy_arr.append(accuracy)

        #find the lowest accuracy of this model during the 10 runs (training and test set)
        #--> add your Python code here 
    lowest_accuracy = min(accuracy_arr)

    #print the lowest accuracy of this model during the 10 runs (training and test set).
    #your output should be something like that:
         #final accuracy when training on contact_lens_training_1.csv: 0.2
         #final accuracy when training on contact_lens_training_2.csv: 0.3
         #final accuracy when training on contact_lens_training_3.csv: 0.4
    #--> add your Python code here
    output = "final accuracy when training on {}: {}"
    print(output.format(ds,lowest_accuracy))




