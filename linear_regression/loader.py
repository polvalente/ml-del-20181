import pandas as pd
from sklearn import preprocessing
import category_encoders as ce


class Loader():
    def __init__(self, filename, categorical=None, ordinal=None, remove=None, previous_loader=None):
        self.filename = filename
        self.data = pd.read_csv(self.filename)
        self.preprocess(categorical, ordinal, remove, previous_loader)
        self.data.to_csv(filename+'.ready')

    def __call__(self):
        return self.split_data()

    def preprocess(self, categorical_data, ordinal_mapping, remove_col_names, previous_loader=None):
        if previous_loader is not None:
            ordinal_encoder = previous_loader.ordinal_encoder
            label = previous_loader.label_encoders
            one_hot = previous_loader.one_hot_encoder
            if self.data.shape[1] != previous_loader.data.shape:
                self.data = self.data.join(pd.DataFrame({'SalePrice': [0]*self.data.shape[0]}))
        else:
            ordinal_encoder = None
            label = None
            one_hot = None

        self.data = self.remove(self.data, remove_col_names)
        self.data = self.process_ordinal(self.data, ordinal_mapping, ordinal_encoder)
        self.data = self.process_categorical(self.data, categorical_data, label, one_hot)
        self.data = self.set_nan_to_median(self.data)
        self.data = self.normalize(self.data)
        return self.data

    def set_nan_to_median(self, data):
        data = data.fillna(data.median())
        return data

    def normalize(self, data):
        "normalizes through min-max normalization"
        scaler = preprocessing.MinMaxScaler()
        scaler.fit(data)
        data[data.columns] = scaler.transform(data[data.columns])
        return data

    def process_categorical(self, data, labels, label_encoders=None, one_hot_encoder=None):
        col_names = list(labels.keys())
        data[pd.isnull(data[col_names])].fillna('nan')
        if label_encoders is None:
            label_encoders = []
            for col in col_names:
                label_encoder = preprocessing.LabelEncoder()
                label_encoder.fit(labels[col]+['nan'])
                label_encoders.append(label_encoder)
            self.label_encoders = label_encoders

        for index in range(len(label_encoders)):
            col = col_names[index]
            label_encoder = label_encoders[index]
            try:
                data[col] = label_encoder.transform(data[col].astype(str))
            except ValueError as e:
                print("col: "+col)
                print("file: "+self.filename)
                print(e)
                raise e

        if one_hot_encoder is None:
            one_hot_encoder = ce.one_hot.OneHotEncoder(cols=col_names, return_df=True)
            one_hot_encoder.fit(data)
            self.one_hot_encoder = one_hot_encoder

        data = one_hot_encoder.transform(data)
        return data

    def process_ordinal(self, data, mapping, ordinal_encoder=None):
        if ordinal_encoder is None:
            ordinal_encoder = ce.ordinal.OrdinalEncoder(
                mapping=mapping,
                cols=[m['col'] for m in mapping],
                return_df=True
                )
            ordinal_encoder.fit(data)
            self.ordinal_encoder = ordinal_encoder
        data = ordinal_encoder.transform(data)
        return data

    def remove(self, data, col_names):
        data = data.drop(columns=col_names)
        return data

    def split_data(self):
        try:
            X = self.data.copy().drop(columns=['SalePrice'])
            y = self.data['SalePrice']
        except ValueError:
            X = self.data.copy()
            y = None
        return X, y
