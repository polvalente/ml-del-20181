from linear_regression.loader import Loader

categorical = [
    "MSSubClass",
    "MSZoning",
    "Street",
    "Alley",
    "LotShape",
    "LandContour",
    "Utilities",
    "LotConfig",
    "LandSlope",
    "Neighborhood",
    "Condition1",
    "Condition2",
    "BldgType",
    "HouseStyle",
    "RoofStyle",
    "RoofMatl",
    "Exterior1st",
    "Exterior2nd",
    "MasVnrType",
    "MasVnrArea",
    "Foundation",
    "Heating",
    "HeatingQC",
    "CentralAir",
    "Electrical",
    "Functional",
    "GarageType",
    "MiscFeature",
    "SaleType"
    ]

ordinal = [
    {
        "col": "OverallQual",
        "mapping": {
            "Very Excellent": 10,
            "Excellent": 9,
            "Very Good": 8,
            "Good": 7,
            "Above Average": 6,
            "Average": 5,
            "Below Average": 4,
            "Fair": 3,
            "Poor": 2,
            "Very Poor": 1
            }
    },
    {
        "col": "OverallCond",
        "mapping": {
            "Very Excellent": 10,
            "Excellent": 9,
            "Very Good": 8,
            "Good": 7,
            "Above Average": 6,
            "Average": 5,
            "Below Average": 4,
            "Fair": 3,
            "Poor": 2,
            "Very Poor": 1
            }
    },
    {
        "col": "ExterQual",
        "mapping": {
            "Ex": 4,
            "Gd": 3,
            "TA": 2,
            "Fa": 1,
            "Po": 0,
            }
    },
    {
        "col": "ExterCond",
        "mapping": {
            "Ex": 4,
            "Gd": 3,
            "TA": 2,
            "Fa": 1,
            "Po": 0,
            }
    },
    {
        "col": "BsmtQual",
        "mapping": {
            "Ex": 5,
            "Gd": 4,
            "TA": 3,
            "Fa": 2,
            "Po": 1,
            "Na": 0
            }
    },
    {
        "col": "BsmtCond",
        "mapping": {
            "Ex": 5,
            "Gd": 4,
            "TA": 3,
            "Fa": 2,
            "Po": 1,
            "Na": 0
            }
    },
    {
        "col": "BsmtExposure",
        "mapping": {
            "Ex": 5,
            "Gd": 4,
            "TA": 3,
            "Fa": 2,
            "Po": 1,
            "Na": 0
            }
    },
    {
        "col": "KitchenQual",
        "mapping":  {
            "Ex": 5,
            "Gd": 4,
            "TA": 3,
            "Fa": 2,
            "Po": 1
            }
    },
    {
        "col": "FireplaceQu",
        "mapping": {
            "Ex": 5,
            "Gd": 4,
            "TA": 3,
            "Fa": 2,
            "Po": 1,
            "NA": 0
            }
    },
    {
        "col": "PoolQC",
        "mapping": {
            "Ex": 4,
            "Gd": 3,
            "TA": 2,
            "Fa": 1,
            "NA": 0
            }
    },
    {
        "col": "Fence",
        "mapping": {
            "GdPrv": 4,
            "MnPrc": 3,
            "GdWo": 2,
            "MnWw": 1,
            "NA": 0
        }
    },
    {
        "col": "SaleCondition",
        "mapping": {
            "Normal": 5,
            "Abnorml": 4,
            "AdjLand": 3,
            "Alloca": 2,
            "Family": 1,
            "Partial": 0,
        }
    }
]

remove = ["BsmtFinType1", "BsmtFinType2", "GarageFinish", "GarageQual", "GarageCond", "PavedDrive"]

train_ld = Loader('./linear_regression/dataset/train.csv')
df_train = train_ld.preprocess(categorical, ordinal, remove)
