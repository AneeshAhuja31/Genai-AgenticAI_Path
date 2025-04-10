from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data,columns=iris.feature_names)
    df['species_name'] = iris.target
    return df,iris.target_names

df,target_name = load_data()

model = RandomForestClassifier()
model.fit(df.iloc[:,:-1],df['species_name'])

st.sidebar.title('Input Features')
sepal_length = st.sidebar.slider("Sepal length",float(df['sepal length (cm)'].min()),float(df['sepal length (cm)'].max()))
sepal_width = st.sidebar.slider("Sepal width",float(df['sepal width (cm)'].min()),float(df['sepal width (cm)'].max()))
petal_length = st.sidebar.slider("Petal length",float(df['petal length (cm)'].min()),float(df['petal length (cm)'].max()))
petal_width = st.sidebar.slider("Petal width",float(df['petal width (cm)'].min()),float(df['petal width (cm)'].max()))

prediction = model.predict([[sepal_length,sepal_width,petal_length,petal_width]])
prediction_species = target_name[prediction[0]]

st.write("Prediction")
st.write(f"The predicted species is: {prediction_species}")