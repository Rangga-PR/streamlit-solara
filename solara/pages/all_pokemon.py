import solara as sl
import pandas as pd
import plotly.express as px

pokemon_df = pd.read_csv("../pokemon_data.csv")
pokemon_logo_url = "./static/pokemon.png"

query = sl.reactive("")

gen_list = pokemon_df["generation"].unique().tolist()
slct_gen = sl.reactive(gen_list)

slct_lgnd_gen = sl.reactive(gen_list[0])

attrs = ["height", "weight", "hp", "attack", "defense", "sp_atk", "sp_def", "speed"]
slct_x = sl.reactive("height")
slct_y = sl.reactive("weight")


@sl.component
def Page():
    with sl.AppBarTitle():
        sl.Text("Pokemon dataset visualization")
    with sl.VBox():
        sl.Image(pokemon_logo_url)
        sl.Markdown("Pokémon is a Japanese media franchise consisting of video games, animated series and films, a trading card game, and other related media. The franchise takes place in a shared universe in which humans co-exist with creatures known as Pokémon, a large variety of species endowed with special powers. The franchise's target audience is children aged 5 to 12 but it is known to attract people of all ages.")
        sl.Markdown("The Pokémon franchise is set in a world in which humans coexist with creatures known as Pokémon.Pokémon Red and Blue contain 151 Pokémon species, with new ones being added in subsequent games; as of January 2024, 1,025 Pokémon species have been introduced. Most Pokémon are inspired by real-world animals.")
        sl.Markdown("Nintendo, if you see this, please don't sue me!")
        
        # pokemon dataset
        sl.Markdown("##1st Generation Pokemon Dataset Visualization")            
        sl.InputText("search pokemon by name", value=query, continuous_update=True)
        sl.DataFrame(pokemon_df[pokemon_df["name"].str.contains(query.value)])

        # explore number of pokemon in each generation
        sl.Markdown("##Number of pokemons in each generation")
        sl.SelectMultiple("Select generations", slct_gen, gen_list)
        gen_count = pokemon_df.loc[pokemon_df["generation"].isin(slct_gen.value)].groupby("generation").size().reset_index(name="count")
        gen_count_fig = px.bar(gen_count, x="generation", y="count")
        sl.FigurePlotly(gen_count_fig)

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
        sl.Select("Compared to generation", value=slct_lgnd_gen, values=gen_list)

        with sl.Row():
            with sl.Column():
                sl.Markdown("###All generation")
                pokemon_df["group"] = pokemon_df["special_group"].mask(pokemon_df["special_group"] != "Legendary", "Non-Legendary")
                lgnd_count = pokemon_df.groupby('group').size().reset_index(name='count')
                lgnd_count_fig = px.pie(lgnd_count, names="group", values="count")
                sl.FigurePlotly(lgnd_count_fig)
            with sl.Column():
                sl.Markdown(f"###Generation {slct_lgnd_gen}")
                genx_df = pokemon_df.loc[pokemon_df["generation"] == slct_lgnd_gen.value]
                genx_df["group"] = genx_df["special_group"].mask(genx_df["special_group"] != "Legendary", "Non-Legendary")
                lgnd_count = genx_df.groupby('group').size().reset_index(name='count')
                lgnd_count_fig = px.pie(lgnd_count, names="group", values="count")
                sl.FigurePlotly(lgnd_count_fig)

        # explore pokemon attributes correlation
        sl.Markdown("###Attributes correlation")
        with sl.Row():
            sl.Select("x axis", value=slct_x, values=attrs)
            sl.Select("y axis", value=slct_y, values=attrs)

        attr_fig = px.scatter(pokemon_df, x=slct_x.value, y=slct_y.value)
        sl.FigurePlotly(attr_fig)