import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np

import chatgpt
import asyncio
import random

import io
from PIL import Image
import chatgpt  # Assuming you have the chatgpt module installed
import category
import style

st.set_page_config(layout="wide")
st.title(':blue[Joy Images]')



st.markdown(style.button_create, unsafe_allow_html=True)
st.markdown(style.button_clear, unsafe_allow_html=True)
st.markdown(style.button_selection, unsafe_allow_html=True)


if 'selections' not in st.session_state:
    st.session_state.selections = dict()
if 'image' not in st.session_state:
    st.session_state.image = None

################################################################################################################################

# Display Menu 
menu = None
with st.sidebar:
    menu = option_menu("Menu Sáng Tạo", ["Lựa Chọn Mục", "Giọng Nói", "Văn Bản"], icons=["list","mic-fill","type"],
        styles={
        "container": {"font-family" : "Tahoma"},
        "nav-link": {"text-align": "left", "font-family" : "Tahoma", "--hover-color": "#60b4ff","font-size":"17px"},
        "nav-link-selected": {"font-family" : "Tahoma", "font-size":"21px", "font-style" : "bold", "background" : "#60b4ff"},
        },
        menu_icon="three-dots", default_index=0)


#####################################################################################################################################33

#############################     AREA FOR CATEGORY     #####################################

def add_selection(selection_list, key, value):
    selection_list[key] = value
    
def remove_selection(selection_list, key):
    if(key in selection_list):
        selection_list.pop(key)

def render_selected():
    
    st.subheader(":blue[Các mục đã chọn:]")

    st.markdown('<span id="button-clear"></span>', unsafe_allow_html=True)    
    if st.button("Xóa tất cả"):
        st.session_state.selections = dict()
        st.session_state.counter = 0

    ncols = 7
    n = len(st.session_state.selections)

    selectionsVN = list(st.session_state.selections.keys())
    
    nrows = n // ncols
    nodds = n - nrows * ncols
    
    columns = st.columns(ncols)
    
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
            with columns[j]:
                st.markdown('''<span class = "button-selection"> </span>''', unsafe_allow_html=True)
                if st.button(button_label, use_container_width=37):
                    add_selection(st.session_state.selections, categoryVN[i*ncols + j], categoryEN[i*ncols + j])
                   

    for i in range(nodds):
        button_label = categoryVN[nrows*ncols + i]
        with columns[i]:
            st.markdown('''<span class = "button-selection"> </span>''', unsafe_allow_html=True)
            if st.button(button_label, use_container_width=37):
                add_selection(st.session_state.selections, categoryVN[nrows*ncols + i], categoryEN[nrows*ncols + i])

    "---"

def render_category_ui():
    render_selection_area()
    render_selected()
    st.markdown('<span id="button-create"></span>', unsafe_allow_html=True)    
    create_button = st.button("Sáng Tạo Ảnh Ngay !")
    if create_button:
        st.session_state.image = bot.create_image_from_selections(st.session_state.selections)
        if(st.session_state.image== None):
            st.write(":red[Hãy chọn một vài mục trước]")
        else:
            st.rerun()

    if (st.session_state.image):
        st.write("Ảnh Của Bạn")
        st.image(st.session_state.image)



#############################     AREA FOR VOICE     #####################################










#############################     AREA FOR SCRIPT     #####################################












#############################     APP RUNS     #####################################
def select_tab(tab):
    if(tab == "Lựa Chọn Mục"):
        render_category_ui()

    elif(tab == "Giọng Nói"):
        pass
    
    elif(tab == "Văn Bản"):
        pass

    else:
        return False

# Run the Streamlit app
bot = chatgpt.ChatBot()
select_tab(menu)



    