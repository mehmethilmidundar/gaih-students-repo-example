#Explain your work


Homework 1
1) How would you define Machine Learning?
2) What are the differences between Supervised and Unsupervised Learning? Specify example 3 algorithms for each of these.
3) What are the test and validation set, and why would you want to use them?
4) What are the main preprocessing steps? Explain them in detail. Why we need to prepare our data?
5) How you can explore and analyse countionus and discrete variables?
6) Analyse the plot given below. (What is the plot and variable type, check the distribution and make comment about how you can preproccess it.)


Answers:
1)Machine Learning is a type of AI algorithms which learns from the given data and solve unseen problems. 

2)In Supervised Learning, there is some input values and output values. The program try to estimate the outputs of unseen problems through train data. 
Otherwise, In Unsupervised Learning, there are no output values and the algorithm try to classify the similiar outputs.
Supervised Learning Algorithm Examples: Linear Regression, Polynomial Regression, Logistic Regression
Unsupervised Learning Algorithm Examples: K-Means, Hierarchical, Density-based.
	
3)Test dataset: It is used to evaluate trained model. It is generally 20/100 or 30/100 of the all data.
Validation dataset: It is used to choose the most proper hyperparameters in the model. It is generally 20/100 of the all data.
	
4)Duplicate Values: Removing the duplicate values in the dataset.
Imbalanced Data: If the data in the one class has highed or lower number of instances than data in the another class we should make their number of instances equal 
by adding copy instances or removing some elements.
Missing Values: If there is missing values because of data gathering, We should fill these values by using medion or mean.
Outlier detection: Some instances of data can be too separated from majority of the data set. This insatnces should be removed from the data set ,because there can be
a data gatherring mistake.
Feature Sclaing: To ease the work on the dataset, we scale the data. Standardization and Normalization are common techiques in the feature scaling.
Bucketing: It is used to minimize small observation errors. The near instances of data are put in the same bin and calculations are done by these bins.
Feature Extraction: The some related fatures can be extracted. Sometimes, we should change two feature with one superior feature.
Feature Encoding: The some verbal classes should be changed with numerical values. If the class features are ordinal values it should be changed with oredered numbers.
If they are nominal value it should be changed with one-hot encoding.
Data Split: Splitting the data train, validation, and test parts.
Cross Validation: In the some algorithms, we can choose the cross validation and change the data split parts and training over and over.
	
5)Continuos Variable: The random variable can be all numbers in the specified set such as reel numbers on the specified interval. 
Discrete Variable: The random variable can be the some specifed numbers in on the specified interval such that {1,2,3}.
	
6)It is continuous variable and the data is determined by histogram. The distrubion is asymetric and there are two local maxima. 	
The some values can be extracted because of outlier detection. The first value higher than 1.75 can be a otlier datum.
Scaling techinques can be applied to ease to undestand our graph.
	
