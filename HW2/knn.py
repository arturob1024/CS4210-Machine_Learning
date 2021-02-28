#-------------------------------------------------------------------------
# AUTHOR: Arturo Blandon
# FILENAME: knn.py
# SPECIFICATION: Reads binary points and outputs LOO-CV Error Rate for 1NN.
# FOR: CS 4200- Assignment #2
# TIME SPENT: 10 Minutes
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []

#reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)

errors = 0

#loop your data to allow each instance to be your test set
for i, instance in enumerate(db):

    #add the training features to the 2D array X removing the instance that will be used for testing in this iteration. For instance, X = [[1, 3], [2, 1,], ...]]
    #--> add your Python code here
    # X =
    X = []
    Y = []
    
    for j in range(len(db)):
        if j == i:
            continue
        #X.append( [ ord(db[j][0]),ord(db[j][1]) ] )
        X.append( [ int(db[j][0]),int(db[j][1]) ] )


    #transform the original training classes to numbers and add to the vector Y removing the instance that will be used for testing in this iteration. For instance, Y = [1, 2, ,...]
    #--> add your Python code here
    # Y =
    for j in range(len(db)):
        if j == i:
            continue
        Y.append(ord(db[j][2]))

    #store the test sample of this iteration in the vector testSample
    #--> add your Python code here
    #testSample =
    testSample = instance
    testSample = [int(testSample[0]), int(testSample[1])]

    #fitting the knn to the data

    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

    #use your test sample in this iteration to make the class prediction. For instance:
    #class_predicted = clf.predict([[1, 2]])[0]
    #--> add your Python code here
    
    class_predicted = clf.predict([testSample])[0]

    #compare the prediction with the true label of the test instance to start calculating the error rate.
    #--> add your Python code here

    if(instance[2] != chr(class_predicted)):
        errors += 1

    

#print the error rate
#--> add your Python code here
output = "LOO-CV Error rate for 1NN = {}"
print(output.format(errors/10))






