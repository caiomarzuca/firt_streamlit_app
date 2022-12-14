import streamlit
import pandas
import requests

streamlit.title('Hello World')

streamlit.header('Breakfast Menu')
streamlit.text('π₯£ Omega 3 & Blueberry Oatmeal')
streamlit.text('π₯ Kale, Spinach & Rocket Smoothie')
streamlit.text('πHard-Boiled Free-Range Egg')
streamlit.text('π₯π Avocato Toast')
streamlit.header('ππ₯­ Build Your Own Fruit Smoothie π₯π')

#Read and display dataframe 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# List of fruits to choose
fruit_selected = streamlit.multiselect("Pick some fruit:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

#Filter the Table Data
fruit_to_show = my_fruit_list.loc[fruit_selected]

streamlit.dataframe(fruit_to_show)

# Resquest -> respose (expeted 200) and header
streamlit.header("Fruityvice Fruit Advice!")

# Text input 
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
# Text box too the fruit name
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# Modeling json data like table view view
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Put de table on the screem
streamlit.dataframe(fruityvice_normalized)
