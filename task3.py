import pandas as pd
import plotly.express as px
import streamlit as st

# Load the CSV file
df = pd.read_csv("listings.csv.gz")

# Create a Streamlit sidebar with widgets
st.sidebar.header("Filter Data")
neighbourhood = st.sidebar.selectbox("neighbourhood", df.neighbourhood.unique())
price_range = st.sidebar.slider("Price Range", min_value=0, max_value=1000, value=(50, 200))
# Filter the data based on the widgets
price = df['price'].str.replace('$','').str.replace(',','')
print(price)
price = price.astype(float)
filtered_df = df[(df.neighbourhood == neighbourhood) & (price >= float(price_range[0])) & (price <= float(price_range[1]))]

# Create a map chart using Plotly
map_fig = px.scatter_mapbox(filtered_df, lat="latitude", lon="longitude", hover_name="name",
                            hover_data=["price"], color="price", zoom=10)
map_fig.update_layout(mapbox_style="open-street-map")
st.plotly_chart(map_fig)

# Create a histogram chart using Plotly
hist_fig = px.histogram(filtered_df, x="price", nbins=20)
st.plotly_chart(hist_fig)
