import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
df = pd.read_csv("../pokemon_data.csv")
pokemon_df =  df.loc[df["generation"] == 2]

# explore number of pokemon
st.title("2nd Generation Pokemon Dataset Visualization")
query = st.text_input("search pokemon by name")
pokemons = pokemon_df[pokemon_df["name"].str.contains(query)]
st.metric("Total Pokemon", pokemons.shape[0])
st.dataframe(pokemons)

col1, col2 = st.columns(2, gap="large")

type1_count = pokemon_df.groupby("type1").size().reset_index(name="count")
type2_count = pokemon_df.groupby("type2").size().reset_index(name="count")

type1_count_fig = px.pie(type1_count, names="type1", values="count")
type2_count_fig = px.pie(type2_count, names="type2", values="count")

with col1:
    st.header("Type 1 population")
    st.plotly_chart(type1_count_fig)

with col2:
    st.header("Type 2 population")
    st.plotly_chart(type2_count_fig)

# explore population of legendary pokemon
st.header("Percentage of legendary")
with st.container():
    pokemon_df["group"] = pokemon_df["special_group"].mask(pokemon_df["special_group"] != "Legendary", "Non-Legendary")
    lgnd_count = pokemon_df.groupby('group').size().reset_index(name='count')
    lgnd_count_fig = px.pie(lgnd_count, names="group", values="count")
    st.plotly_chart(lgnd_count_fig)

# explore pokemon attributes correlation
st.header("Attributes correlation")
with st.container():
    attrs = ["height", "weight", "hp", "attack", "defense", "sp_atk", "sp_def", "speed"]
    x = None
    y = None
    attr_col1, attr_col2 = st.columns(2)
    with attr_col1:
        x = st.selectbox("x axis", attrs, index=0)
    with attr_col2:
        y = st.selectbox("y axis", attrs, index=1)
    
    attr_fig = px.scatter(pokemon_df, x=x, y=y)
    st.plotly_chart(attr_fig)