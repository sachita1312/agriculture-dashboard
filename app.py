import streamlit as st
import pandas as pd
import plotly.express as px

#load dataset
df=pd.read_csv("final_dataset.csv")

#title
st.title("Smart Agriculture disease monitoring dashboard")

#sidebar
st.sidebar.header("filter option")
crop=st.sidebar.selectbox("select crop",df['crop'].unique())

#filter data
filtered= df[df['crop']==crop]

#show dataset
st.subheader("filtered dataset")
st.dataframe(filtered)

#------visualizations

#1. disease distribution
fig1 = px.bar(filtered, x='disease', title='disease distribution')
st.plotly_chart(fig1)

#2. pie chart
fig2 = px.pie(filtered, names='disease', title='disease percentage')
st.plotly_chart(fig2)

#3. time trend
fig3=px.line(filtered, x='date', y='severity', title='disease trend over time')
st.plotly_chart(fig3)

#footer
st.markdown("### Insights:")
st.write(" Helps farmers identify disease trends")
st.write(" useful for crop health monitoring ")

# deploy output
#Local URL: http://localhost:8501
#Network URL: http://10.249.91.32:8
