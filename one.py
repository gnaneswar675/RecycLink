1. Evaluate the Information Gain of each attribute in the Student dataset and identify the best attribute to split for predicting Result.
@relation student
@attribute Attendance numeric
@attribute InternalMarks numeric
@attribute AssignmentScore numeric
@attribute SemesterMarks numeric
@attribute Result {Pass, Fail}
2. Demonstrate classification using the J48 Decision Tree algorithm on the Weather dataset and predict Play for a given test instance.
@relation weather
@attribute Outlook {Sunny, Overcast, Rain}
@attribute Temperature numeric
@attribute Humidity numeric
@attribute Windy {True, False}
@attribute Play {Yes, No}
3. Demonstrate classification using the ID3 Decision Tree algorithm on the Weather dataset (with all attributes nominal) and derive decision rules for Play.
@relation weather
@attribute Outlook {Sunny, Overcast, Rain}
@attribute Temperature {Hot, Mild, Cool}
@attribute Humidity {High, Normal}
@attribute Windy {True, False}
@attribute Play {Yes, No}
4. Predict the Result of a new student record using k-Nearest Neighbor classification and evaluate model accuracy.
@relation student
@attribute Attendance numeric
@attribute InternalMarks numeric
@attribute AssignmentScore numeric
@attribute SemesterMarks numeric
@attribute Result {Pass, Fail}
5. Predict the species of a new Iris sample using Bayesian classification and display the probability of each class.
@relation iris
@attribute SepalLength numeric
@attribute SepalWidth numeric
@attribute PetalLength numeric
@attribute PetalWidth numeric
@attribute Species {Setosa, Versicolor, Virginica}
6. Select prominent feature subsets from the Iris dataset to improve model performance.
@relation iris
@attribute SepalLength numeric
@attribute SepalWidth numeric
@attribute PetalLength numeric
@attribute PetalWidth numeric
@attribute Species {Setosa, Versicolor, Virginica}
7. Perform pre-processing on the Customer dataset: handling missing values, normalize numerical columns, normalization, Discretization, standardization, remove unnecessary attributes and encode categorical attributes.
@relation customer
@attribute CustomerID numeric
@attribute Age numeric
@attribute Gender {Male, Female}
@attribute AnnualIncome numeric
@attribute SpendingScore numeric
@attribute Segment {High, Medium, Low}
8. Apply data pre-processing techniques on the Iris dataset, including handling missing values, normalization, and encoding categorical data.
@relation iris
@attribute SepalLength numeric
@attribute SepalWidth numeric
@attribute PetalLength numeric
@attribute PetalWidth numeric
@attribute Species {Setosa, Versicolor, Virginica}
9. Implement a Back Propagation Neural Network on the Student Performance dataset to train and update weights and biases for predicting the Result (Pass/Fail).
@relation student_performance
@attribute Attendance numeric
@attribute InternalMarks numeric
@attribute AssignmentScore numeric
@attribute SemesterMarks numeric
@attribute Result {Pass, Fail}
10. Apply the k-Means clustering algorithm on the Customer Segmentation dataset to group customers based on similar spending behavior.
@relation customer_segmentation
@attribute Age numeric
@attribute AnnualIncome numeric
@attribute SpendingScore numeric
11. Use the Apriori algorithm on the Market Basket dataset to identify frequent itemsets and generate strong association rules.
@relation market_basket
@attribute Milk {Yes, No}
@attribute Bread {Yes, No}
@attribute Butter {Yes, No}
@attribute Eggs {Yes, No}
@attribute Jam {Yes, No}
12. Apply the FP-Growth algorithm on the Retail Transactions dataset to find frequent patterns and generate association rules.
@relation retail_transactions
@attribute Rice {Yes, No}
@attribute Wheat {Yes, No}
@attribute Oil {Yes, No}
@attribute Sugar {Yes, No}
@attribute Salt {Yes, No}
13. Compare the performance of Decision Tree (J48), k-NN, and Naive Bayes classifiers on the Agricultural dataset using accuracy, precision, and recall metrics.
@relation agricultural
@attribute Temperature numeric
@attribute Rainfall numeric
@attribute SoilMoisture numeric
@attribute FertilizerUsed numeric
@attribute CropYield {Low, Medium, High}
14. Install and configure the WEKA tool on your system. Demonstrate how to load a dataset, explore available algorithms, and perform a simple classification task to verify successful installation.
