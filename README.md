# Cardiovascular Risk Prediction Analysis

![image](https://user-images.githubusercontent.com/39692126/182947470-ce4046e1-1c36-4528-a664-3478d35845a7.png)


[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)]()
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)]()
[![forthebadge](https://forthebadge.com/images/badges/powered-by-responsibility.svg)]()
[![forthebadge](https://user-images.githubusercontent.com/39692126/182951370-d1f4e0bd-e2b6-4597-8297-d2697d10513d.png)](https://chd-risk-prediction-app.herokuapp.com/)

Link to Heroku: [https://chd-risk-prediction-app.herokuapp.com/](https://chd-risk-prediction-app.herokuapp.com/)

### Summary

  Heart disease is the leading cause of death worldwide, accounting for one third of all deaths in 2019. Heart disease cases nearly doubled from 271 million in 1990 to 523 million in 2019, and the number of heart disease fatalities increased by half, from 12 million to 18 million. The shocking fact is that 3 out of 4 such deaths take place in developing countries.

Of all the heart diseases, coronary heart disease (aka heart attack) is by far the most common and most fatal. In this project, we’ve given effort to determine whether the patient has a 10-year risk of future coronary heart disease (CHD) or not. The dataset is from a cardiovascular study on residents of the town of Framingham, Massachusetts. The dataset is collected from Kaggle and it has over 3000 records and 15 attributes. Each attribute is a potential risk factor. There are both demographic and behavioral and medical risk factors. Our target is a binary variable.

We’ve used Python to build this project. NumPy and Pandas are used as the base libraries. For data visualization, libraries like matplotlib, seaborn, and plotly are used. We’ve performed exploratory data analysis on various aspects like chances of CHD over ages, genders, or their habit of smoking, how medical features are distributed over patients' ages, or the effects of blood pressure on the risk factor, and much more. Apart from these, we’ve also checked for null or missing values and plotted the distribution and correlation of attributes. Then we perform feature selection and standardize the selected features before training. For the feature selection, we’ve combined the results obtained from the BorutaPy and SelectKBest algorithms.

The dataset we’re working on is an imbalanced dataset, i.e., there is a significant difference between the target class labels. So, we’ve applied oversampling techniques like SMOTE to balance the classes. For the machine learning part, we’ve built two pipelines. One has the steps defined as standardization and cross-validation. The other pipeline is the same as the first one but it has one extra step, i.e., to resample the data. For both the pipelines, we’ve used ShuffleSplit to split the data into 5 folds and used HalvingGridSearch for cross validation. It is similar to grid search CV but an optimized and fast version of the former. We’ve trained six different machine learning algorithms on these two pipelines. I found Random Forest with the oversampled dataset to be the best performing model with a recall and f1 score of 87%.

We’ve also used shap and eli5 libraries to explain our model and found out that glucose level and systematic bp contribute more to the prediction of our model. We know, in the sensitive healthcare field where we’ve to deal with people’s lives, that an 85% recall means at least 15 people in every 100 who have a risk of CHD will be incorrectly diagnosed. Keeping in mind that most of our data points are artificially synthesized, we may consider this as a limitation of our project and should look forward to the future scope.
   
   ### 🔧 Libraries used:
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
* Pipeline 2 - Model Training on Oversampled Dataset using SMOTE : LogisticRegression, LinearSVC, DecisionTreeClassifier, RandomForestClassifier, KNeighborClassifier, BernoulliNB
* Classification
* Prediction
   
   The metrics we've achieved are as follows,
   
   ![image](https://user-images.githubusercontent.com/39692126/182948670-6bf4a78d-19e6-4e91-bb72-653430f2de8f.png)
   
   ![image](https://user-images.githubusercontent.com/39692126/182948787-c9f18f9b-22ab-4e4a-8451-9b98ad28b040.png)


## 🤝 Connect with me on
* Debanjan:
<br> [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/awesomedeba10/)







   
   

