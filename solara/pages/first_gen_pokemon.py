import solara as sl
import pandas as pd
import plotly.express as px

df = pd.read_csv("../pokemon_data.csv")
pokemon_df =  df.loc[df["generation"] == 1]



query = sl.reactive("")

gen_list = pokemon_df["generation"].unique().tolist()
slct_gen = sl.reactive(gen_list)

slct_lgnd_gen = sl.reactive(gen_list[0])

attrs = ["height", "weight", "hp", "attack", "defense", "sp_atk", "sp_def", "speed"]
slct_x = sl.reactive("height")
slct_y = sl.reactive("weight")

@sl.component
def Page():
    sl.Title("First gen pokemon dataset visualization")
    with sl.VBox():
        # pokemon dataset
        sl.Markdown("##1st Gen Pokemon Dataset Visualization")            
        sl.InputText("search pokemon by name", value=query, continuous_update=True)
        sl.DataFrame(pokemon_df[pokemon_df["name"].str.contains(query.value)])

        # explore number of pokemon in each generation
        type1_count = pokemon_df.groupby("type1").size().reset_index(name="count")
        type2_count = pokemon_df.groupby("type2").size().reset_index(name="count")

        type1_count_fig = px.pie(type1_count, names="type1", values="count")
        type2_count_fig = px.pie(type2_count, names="type2", values="count")

        with sl.Row():
            with sl.Column():
                sl.Markdown("###Type 1 population")
                sl.FigurePlotly(type1_count_fig)
            with sl.Column():
                sl.Markdown("###Type 2 population")
                sl.FigurePlotly(type2_count_fig)
        
        # explore population of legendary pokemon
        sl.Markdown("##Percentage of legendary")
        pokemon_df["group"] = pokemon_df["special_group"].mask(pokemon_df["special_group"] != "Legendary", "Non-Legendary")
        lgnd_count = pokemon_df.groupby('group').size().reset_index(name='count')
        lgnd_count_fig = px.pie(lgnd_count, names="group", values="count")
        sl.FigurePlotly(lgnd_count_fig)

        # explore pokemon attributes correlation
        sl.Markdown("###Attributes correlation")
        with sl.Row():
            sl.Select("x axis", value=slct_x, values=attrs)
            sl.Select("y axis", value=slct_y, values=attrs)

        attr_fig = px.scatter(pokemon_df, x=slct_x.value, y=slct_y.value)
        sl.FigurePlotly(attr_fig)