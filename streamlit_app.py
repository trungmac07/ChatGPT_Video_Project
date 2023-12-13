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
st.title(':blue[Joy Images]')

import style
button_create = style.button_create
button_clear = style.button_clear



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
    
    st.subheader(":blue[Các mục đã chọn:]")

    st.markdown('<span id="button-clear"></span>', unsafe_allow_html=True)    
    if st.button("Xóa tất cả"):
        st.session_state.selections = dict()
        st.session_state.counter = 0

    ncols = 10
    n = len(st.session_state.selections)

    selectionsVN = list(st.session_state.selections.keys())
    
    nrows = n // ncols
    nodds = n - nrows * ncols
    
    columns = st.columns(7)
    
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
    "---"
            

def render_selection_area():

    category_names = list(category.categories.keys())
    st.subheader(":blue[Lựa Chọn Chủ Đề]")
    selection_box = st.selectbox("Hãy lựa chọn chủ đề của bức ảnh", options=category_names)
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

    "---"

def render_ui():
   
    st.markdown('<span id="button-create"></span>', unsafe_allow_html=True)    
    create_button = st.button("Sáng Tạo Ảnh Ngay !")
    if create_button:
        st.session_state.image = bot.create_image_from_selections(st.session_state.selections)
        if(st.session_state.image== None):
            st.write(":red[Please select some contents first]")
        else:
            st.rerun()

    if (st.session_state.image):
        st.write("Ảnh Của Bạn")
        st.image(st.session_state.image)
        
# Run the Streamlit app
bot = chatgpt.ChatBot()
render_selection_area()
render_selection()
render_ui()


# Display the styled button
