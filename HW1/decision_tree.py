#-------------------------------------------------------------------------
# AUTHOR: Arturo Blandon
# FILENAME: decision_tree.py
# SPECIFICATION: Creates a decision tree based on data read from a csv.
# FOR: CS 4200- Assignment #1
# TIME SPENT: 15 minutes.
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays
#importing some Python libraries

from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

#transfor the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
#--> add your Python code here
# X =

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

for i in range(len(db)):
  X.append([])
  for j in range(len(db[0])-1):
    X[i].append(transformFeatures[db[i][j]])

#transfor the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> addd your Python code here
# Y = 
transformClass = {
  "Yes": 1,
  "No": 2
}
for i in range(len(db)):
  Y.append(transformClass[db[i][len(db[0])-1]])

#fiiting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()


