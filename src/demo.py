#------------------------------------------------------------------------------
# BETA
#------------------------------------------------------------------------------
# import os
# # Manually set path of current file
# path_to_here = "/Users/muhlbach/Repositories/mlregression/src"
# # Change path
# os.chdir(path_to_here)

#------------------------------------------------------------------------------
# Libraries
#------------------------------------------------------------------------------
%reset -f

# Standard
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

# This library
from mlregression.mlreg import MLRegressor
from mlregression.mlreg import RF
from mlregression.estimator.boosting import XGBRegressor

#------------------------------------------------------------------------------
# Data
#------------------------------------------------------------------------------
# Generate data
X, y = make_regression(n_samples=500,
                       n_features=10, 
                       n_informative=5,
                       n_targets=1,
                       bias=0.0,
                       coef=False,
                       random_state=1991)

X_train, X_test, y_train, y_test = train_test_split(X, y)

#------------------------------------------------------------------------------
# Main use of MLRegressor
#------------------------------------------------------------------------------
# Instantiate model
mlreg = MLRegressor(estimator="RandomForestRegressor",
                    max_n_models=2)

# Fit
mlreg.fit(X=X_train, y=y_train)

# Predict
y_hat = mlreg.predict(X=X_test)

# Access all the usual attributes
mlreg.best_score_
mlreg.best_estimator_

# Check the score
mlreg.score(X=X_test,y=y_test)

#------------------------------------------------------------------------------
# RF
#------------------------------------------------------------------------------
# Instantiate model
rf = RF(max_n_models=2)

# Fit
rf.fit(X=X_train, y=y_train)

# Predict and score
rf.score(X=X_test,y=y_test)

#------------------------------------------------------------------------------
# XGBoost
#------------------------------------------------------------------------------
# Instantiate model
xgb = MLRegressor(estimator=XGBRegressor(),
                  max_n_models=2)

xgb.get_params()

# Fit
xgb.fit(X=X_train, y=y_train)

# Predict and score
xgb.score(X=X_test,y=y_test)


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
xgb.get_params()

xgb.param_grid

from mlregression.estimator import boosting
estimator=XGBRegressor()

estimator.get_params()
rf.get_params()















