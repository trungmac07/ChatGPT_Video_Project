import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np

import time


import chatgpt
import asyncio
import random

import io
from PIL import Image
import chatgpt  # Assuming you have the chatgpt module installed
import category
import style

import vi2en
import speech_recognition as sr

st.set_page_config(layout="wide")
st.title(':blue[Joy Images]')

st.markdown(style.button_create             , unsafe_allow_html=True)
st.markdown(style.button_clear              , unsafe_allow_html=True)
st.markdown(style.button_selection_disabled , unsafe_allow_html=True)
st.markdown(style.button_selection_enabled  , unsafe_allow_html=True)
st.markdown(style.button_selected           , unsafe_allow_html=True)
st.markdown(style.button_support           , unsafe_allow_html=True)
st.markdown(style.text_m                    , unsafe_allow_html=True)
st.markdown(style.text_l                    , unsafe_allow_html=True)
st.markdown(style.text_xl                   , unsafe_allow_html=True)





if 'selections' not in st.session_state:
    st.session_state.selections = dict()
if 'image' not in st.session_state:
    st.session_state.image = None
if 'srt' not in st.session_state:
    st.session_state.srt = None
if 'speech' not in st.session_state:
    st.session_state.speech = None

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
    
    st.subheader(":red[Các mục đã chọn:]")
    

    ncols = 7
    n = len(st.session_state.selections)

    selectionsVN = list(st.session_state.selections.keys())
    
    nrows = n // ncols
    nodds = n - nrows * ncols
    
    columns = st.columns(ncols)
    
    for i in range(nrows):
        for j in range(ncols):
            button_label = selectionsVN[i*ncols + j]
            with columns[j]:
                st.markdown('''<span class = "button-selected"> </span>''', unsafe_allow_html=True)
                if st.button(button_label, key = button_label+"selection", use_container_width=37):
                    remove_selection(st.session_state.selections, button_label)
                    st.rerun()

    for i in range(nodds):
        button_label = selectionsVN [nrows*ncols + i]
        with columns[i]:
            st.markdown('''<span class = "button-selected"> </span>''', unsafe_allow_html=True)
            if st.button(button_label, key = button_label+"selection", use_container_width=37):
                remove_selection(st.session_state.selections, button_label)
                st.rerun()
    
    st.markdown('<span id="button-clear"></span>', unsafe_allow_html=True)    
    if st.button("Xóa tất cả"):
        st.session_state.selections = dict()
        st.session_state.counter = 0
        st.rerun()
    
    "---"
            

def render_selection_area():

    category_names = list(category.categories.keys())
    st.header(":blue[Lựa Chọn Chủ Đề]")
    st.markdown('<span class = "text-l"> </span>', unsafe_allow_html=True)
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
                if(button_label in st.session_state.selections.keys()):
                    st.markdown('''<span class = "button-selection_enabled"> </span>''', unsafe_allow_html=True)
                    if st.button(button_label):
                        remove_selection(st.session_state.selections, button_label)
                        st.rerun()
                else:
                    st.markdown('''<span class = "button-selection_disabled"> </span>''', unsafe_allow_html=True)
                    if st.button(button_label):
                        add_selection(st.session_state.selections, categoryVN[i*ncols + j], categoryEN[i*ncols + j])
                        st.rerun()

    for i in range(nodds):
        button_label = categoryVN[nrows*ncols + i]
        with columns[i]:
            if(button_label in st.session_state.selections.keys()):
                st.markdown('''<span class = "button-selection_enabled"> </span>''', unsafe_allow_html=True)
                if st.button(button_label, use_container_width=37):
                    remove_selection(st.session_state.selections, button_label)
                    st.rerun()
            else:
                st.markdown('''<span class = "button-selection_disabled"> </span>''', unsafe_allow_html=True)
                if st.button(button_label):
                    add_selection(st.session_state.selections, categoryVN[nrows*ncols + i], categoryEN[nrows*ncols + i])    
                    st.rerun()

    "---"

def render_category_ui():
    render_selection_area()
    render_selected()
    
    st.markdown('<span id="button-create"></span>', unsafe_allow_html=True)    
    create_button = st.button("Sáng Tạo Ảnh Ngay !")
    if create_button:
        with st.spinner('Chờ xíu nhé...'):
            st.session_state.image = bot.create_image_from_selections(st.session_state.selections)
            
        if(st.session_state.image == None):
            st.write(":red[Hãy chọn một vài mục trước]")
        else:
            st.rerun()

    if (st.session_state.image):
        
        st.write("Ảnh Của Bạn")
        st.image(st.session_state.image)



#############################     AREA FOR VOICE     #####################################

