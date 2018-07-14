# import pandas as pd
# import seaborn as sns
# import numpy as np
# from scipy.stats import norm
# from sklearn.preprocessing import StandardScaler
# from scipy import stats
from .loader import Loader
import warnings
warnings.filterwarnings('ignore')


class Regressor():
    """
    This is the main class for the project.
    It uses sklearn to create a regression model for the following Kaggle challenge:
    https://www.kaggle.com/c/house-prices-advanced-regression-techniques
    """

    def __init__(self, dataset="train"):
        loader = Loader()
        self.train_x, self.train_y = loader.load(dataset)

    def train(self):
        raise NotImplementedError

    def test(self):
        loader = Loader()
        self.test_x, self.test_y = loader.load("test")
