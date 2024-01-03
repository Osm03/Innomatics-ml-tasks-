import streamlit as st
import pandas as pd
from PIL import Image

# base="light"
# primaryColor="#bf1919"
# backgroundColor="#d8ce14"
# secondaryBackgroundColor="#44bb72"
# font="serif"

image = Image.open("dan-gold-t5VKrG0xNtw-unsplash.jpg")

st.set_page_config(
    page_title="Home"
)
# make title and header
st.title("Heyy! Wanna Find Nearest Pub? Come Here ,Let me help you!!🥂🍻")
# st.image(image)
st.image(image)

st.header("Problem Statement: ")

# import the modified data 
df = pd.read_csv("https://raw.githubusercontent.com/sohilsharma1996/Innomatics-Internship-July-2022/main/Open_Pub_Application(Streamlit)/open_pubs_updated.csv")

text='''<div style='text-align:justify'>Let’s assume you are on a Vacation in the United Kingdom with your friends. Just for 
some fun, you decided to go to the Pubs nearby for some drinks. Google Map 
is down because of some issues. 
While searching the internet, you came across https://www.getthedata.com/open-pubs. 
On this website, you found all the pub locations (Specifically Latitude 
and Longitude info). 
In order to impress your frien0
ds, you decided to create a Web Application 
with the data available in your hand. 
'''
st.write(text,unsafe_allow_html=True)
st.header("Available DataSet: ")

# print the data frame
st.dataframe(df.head(11))

st.header("Table representing Columns for DataSet: ")

ds = pd.read_excel("data_dictionary.xlsx")
st.dataframe(ds)

rows = df.count()[0]
columns = df.shape[1] - 1
st.subheader(f'Here , the Total Number of Rows in the data are : {rows}')
st.subheader(f'Here , the Total Number of Columns in the data are : {columns}')

st.header("Basic Statistical Data regarding the DataSet :")
x = df.describe()
x 