def render_voice_ui():
    st.header(":blue[Vẽ Qua Lời Nói]")
    
    isRecording = False
    
    st.markdown('<span id="button-create"></span>', unsafe_allow_html=True)
    record_btn = st.button("Thu âm")    
    if record_btn:
        with st.spinner('Đang thu âm...'):
            with sr.Microphone() as source:
                isRecording = True
                st.spinner("Đang thu âm...")
                try:
                    audio_data = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                except Exception as e:
                    audio_data = None
                
            try:
                st.spinner("Đang nhận diện...")
                st.session_state.speech = recognizer.recognize_google(audio_data, language="vi-VN")  # Specify the language as Vietnamese
            except Exception as e:
                st.session_state.speech = None
                st.write("Không nhận diện được giọng nói")
            
            isRecording = False
                
    if not isRecording and st.session_state.speech:
        st.subheader(":blue[Chỉnh sửa mô tả]")
        st.session_state.speech = st.text_area("Chỉnh sửa mô tả của bạn:", value=st.session_state.speech)
             
    
    
    st.markdown('<span id="button-support" class = "text-l"></span>', unsafe_allow_html=True)   
    ai_sp = st.button("Hỗ trợ bằng AI")
    st.write("AI sẽ giúp bạn làm đoạn yêu cầu của bạn hay hơn từ đó sẽ giúp tạo ra ảnh đẹp hơn.")
    if not isRecording and ai_sp:
        with st.spinner('Chờ xíu nhé...'):
            st.session_state.speech = st.session_state.speech.strip()
            if len(st.session_state.speech) > 0:
                st.spinner('Đang dịch lời nói...')
                success, translated_srt, error_msg = v2e.translateVi2En(st.session_state.speech)
                st.spinner('Đang hỗ trợ bằng AI')
                ai_script = bot.support_script(translated_srt)
                print(ai_script)
                if success:
                    st.spinner('Đang tạo ảnh từ lời nói...')
                    st.session_state.image = bot.create_image_from_script(ai_script)
                else:
                    st.write(f":red[{error_msg}]")
            else:
                st.write(":red[Hãy mô tả bức tranh của bạn trước]")
                st.session_state.image = None
       

    st.markdown('<span id="button-create"></span>', unsafe_allow_html=True)   
    create_btn = st.button("Sáng Tạo Ảnh Ngay!")
    if not isRecording and create_btn:
        with st.spinner('Chờ xíu nhé...'):
            st.session_state.speech = st.session_state.speech.strip()
            if len(st.session_state.speech) > 0:
                st.spinner('Đang dịch lời nói...')
                success, translated_srt, error_msg = v2e.translateVi2En(st.session_state.speech)
                if success:
                    st.spinner('Đang tạo ảnh từ lời nói...')
                    st.session_state.image = bot.create_image_from_script(translated_srt)
                else:
                    st.write(f":red[{error_msg}]")
            else:
                st.write(":red[Hãy mô tả bức tranh của bạn trước]")
                st.session_state.image = None
                
    if st.session_state.image:
        st.write("Ảnh Của Bạn")
        st.image(st.session_state.image)



#############################     AREA FOR SCRIPT     #####################################

def render_script_ui():
    st.header(":blue[Vẽ Qua Lời Văn]")
    st.session_state.srt = st.text_area("Hãy mô tả bức tranh của bạn:", value=st.session_state.srt)
    
    
    st.markdown('<span id="button-support" class = "text-l"></span>', unsafe_allow_html=True)   
    ai_sp = st.button("Hỗ trợ bằng AI")
    st.write("AI sẽ giúp bạn làm đoạn yêu cầu của bạn hay hơn từ đó sẽ giúp tạo ra ảnh đẹp hơn.")
    if ai_sp:
        with st.spinner('Chờ xíu nhé...'):
            st.session_state.srt = st.session_state.srt.strip()
            if len(st.session_state.srt) > 0:
                st.spinner('Đang dịch văn bản...')
                success, translated_srt, error_msg = v2e.translateVi2En(st.session_state.srt)
                if success:
                    st.spinner('Đang tạo ảnh từ văn bản...')
                    ai_script = bot.support_script(translated_srt)
                    st.session_state.image = bot.create_image_from_script(ai_script)
                else:
                    st.write(f":red[{error_msg}]")
            else:
                st.write(":red[Hãy mô tả bức tranh của bạn trước]")
                st.session_state.image = None
    
    
    st.markdown('<span id="button-create"></span>', unsafe_allow_html=True)
    submit_button = st.button("Sáng Tạo Ảnh Ngay!")

    if submit_button:
        with st.spinner('Chờ xíu nhé...'):
            st.session_state.srt = st.session_state.srt.strip()
            if len(st.session_state.srt) > 0:
                st.spinner('Đang dịch văn bản...')
                success, translated_srt, error_msg = v2e.translateVi2En(st.session_state.srt)
                if success:
                    st.spinner('Đang tạo ảnh từ văn bản...')
                    st.session_state.image = bot.create_image_from_script(translated_srt)
                else:
                    st.write(f":red[{error_msg}]")
            else:
                st.write(":red[Hãy mô tả bức tranh của bạn trước]")
                st.session_state.image = None
        
    if st.session_state.image:
        st.write("Ảnh Của Bạn")
        st.image(st.session_state.image)



#############################     APP RUNS     #####################################
def select_tab(tab):
    if(tab == "Lựa Chọn Mục"):
        render_category_ui()

    elif(tab == "Giọng Nói"):
        render_voice_ui()
    
    elif(tab == "Văn Bản"):
        render_script_ui()

    else:
        return False

# Run the Streamlit app
bot = chatgpt.ChatBot()
v2e = vi2en.Vi2En()
recognizer = sr.Recognizer()
select_tab(menu)

