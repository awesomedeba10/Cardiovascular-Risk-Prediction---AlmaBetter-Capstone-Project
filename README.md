# Cardiovascular-Risk-Prediction---AlmaBetter-Capstone-Project

![image](https://user-images.githubusercontent.com/39692126/168034896-40d238ee-cd19-425d-8770-d348df7c7260.png)


[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)]()
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/powered-by-responsibility.svg)](https://forthebadge.com)

  Heart disease is the leading cause of death worldwide, accounting for one third of deaths in 2019. Heart disease cases nearly doubled over the period, from 271 million in 1990 to 523 million in 2019, and the number of heart disease deaths rose from 12.1 million to 18.6 million. Over three quarters of these deaths took place in low- and middle-income countries.

  Of all heart diseases, coronary heart disease (aka heart attack) is by far the most common and the most fatal. The silver lining is that heart attacks are highly preventable and simple lifestyle modifications (such as reducing alcohol and tobacco use; eating healthily and exercising) coupled with early treatment greatly improves its prognosis.

  In this project, the classification goal is to predict whether the patient has 10-year risk of future coronary heart disease (CHD) or not. The dataset is from an ongoing cardiovascular study on residents of the town of Framingham, Massachusetts. It includes over 3,000 records and 15 attributes. Each attribute is a potential risk factor. There are both demographic, behavioral, and medical risk factors.

   The dataset is an imbalance dataset, so SMOTE has been used to balance the dataset for both classes. Top features have been selected and normalized before training. Many machine learning algorithms like Logistic Regression, Random Forest, LinearSVC etc. has been used to train and evaluate with both imbalanced and oversampled dataset. Out of which, random forest is proved to be best in performance with a f1 score of 0.85. Recall is far more important metrics than accuracy or precision. As this is a sensitive domain, and we can’t put any risk of falsely identify a potentially risked patient. However, the maximum recall we’ve achieved is 0.8549.
   
   ## 🔧 Libraries used:
| Base Library 		    | Visualization		    | ML  	|
|---			      		|---		    		|---		      	|
| - Numpy	    | - Matplotlib		    | - scikit-learn		|
| - Pandas				    | - seaborn			    | - imblearn			|
| - json		    | - plotly			    | -  shap			|
| - 			    | - 			    | - eli5		|
| - 	    | - 			    | - 			|
   
   ## 🔧 Steps used:
* Data Exploration
* EDA
* Feature Selection
* Pipeline (Common) - Data Normalization : StandardScaler
* Pipeline 1 - Model Training on Imbalanced Dataset by default : LogisticRegression, LinearSVC, DecisionTreeClassifier, RandomForestClassifier, KNeighborClassifier, BernoulliNB
* * Pipeline 2 - Model Training on Oversampled Dataset using SMOTE : LogisticRegression, LinearSVC, DecisionTreeClassifier, RandomForestClassifier, KNeighborClassifier, BernoulliNB
* Classification
* Prediction
   
   The metrics we've achieved are as follows,
   
   ![image](https://user-images.githubusercontent.com/39692126/168030546-3256d055-703e-4583-a055-b69eb33fb0d2.png)
   
   ![image](https://user-images.githubusercontent.com/39692126/168030600-59c98fff-f9a9-44ee-ac9f-aa48a6213ca0.png)

Below is the Confusion Matrix, Classification Report, ROC AUC Graph and Feature Importances score obtained by Final Model:

![image](https://user-images.githubusercontent.com/39692126/168030746-82ebb5a5-60f7-47ac-9d57-ecc6ec609a3a.png)

![image](https://user-images.githubusercontent.com/39692126/168030798-93132691-7c45-4449-9bda-22eafdab3791.png)

![image](https://user-images.githubusercontent.com/39692126/168030940-3fa1088e-5dbd-4cf1-b55c-2832b793ebf8.png)

![image](https://user-images.githubusercontent.com/39692126/168031063-860db09b-d407-4cc2-95e4-fcde96d8be83.png)

![image](https://user-images.githubusercontent.com/39692126/168031254-e2aa324a-2312-441b-b059-cacc3890fb6d.png)

## 🤝 Connect with me on
* Debanjan:
<br> [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/awesomedeba10/)







   
   

