from .loader import Loader
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
        if kind.upper() == 'SVM':
            from sklearn import svm
            self.regressor = svm.SVR()

    def train(self):
        self.regressor.fit(self.X, self.y)

    def predict(self, X_test):
        return self.regressor.predict(X_test)