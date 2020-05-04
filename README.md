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
* 77 variables
	* 31 are considered numeric or continuous
	* 46 are considered categorical or discrete

## Modelling


## Model Evaluation


## Deliverable
