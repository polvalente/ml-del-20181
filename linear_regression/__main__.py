from linear_regression.loader import Loader
from linear_regression.dataset import categorical, ordinal, remove
import pandas as pd

train_filename = './linear_regression/dataset/train.csv'
test_filename = './linear_regression/dataset/test.csv'

# Load training data
print('Loading training data...', end='')
train_loader = Loader(train_filename, categorical, ordinal, remove)
X_train, y_train = train_loader()
print(" Done!\nLoaded training data from file: '"+train_filename+"'")

# Load test data
print('Loading test data...', end='')
test_loader = Loader(test_filename, categorical, ordinal, remove, train_loader)
X_test, _ = test_loader()

print(" Done!\nLoaded test data from file: '"+test_filename+"'")
