import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Pub Locations"
)

df = pd.read_csv("open_pubs_updated.csv")

# make header
st.header("Location of all Bars in UK based on the Local Authority: 🍷🍷🍷")
# enter either postal code or local authority

local_auth = st.selectbox('The Local Authority of the Area which you want to search', set(df['local_authority']))
button_1 = st.button("Submit")

if button_1:
    df_new = df.loc[(df['local_authority'] == local_auth)]
    st.text("The Pubs in this Region are:")
    st.dataframe(df_new)
    st.map(df_new)

# import streamlit as st 
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# from sklearn import preprocessing
# import plotly.express as px

# st.set_page_config(page_title="Unemployment Analysis Web App", page_icon=":smiley:")

# st.title('Hello Friends :smile:')
        
# st.header(' Hii!:wave: I am :green[Om Mahajan], and this is my first-ever web application! :tada:')
    
# st.subheader(" let's Explore this Dataset of Unemployment Analysis of India together!")
# st.subheader(" We are going to explore the unemployment report of India dataset and analyse the unemployment scenario in india. ")

# st.markdown("<h1 style='text-align: center; color:White;'>Unemployment Analysis of India</h1>", unsafe_allow_html=True)

# st.image("https://cdn.pixabay.com/photo/2020/05/03/12/27/recession-5124813__340.jpg", width=710)

# df = pd.read_csv(r"C:\Users\Om\Desktop\Oasis Internship\Final\Unemployment_Rate_upto_11_2020.csv")
# st.header('Statistics of Dataframe')
# st.write(df.describe())

# df.columns= ["States","Date","Frequency",
#                "Estimated Unemployment Rate",
#                "Estimated Employed",
#                "Estimated Labour Participation Rate",
#                "Region","longitude","latitude"]

# st.header('Head of Dataframe')
# st.write(df.head())

# st.header('Tail of the Dataframe')
# st.write(df.tail())

# st.header("Statewise Unemployment Rate")
# statewise_unemployment=df[["States","Estimated Unemployment Rate"]].groupby("States").sum().sort_values(by="Estimated Unemployment Rate", ascending=False)
# st.write(statewise_unemployment.head(15))

# st.header("Statewise Employed per state")
# statewise_employed=df[["States","Estimated Employed"]].groupby("States").sum().sort_values(by="Estimated Employed", ascending=False)
# st.write(statewise_employed.head(15))


# st.header('Correlation Between Data')
# st.write(df.corr())
# st.header('Pairplot')
# sns_plot=sns.pairplot(df, hue='Region',palette='tab10')
# st.pyplot(sns_plot)

# st.header('Heatmap')
# fig = plt.figure(figsize=(10, 8))
# sns.heatmap(df.corr(),cmap="Blues", linecolor='white', linewidths=1,annot=True)
# st.pyplot(fig)

# unemployment=df[["States", "Region","Estimated Unemployment Rate"]]
# fig= px.sunburst(unemployment, path=["Region","States"],
#                    values="Estimated Unemployment Rate",
#                    width=750, height=750, color_continuous_scale="RdY1Gn",
#                    title="Unemployment Rate in India")
# st.plotly_chart(fig)

# fig =px.bar(df, y="Region",color="Region", orientation="h", hover_name="States",
#              color_discrete_map={
#                 "North": "blue",
#                 "South": "green",
#                 "East": "grey",
#                 "West": "orange",
#                 "Northeast": "red"},
#              title="Regionwise Unemployment Rate In India")
# fig.update_layout(yaxis={'categoryorder':'total descending'})

# st.plotly_chart(fig)

# fig=px.bar(df,x='States',y='Estimated Unemployment Rate',color='States',title='Statewise Unemployment Rate In India',template='plotly')
# fig.update_layout(xaxis={'categoryorder':'total descending'})

# st.plotly_chart(fig)