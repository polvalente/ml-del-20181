from linear_regression.loader import Loader
from linear_regression.dataset import categorical, ordinal, remove
from linear_regression.regressor import Regressor
import pandas as pd
from sys import argv, exit

train_filename = './linear_regression/dataset/train.csv'
test_filename = './linear_regression/dataset/test.csv'

if len(argv[1]) < 2:
    print("Usage: %s <regressor_name>" % argv[0])
    exit(1)

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

# Call regressor
print("Preparing '%s' regressor..." % (argv[1]), end='')
regressor = Regressor(X_train, y_train, argv[1])
print(" Done!\nTraining...", end='')
regressor.train()
print(" Done!\nPredicting...", end='')
y_test = regressor.predict(X_test)
print(" Done!\nSaving data to 'submission.csv'")

output_df = pd.read_csv('linear_regression/dataset/sample_submission.csv')
output_df['SalePrice'] = y_test
output_df.to_csv('linear_regression/submission.csv', index=False)