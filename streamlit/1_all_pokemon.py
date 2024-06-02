import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
pokemon_df = pd.read_csv("../pokemon_data.csv")

# pokemon brief introduction
st.image("./static/pokemon.png",caption="Pokemon gotta catch em all")
st.markdown("Pokémon is a Japanese media franchise consisting of video games, animated series and films, a trading card game, and other related media. The franchise takes place in a shared universe in which humans co-exist with creatures known as Pokémon, a large variety of species endowed with special powers. The franchise's target audience is children aged 5 to 12 but it is known to attract people of all ages.")
st.markdown("The Pokémon franchise is set in a world in which humans coexist with creatures known as Pokémon.Pokémon Red and Blue contain 151 Pokémon species, with new ones being added in subsequent games; as of January 2024, 1,025 Pokémon species have been introduced. Most Pokémon are inspired by real-world animals.")
st.text("Nintendo, if you see this, please don't sue me!")
st.divider()

# pokemon dataset
st.title("Pokemon Dataset Visualization")
query = st.text_input("search pokemon by name")
st.dataframe(pokemon_df[pokemon_df["name"].str.contains(query)])

# explore number of pokemon in each generation
st.header("Number of pokemons in each generation")
gen_list = pokemon_df["generation"].unique()
default_slct = gen_list
slct_gen = st.multiselect("Select generations", gen_list, default_slct, format_func=lambda gen: f"gen {gen}")
gen_count = pokemon_df.loc[pokemon_df["generation"].isin(slct_gen)].groupby("generation").size().reset_index(name="count")
gen_count_fig = px.bar(gen_count, x="generation", y="count",)
st.plotly_chart(gen_count_fig)

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
    compare_with = st.selectbox("Compared to",gen_list, format_func=lambda gen: f"generation {gen}")
    lgnd_col1, lgnd_col2 = st.columns(2)
    
    with lgnd_col1:
        st.subheader("All generation")
        pokemon_df["group"] = pokemon_df["special_group"].mask(pokemon_df["special_group"] != "Legendary", "Non-Legendary")
        lgnd_count = pokemon_df.groupby('group').size().reset_index(name='count')
        lgnd_count_fig = px.pie(lgnd_count, names="group", values="count")
        st.plotly_chart(lgnd_count_fig)

    with lgnd_col2:
        st.subheader(f"Generation {compare_with}")
        genx_df = pokemon_df.loc[pokemon_df["generation"] == compare_with]
        genx_df["group"] = genx_df["special_group"].mask(genx_df["special_group"] != "Legendary", "Non-Legendary")
        lgnd_count = genx_df.groupby('group').size().reset_index(name='count')
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