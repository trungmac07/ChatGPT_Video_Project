import streamlit as st
import pandas as pd
import numpy as np

import chatgpt
import asyncio
import random

import io
from PIL import Image
import chatgpt  # Assuming you have the chatgpt module installed
import category


st.set_page_config(layout="wide")
st.title('Hello ChatGPT')


if 'selections' not in st.session_state:
    st.session_state.selections = dict()
if 'image' not in st.session_state:
    st.session_state.image = None

def add_selection(selection_list, key, value):
    selection_list[key] = value
    
def remove_selection(selection_list, key):
    if(key in selection_list):
        selection_list.pop(key)

def render_selection():
    
    st.write("Selected Values:")
    if st.button("Clear"):
        st.session_state.selections = dict()
        st.session_state.counter = 0

    ncols = 10
    n = len(st.session_state.selections)

    selectionsVN = list(st.session_state.selections.keys())
    
    nrows = n // ncols
    nodds = n - nrows * ncols
    
    columns = st.columns(10)
    
    for i in range(nrows):
        for j in range(ncols):
            button_label = selectionsVN[i*ncols + j]
            if columns[j].button(button_label, key = button_label+"selection", use_container_width=37):
                remove_selection(st.session_state.selections, button_label)
                st.rerun()

    for i in range(nodds):
        button_label = selectionsVN [nrows*ncols + i]
        if columns[i].button(button_label, key = button_label+"selection", use_container_width=37):
            remove_selection(st.session_state.selections, button_label)
            st.rerun()
            

def render_selection_area():

    category_names = list(category.categories.keys())
    selection_box = st.selectbox("Selection", options=category_names)
    categoryVN,categoryEN =  list(category.categories[selection_box].keys()) , list(category.categories[selection_box].values())
    
    n = len(categoryVN)
    ncols = 7
    nrows = n // ncols
    nodds = n - nrows * ncols

    columns = st.columns(ncols)
    
    for i in range(nrows):
        for j in range(ncols):
            button_label = categoryVN[i*ncols + j]
            if columns[j].button(button_label, use_container_width=37):
                add_selection(st.session_state.selections, categoryVN[i*ncols + j], categoryEN[i*ncols + j])
                   

    for i in range(nodds):
        button_label = categoryVN[nrows*ncols + i]
        if columns[i].button(button_label, use_container_width=37):
            add_selection(st.session_state.selections, categoryVN[nrows*ncols + i], categoryEN[nrows*ncols + i])

def render_ui():

    if st.button("Create !"):
        st.session_state.image = bot.create_image_from_selections(st.session_state.selections)
        st.rerun()
    
    if (st.session_state.image):
        st.write("YOUR IMAGE")
        st.image(st.session_state.image)
        
# Run the Streamlit app

bot = chatgpt.ChatBot()
render_selection_area()
render_selection()
render_ui()
