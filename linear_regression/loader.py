import pandas as pd
from sklearn import preprocessing


class Loader():
    def __init__(self, filename):
        self.filename = filename
        self.data = pd.read_csv(filename)

    def pre_process(self, categorical_col_names, ordinal_col_names, remove_col_names):
        self.data = self.process_ordinal(self.data, ordinal_col_names)
        self.data = self.process_categorical(self.data, categorical_col_names)
        self.data = self.remove(self.data, remove_col_names)
        self.data = self.normalize(self.data)

    def normalize(self, data):
        "normalizes through min-max normalization"
        normalized = (data-data.min())/(data.max() - data.min())
        return normalized

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
            one_hot_encoder = preprocessing.OneHotEncoder(col_names)
            one_hot_encoder.fit(data)
            self.one_hot_encoder = one_hot_encoder

        data = one_hot_encoder.transform(data)
        return data

    def process_ordinal(self, data, col_names, ordinal_encoder=None):
        if ordinal_encoder is None:
            ordinal_encoder = preprocessing.LabelEncoder()
            ordinal_encoder.fit(data[col_names])
        self.ordinal_encoder = ordinal_encoder
        data = ordinal_encoder.transform(data)
        return data

    def remove(self, data, col_names):
        data.drop(col_names)
        return data
