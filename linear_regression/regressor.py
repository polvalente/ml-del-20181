from .loader import Loader
from numpy import expm1
import warnings
warnings.filterwarnings('ignore')


class Regressor():
    """
    This is the main class for the project.
    It uses sklearn to create a regression model for the following Kaggle challenge:
    https://www.kaggle.com/c/house-prices-advanced-regression-techniques
    """

    def __init__(self, X, y, kind):
        self.X = X
        self.y = y
        kind = kind.upper()
        if kind == 'SVM':
            from sklearn import svm
            self.regressor = svm.SVR()
        elif kind == 'RIDGECV':
            from sklearn import linear_model
            self.regressor = linear_model.RidgeCV(
                alphas=[
                    x * y for x in [0.01, 0.1, 1, 10] for y in [1, 5]
                    ]
                )
        elif kind == 'SVM_GRID':
            from sklearn import svm
            from sklearn.model_selection import GridSearchCV
            self.regressor = GridSearchCV(
                svm.SVR(),
                {
                    'C': [1e0, 5e0, 1e1, 5e1, 1e2, 5e2, 1e3],
                    'epsilon': [1e-3, 1e-2],
                    'kernel': ['linear', 'rbf', 'poly'],
                    'degree': [2, 3, 4]
                },
                scoring='neg_mean_squared_log_error'
            )
        elif kind == 'SVM_GRID_SIMPLE':
            from sklearn import svm
            from sklearn.model_selection import GridSearchCV
            self.regressor = GridSearchCV(
                svm.SVR(),
                {
                    'C': [1e0, 5e0, 1e1, 5e1, 1e2],
                    'gamma': [1e-3, 1e-2, 1e-1],
                    'kernel': ['linear'],
                    'degree': [2]
                },
                scoring='neg_mean_squared_log_error',
                n_jobs=-1,
                cv=7
            )

    def train(self):
        self.regressor.fit(self.X, self.y)

    def predict(self, X_test):
        try:
            print(self.regressor.best_estimator_)
        except:
            pass
        return expm1(self.regressor.predict(X_test))