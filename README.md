## Problem Statement
Develop a model for classification of connections to a server. The model should be designed to flag instances of intrusion to the server, and specifically limit the number of false positives. Too many false positives would lead to having too many possible issues to check.

## Outcome Predictions
Build a classification model using training data and apply boosting methods to obtain a precision score of no less than 0.95.

## Data Acquisition
The data was obtained via the 1998 DARPA Intrusion Detection Evaluation Program. Further information on the data was found on a web document (http://kdd.ics.uci.edu/databases/kddcup99/task.html) that was adapted from a 2000 paper by Stolfo et al, titled: *Cost-based Modeling and Evaluation for Data Mining WithA pPLication to Fraud and Intrusion Deteciton: Results from the JAM Project*.

## Data Preparation
In preparation for modelling, the data was slightly altered. 

In the data used, there were a few variables that did not vary, and thus were deleted. 

There was an 'id' column which was as unique as the connections themselves and served no purpose for analysis.

In addition to this, the target column was changed from 'yes/no' to boolean, and renamed for ease. It should be noted that the data dictionary contained in the web document given above that most of the symbolic columns had already been dummied. Further variable reduction was completed using $\chi^2$ and ANOVA statistical methods.

## Universe Description
* 48113 connection records
	* 200 classified as 'outliers'
	* Each of the outliers is considered an attack
* 77 variables
	* 31 are considered numeric or continuous
	* 46 are considered categorical or discrete
* 43 variables considered statistically significant
	* i.e. p-value < 0.05

## Modelling
1. Developed a method for variable reduction using chi^2 and ANOVA methods. Reduced variables from 77 to 43, 21 in categorical or discrete, 22 in numerical or continuous, as per definitions on the data dictionary document.
2. Attempted Logistic Regression, which scored very poorly ~0.4 precision.
3. Attempted a Bagging model with logistic regression which was taking far too long, and was thus abandoned in the interest of time.
4. A decision tree model was found to be decent, but couldn't be improved past a precision of about 0.8.
5. A Random Forest model was then attempted, which yielded the best results. A precision of about 0.87.
	* Within the RF model, I also attempted to balance the classes using various methods in imbalanced-learn. Unfortunately they yielded worse results than the default class balancing contained in the classifiers.
6. In an attempt to improve this further, I next attempted XGBoost, which provided a much better precision score of 0.95 or higher. The recall score was also not terrible, though isn't the aim of this task.

## Model Evaluation
The model to be used is an XGBoost model based on gradient boosted trees of depth 2. The model required both L1 and L2 regularization for best results. The scores were as follows:

	* Train:
		* Precision = 0.99
		* Recall = 0.97
	* Validation:
		* Precision = 0.95
		* Recall = 0.61
	* Test:
		* Precision = 0.97
		* Recall = 0.68

## Deliverable
