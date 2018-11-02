import pandas as pd

print(pd.__version__)


def california_data():
    california_housing_dataframe = pd.read_csv("D:/Documents/Downloads/california_housing_train.csv", sep=",")
    #print(california_housing_dataframe)
    print(california_housing_dataframe.describe())
    print(california_housing_dataframe.head())
    print(california_housing_dataframe.hist('housing_median_age'))


def sample():
    city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
    population = pd.Series([852469, 1015785, 485199])
    date_frame = pd.DataFrame({ 'City name': city_names, 'Population': population })
    return date_frame

ds = sample()
print(ds)
