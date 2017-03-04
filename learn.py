import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, ElasticNet
from sklearn.ensemble import GradientBoostingRegressor

# read data from json
df = pd.read_json("./reviews.json")

# remove empty values
df = df.dropna()

# convert text data to bag of words
count_vect = CountVectorizer()
bag_of_words = count_vect.fit_transform(df['text'])

# our actual data
X = bag_of_words
Y = df['rating']

# split data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.25)

# teach some models
lr = LinearRegression()
lr.fit(X_train, y_train)
print lr.score(X_train, y_train), lr.score(X_test, y_test)

ridge = Ridge()
ridge.fit(X_train, y_train)
print ridge.score(X_train, y_train), ridge.score(X_test, y_test)


en = ElasticNet()
en.fit(X_train, y_train)
print en.score(X_train, y_train), en.score(X_test, y_test)
