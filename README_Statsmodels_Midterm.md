


## Overview

This project explores Statsmodels, a powerful Python library for performing advanced statistical modeling and hypothesis testing.  
It demonstrates how Statsmodels bridges the gap between descriptive statistics and machine learning by providing tools for statistical inference, model diagnostics, and hypothesis testing.

The project includes:
- A detailed slide deck explaining theoretical and conceptual aspects of Statsmodels  
- A Jupyter Notebook tutorial demonstrating regression, ANOVA, logistic regression, time series, and hypothesis testing  
- Example code, visualizations, and model summaries for hands-on learning  

---

## Installation

To run this project locally:

```bash
# Clone the repository
git clone https://github.com/your-username/statsmodels-midterm.git
cd statsmodels-midterm

# Install dependencies

```python
!pip install statsmodels seaborn matplotlib pandas

```

---

## Project Contents

File Description
------------------
`Statsmodels_Deep_Dive.ipynb` Full code demonstration notebook
`Statsmodels_Presentation.pptx` PowerPoint presentation explaining Statsmodels
`README.md` Overview, installation, and usage instructions
`requirements.txt`  List of dependencies used in the project

---

## Topics Covered

1. Introduction to Statsmodels  
2. Ordinary Least Squares (OLS) Regression  
3. Logistic Regression  
4. ANOVA (Analysis of Variance)  
5. Time Series Forecasting (ARIMA)  
6. Hypothesis Testing (t-test)  
7. Model Diagnostics  
8. Comparison with R and Scikit-Learn  
9. Practical Insights and Statistical Interpretations  

---

## Example Outputs

### Linear Regression Summary

                            OLS Regression Results                            
==============================================================================
Dep. Variable:                 salary   R-squared:                       0.853
Model:                            OLS   Adj. R-squared:                  0.828
Method:                 Least Squares   F-statistic:                     34.68
Date:                Sun, 02 Nov 2025   Prob (F-statistic):            0.00106
Time:                        20:22:13   Log-Likelihood:                -81.891
No. Observations:                   8   AIC:                             167.8
Df Residuals:                       6   BIC:                             167.9
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const       1.875e+04   6073.908      3.087      0.021    3887.682    3.36e+04
experience  7083.3333   1202.813      5.889      0.001    4140.156       1e+04
==============================================================================
Omnibus:                        3.753   Durbin-Watson:                   1.512
Prob(Omnibus):                  0.153   Jarque-Bera (JB):                1.150
Skew:                           0.926   Prob(JB):                        0.563
Kurtosis:                       3.143   Cond. No.                         11.5
==============================================================================

### Logistic Regression (Binary Classification)

                           Logit Regression Results                           
==============================================================================
Dep. Variable:       bought_insurance   No. Observations:                   50
Model:                          Logit   Df Residuals:                       47
Method:                           MLE   Df Model:                            2
Date:                Sun, 02 Nov 2025   Pseudo R-squ.:                   1.000
Time:                        20:28:59   Log-Likelihood:            -4.8902e-06
converged:                      False   LL-Null:                       -33.203
Covariance Type:            nonrobust   LLR p-value:                 3.802e-15
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const       -323.0830   1.16e+04     -0.028      0.978   -2.31e+04    2.25e+04
age            0.5841     49.350      0.012      0.991     -96.140      97.308
income         0.0049      0.178      0.027      0.978      -0.345       0.355
==============================================================================

Complete Separation: The results show that there iscomplete separation or perfect prediction.
In this case the Maximum Likelihood Estimator does not exist and the parameters
are not identified.
### Time Series Forecast Diagnostic Plot  
(Generated from ARIMA model)
![ARIMA Diagnostic Plot](images/arima_diagnostic.png)
 SARIMAX Results                                
==============================================================================
Dep. Variable:                    co2   No. Observations:                  526
Model:                 ARIMA(1, 1, 1)   Log Likelihood                -633.476
Date:                Sun, 02 Nov 2025   AIC                           1272.951
Time:                        23:45:38   BIC                           1285.742
Sample:                    03-31-1958   HQIC                          1277.960
                         - 12-31-2001                                         
Covariance Type:                  opg                                         
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
ar.L1          0.5666      0.051     11.098      0.000       0.467       0.667
ma.L1          0.3321      0.057      5.798      0.000       0.220       0.444
sigma2         0.6529      0.046     14.087      0.000       0.562       0.744
===================================================================================
Ljung-Box (L1) (Q):                   2.76   Jarque-Bera (JB):                 1.36
Prob(Q):                              0.10   Prob(JB):                         0.51
Heteroskedasticity (H):               0.90   Skew:                             0.07
Prob(H) (two-sided):                  0.49   Kurtosis:                         2.80
===================================================================================

---

## Key Insights

- Statsmodels provides full statistical inference, unlike predictive-only libraries such as Scikit-learn.  
- It is closer in philosophy to R but allows seamless integration with Python’s scientific ecosystem.  
- Built-in datasets, formula-based modeling (`ols('y ~ x1 + x2')`) and model summaries make analysis intuitive and transparent.  

---

## Usage

You can open the Jupyter Notebook directly in your browser:
```bash
jupyter notebook Statsmodels_Deep_Dive.ipynb
```
Then execute each cell step-by-step to view results and interpretations.

---

## Conclusion

This project highlights how Statsmodels empowers analysts to interpret models with statistical rigor — connecting classic econometrics with modern Python workflows.

---



Created by Tavishi Chaturvedi 
Instructor: Matthew Macarty
Babson College | MS in Business Analytics  
Fall 2025 — OIM 7502: Advanced Programming
