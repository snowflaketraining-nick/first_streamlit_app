import streamlit as stl
import streamlit

stl.title("My Parents New Healthy Diner")

stl.header("Breakfast Menu")

stl.text("🥣 Omega 3 & Blueberry Oatmeal")
stl.text("🥗 Kale, Spinach & Rocket Smoothie")
stl.text("🐔 Hard-Boiled Free-Range Egg")
stl.text("🥑🍞 Avocado Toast")


stl.header("🍌🥭 Build Your Own Fruit Smoothie 🥝🍇")

import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index("Fruit")

# Let's put a pick list here so they can pick the fruit they want to include 
stl.multiselect("Pick some fruits:", list(my_fruit_list.index), ["Avocado", "Strawberries"])

# Display the table on the page.

stl.dataframe(my_fruit_list)
