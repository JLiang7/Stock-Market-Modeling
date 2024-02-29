# Stock-Market-Modeling

## Table of Contents

- [About](#about-the-project)
- [Setup](#setup)
- [Modeling](#modeling)

---

## About The Project
Two-Part Project
### First Part 
- Running models on a static S&P500 csv file
```
Stock.ipynb
sphist.csv 
```
### Second Part
- Apply modeling to modern stock data retrieved thru API such as Quandl, Google, Yahoo, AlphaVantage, sooq ...
- But for this proj, I will be using yahoo
- First attempt would be on one stock
- 2024, added other tech stocks into the picture 
```
Proj_Stock_Modeling_API.ipynb
```

## Setup
> Install packages first (If Anaconda was used, only some packages are needed to be installed)
```
pip install pandas-datareader
pip install numpy
pip install pandas
pip install -U scikit-learn
pip install matplotlib
pip install setuptools
pip install xgboost
```
---

## Modeling
**1. Data Preprocessing and Exploratory Data Analysis**
  >- Check and Understand Data
  >- Convert datatypes
  >- Clean Data ( Remove anything unused, Duplicates) Removed rows with missing values 
  
**2. Train/Test Split**
  >- Split data to train and test set (20~25%)
  
**3. Prepare for Modeling**
  >- Feature Engineer - Aggregations ( Any Calculations)
  >- Transform Data ( Normalize, Standardize, One Hot Encoder...)
  >- Feature Selection ( Dimension?)
  
**4. Picking models**
  >- Try out Models such as Regression or Classification Models
  
**5. Model Selection**
  >- Cross-Validation (Kfold...)
  
**6. Model Tuning and Picking Best Model**
  >- Hyperparameter tuning ( Using Cross-Validation, Grid Search, Bayesian Optimization...)
  >- Compare Accuracy and pick best model

## Insights and Conclusion
```
Achieved K-Fold Validation Accuracy of % with a Standard Deviation of %
Accuracy Score of %
F-1 Accuary of %
```
Confusion Matrix 
|    | 0  | 1  | 2  |
|----|----|----|----| 
| 0  | 13 | 0  | 0  |
| 1  | 0  | 16 | 0  |
| 2  | 0  | 1  | 8  |

> **Conclusion**

>- Random Forest and LTSM has achieved similar Accuracy Scores
