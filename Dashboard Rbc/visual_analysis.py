import streamlit as st
from BreastData import dataset


dataframe = dataset()

def DataAnalysis_section():
    #st.text('Bellow is a Breast Cancer dataset')
    #st.dataframe(dataframe.data.head())

    #st.text('Explotary Data Anlysis')
    #st.text('Removing unneeded feature ')
    #st.dataframe(dataframe.remove_id_unnamed)


     col1, col2 = st.columns(2)

     with col1:
         st.text('Bellow is a Breast Cancer dataset')
         st.dataframe(dataframe.data.head())

     with col2:
          st.text('Explotary Data Anlysis')

          st.dataframe(dataframe.remove_id_unnamed)

    
     st.text('Target Values ')
     Target, Count_Target = dataframe.Target
     st.bar_chart(Target)
        
     st.text("Correlation Graph")
     st.dataframe(dataframe.Corr_graph)   