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
### Second Part
- Apply modeling to modern stock data retrieved thru API 

## Setup
> Install packages first
```
pip install pandas-datareader
pip install numpy
pip install pandas
```
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

