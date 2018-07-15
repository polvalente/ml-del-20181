import pandas as pd
from sklearn import preprocessing
import category_encoders as ce


class Loader():
    def __init__(self, filename):
        self.filename = filename
        self.data = pd.read_csv(filename)

    def preprocess(self, categorical_col_names, ordinal_mapping, remove_col_names):
        self.data = self.remove(self.data, remove_col_names)
        self.data = self.process_ordinal(self.data, ordinal_mapping)
        self.data = self.process_categorical(self.data, categorical_col_names)
        self.data = self.set_nan_to_median(self.data)
        self.data = self.normalize(self.data)
        return self.data

    def set_nan_to_median(self, data):
        data = data.fillna(data.median())
        return data

    def normalize(self, data, scaler=None):
        "normalizes through min-max normalization"
        if scaler is None:
            scaler = preprocessing.MinMaxScaler()
            scaler.fit(data)
        data[data.columns] = scaler.transform(data[data.columns])
        return data

    def process_categorical(self, data, col_names, label_encoders=None, one_hot_encoder=None):
        data[pd.isnull(data[col_names])].fillna('nan')
        if label_encoders is None:
            label_encoders = []
            for col in col_names:
                label_encoder = preprocessing.LabelEncoder()
                label_encoder.fit(data[col].astype(str))
                label_encoders.append(label_encoder)
            self.label_encoders = label_encoders

        for index in range(len(label_encoders)):
            col = col_names[index]
            label_encoder = label_encoders[index]
            data[col] = label_encoder.transform(data[col].astype(str))

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
