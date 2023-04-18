import streamlit as stl

stl.title("My Parents New Healthy Diner")

stl.header("Breakfast Menu")

stl.text("🥣 Omega 3 & Blueberry Oatmeal")
stl.text("🥗 Kale, Spinach & Rocket Smoothie")
stl.text("🐔 Hard-Boiled Free-Range Egg")
stl.text("🥑🍞 Avocado Toast")


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
stl.dataframe(my_fruit_list)
