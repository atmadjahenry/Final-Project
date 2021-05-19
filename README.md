# Final-Project
Final Project Bank Loan Approval

This data is from Kaggle, [Bank Loan Status Dataset](https://www.kaggle.com/zaurbegiev/my-dataset).

This dataset has 100514 rows and 18 columns.


Project Description
------------
Bank loan is when a bank offers to lend money to consumers for a certain period. As a condition of bank loan, the borrower will need to pay a certain amount of interest per month or year. Loan prediction is one of the methods used by the bank to investigate their consumers are going to be default (Charged Off) or not (Fully Paid).
Machine learning is a tool to make a bank loan prediction. With the classification method, we can predict the loan status of the consumers.
From this dataset, we can see that around 22.64% of consumers failed to pay the loan. Consumers who failed to pay will make a big loss to Bank as a lender.


Project Goals
-------------
The goal of the project is to reduce the risk of charged off loan status from consumers by making Machine Learning applications to determine the loan request based on the historical data.


Modeling
-------------
In this project, I build a Machine Learning that can predict the future loan status of the consumers.
I compare 5 Machine Learning models to predict, such as :
* Logistic Regression
* Random Forest Classifier
* Decision Tree Classifier
* K-Nearest Neighbors
* Ada Boost Classifier

In this case, I have imbalanced target so I used smote for resampling the model.

Decision Tree Classifier and Ada Boost Classifier has the highest Recall Score, so I did hyperparameter tuning for those models. Ada Boost Classifier is the best model for this case. We can still improve our model with threshold adjustment. I try to find the best threshold for Ada Boost Classifier model based on Precision-Recall Curve. The best threshold is 0.499394525800627.
Recall Score for Ada Boost Classifier is 0.87
