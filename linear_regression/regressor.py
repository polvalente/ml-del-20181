from .loader import Loader
import warnings
warnings.filterwarnings('ignore')


class Regressor():
    """
    This is the main class for the project.
    It uses sklearn to create a regression model for the following Kaggle challenge:
    https://www.kaggle.com/c/house-prices-advanced-regression-techniques
    """

    def __init__(self, loader, X, y):
        self.X = X
        self.y = y
        self.loader = loader

    def train(self):
        raise NotImplementedError