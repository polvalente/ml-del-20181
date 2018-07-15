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
    "OverallQual",
    "OverallCond",
    "YearBuilt",
    "YearRemodAdd",
    "ExterQual",
    "ExterCond",
    "BsmtQual",
    "BsmtCond",
    "BsmtExposure",
    "BsmtFinType1",
    "BsmtFinType2",
    "KitchenQual",
    "FireplaceQu",
    "GarageYrBlt",
    "GarageFinish",
    "GarageQual",
    "GarageCond",
    "PavedDrive",
    "PoolQC",
    "Fence",
    "MoSold",
    "YrSold",
    "SaleCondition"
]

remove = [
]

train_ld = Loader('./linear_regression/dataset/train.csv')
df_train = train_ld.pre_process(categorical, ordinal, remove)
