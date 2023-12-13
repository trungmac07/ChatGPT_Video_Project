

import streamlit as st 


button_create = st.markdown(
        """
        <style>
        .element-container:has(style){
            display: none;
        }
        #button-create {
            display: none;
        }
        .element-container:has(#button-create) {
            display: none;
        }
        .element-container:has(#button-create) + div button {
        background-color: #1899D6;
        color: #ffffff;
        border: solid transparent;
        border-radius: 15px;
        border-width: 0 0 4px;
        box-sizing: border-box;
        display: inline-block;
        font-size: 15px;
        font-weight: 700;
        letter-spacing: .8px;
        line-height: 20px;
        margin: 0;
        outline: none;
        overflow: visible;
        padding: 13px 16px;
        text-align: center;
        text-transform: uppercase;
        touch-action: manipulation;
        transform: translateZ(0);
        transition: filter .2s;
        -webkit-user-select: none;
        vertical-align: middle;
        
        }
        .element-container:has(#button-create) + div button:hover 
        {
            background-color: #77eeee; 
            color: #000000;
            font-weight: 1500;
            font-size: 17px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

button_clear = st.markdown(
        """
        <style>
        .element-container:has(style){
            display: none;
        }
        #button-clear {
            display: none;
        }
        .element-container:has(#button-clear) {
            display: none;
        }
        .element-container:has(#button-clear) + div button {
        background-color: #aa1111;
        color: #ffffff;
        border: solid transparent;
        border-radius: 15px;
        border-width: 0 0 4px;
        box-sizing: border-box;
        display: inline-block;
        font-size: 15px;
        font-weight: 700;
        letter-spacing: .8px;
        line-height: 7px;
        margin: 0;
        outline: none;
        overflow: visible;
        padding: 7;
        text-align: center;
        text-transform: uppercase;
        touch-action: manipulation;
        transform: translateZ(0);
        transition: filter .2s;
        -webkit-user-select: none;
        vertical-align: middle;
        
        }
        .element-container:has(#button-clear) + div button:hover 
        {
            background-color: #ee2222; 
            color: #000000;
            font-weight: 1500;
            font-size: 17px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


