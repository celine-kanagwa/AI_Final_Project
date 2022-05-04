import streamlit as st
from BreastData import dataset

dataframe = dataset()

def PredModel():
    st.text("Model Prediction using Logististic ")


    with st.form("ai form"):
        col1, col2, col3 = st.columns(3)

        with col1:
             radius_mean= st.selectbox('Radius Mean',(set(dataframe.data['radius_mean'])))
             texture_mean= st.selectbox('Texture Mean', (set(dataframe.data['texture_mean'])))
             perimeter_mean = st.selectbox('Perimeter',(set(dataframe.data['perimeter_mean'])))
             area_mean= st.selectbox('area',(set(dataframe.data['area_mean'])))
             smoothness_mean = st.selectbox('smoothness',(set(dataframe.data['smoothness_mean'])))
             compactness_mean = st.selectbox('compactness',(set(dataframe.data['compactness_mean'])))
             concavity_mean= st.selectbox('concavity',(set(dataframe.data['concavity_mean'])))
             concave_points_mean = st.selectbox('concave_points',(set(dataframe.data['concave points_mean'])))
             symmetry_mean  = st.selectbox('symmetry',(set(dataframe.data['symmetry_mean' ])))
       
        with col2:
             radius_se= st.selectbox('Radius sd',(set(dataframe.data['radius_se'])))
             texture_se= st.selectbox('Texture sd', (set(dataframe.data['texture_se'])))
             perimeter_se = st.selectbox('Perimeter sd',(set(dataframe.data['perimeter_se'])))
             area_se= st.selectbox('area st',(set(dataframe.data['area_se'])))
             smoothness_se= st.selectbox('smoothness sd',(set(dataframe.data['smoothness_se'])))
             compactness_se = st.selectbox('compactness sd',(set(dataframe.data['compactness_se'])))
             concavity_se= st.selectbox('concavity sd',(set(dataframe.data['concavity_se'])))
             concave_points_se = st.selectbox('concave_points sd ',(set(dataframe.data['concave points_se'])))
             symmetry_se = st.selectbox('symmetry sd',(set(dataframe.data['symmetry_se' ])))

        with col3:
             radius_worst = st.selectbox('Radius worst',(set(dataframe.data['radius_worst'])))
             texture_worst = st.selectbox('Texture worst', (set(dataframe.data['texture_worst'])))
             perimeter_worst  = st.selectbox('Perimeter worst',(set(dataframe.data['perimeter_worst'])))
           



        submitted = st.form_submit_button("Submit")    

    

    