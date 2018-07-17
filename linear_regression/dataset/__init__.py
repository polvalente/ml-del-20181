categorical = {
    "MSSubClass": [
        "20",
        "30",
        "40",
        "45",
        "50",
        "60",
        "70",
        "75",
        "80",
        "85",
        "90",
        "120",
        "150",
        "160",
        "180",
        "190"
    ],
    "MSZoning": [
        "A",
        "C",
        "C (all)",
        "FV",
        "I",
        "RH",
        "RL",
        "RP",
        "RM"
    ],
    "Street": [
        "Grvl",
        "Pave"
    ],
    "Alley": [
        "Grvl",
        "Pave",
        "NA"
    ],
    "LotShape": [
        "Reg",
        "IR1",
        "IR2",
        "IR3"
    ],
    "LandContour": [
        "Lvl",
        "Bnk",
        "HLS",
        "Low",
    ],
    "Utilities": [
        "AllPub",
        "NoSewr",
        "NoSeWa",
        "ELO"
    ],
    "LotConfig": [
        "Inside",
        "Corner",
        "CulDSac",
        "FR2",
        "FR3"
    ],
    "LandSlope": [
        "Gtl",
        "Mod",
        "Sev"
    ],
    "Neighborhood": [
        "Blmngtn",
        "Blueste",
        "BrDale",
        "BrkSide",
        "ClearCr",
        "CollgCr",
        "Crawfor",
        "Edwards",
        "Gilbert",
        "IDOTRR",
        "MeadowV",
        "Mitchel",
        "Names",
        "NoRidge",
        "NPkVill",
        "NridgHt",
        "NWAmes",
        "OldTown",
        "SWISU",
        "Sawyer",
        "SawyerW",
        "Somerst",
        "StoneBr",
        "Timber",
        "Veenker",
    ],
    "Condition1": [
        "Artery",
        "Feedr",
        "Norm",
        "RRNn",
        "RRAn",
        "PosN",
        "PosA",
        "RRNe",
        ''"RRAe"
    ],
    "Condition2": [
        "Artery",
        "Feedr",
        "Norm",
        "RRNn",
        "RRAn",
        "PosN",
        "PosA",
        "RRNe",
        "RRAe"
    ],
    "BldgType": [
       "1Fam",
       "2FmCon",
       "Duplex",
       "TwnhsE",
       "TwnhsI"
    ],
    "HouseStyle": [
        "1Story",
        "1.5Fin",
        "1.5Unf",
        "2Story",
        "2.5Fin",
        "2.5Unf",
        "SFoyer",
        "SLvl"
    ],
    "RoofStyle": [
        "Flat",
        "Gable",
        "Gambrel",
        "Hip",
        "Mansard",
        "Shed"
    ],
    "RoofMatl": [
        "ClyTile",
        "CompShg",
        "Membran",
        "Metal",
        "Roll",
        "Tar&Grv",
        "WdShake",
        "WdShngl"
    ],
    "Exterior1st": [
       "AsbShng",
       "AsphShn",
       "BrkComm",
       "BrkFace",
       "CBlock",
       "CemntBd",
       "HdBoard",
       "ImStucc",
       "MetalSd",
       "Other",
       "Plywood",
       "PreCast",
       "Stone",
       "Stucco",
       "VinylSd",
       "Wd Sdng",
       "WdShing"
    ],
    "Exterior2nd": [
       "AsbShng",
       "AsphShn",
       "BrkComm",
       "BrkFace",
       "CBlock",
       "CemntBd",
       "HdBoard",
       "ImStucc",
       "MetalSd",
       "Other",
       "Plywood",
       "PreCast",
       "Stone",
       "Stucco",
       "VinylSd",
       "Wd Sdng",
       "WdShing"
    ],
    "Foundation": [
        "BrkTil",
        "CBlock",
        "PConc",
        "Slab",
        "Stone",
        "Wood"
    ],
    "Heating": [
        "Floor",
        "GasA",
        "GasW",
        "Grav",
        "OthW",
        "Wall",
    ],
    "HeatingQC": [
        "Ex",
        "Gd",
        "TA",
        "Fa",
        "Po"
    ],
    "CentralAir": [
        "N",
        "Y"
    ],
    "Electrical": [
        "SBrkr",
        "FuseA",
        "FuseF",
        "FuseP",
        "Mix"
    ],
    "Functional": [
        "Typ",
        "Min1",
        "Min2",
        "Mod",
        "Maj1",
        "Maj2",
        "Sev",
        "Sal"
    ],
    "GarageType": [
        "2Types",
        "Attchd",
        "Basment",
        "BuiltIn",
        "CarPort",
        "Detchd",
        "NA"
    ],
    "MiscFeature": [
        "Elev",
        "Gar2",
        "Othr",
        "Shed",
        "TenC",
        "NA"
    ],
    "SaleType": [
        "WD",
        "CWD",
        "VWD",
        "New",
        "COD",
        "Con",
        "ConLw",
        "ConLI",
        "ConLD",
        "Oth"
    ]
}
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

remove = [
    "MasVnrArea",
    "MasVnrType",
    "BsmtFinType1",
    "BsmtFinType2",
    "GarageFinish",
    "GarageQual",
    "GarageCond",
    "PavedDrive"
    ]