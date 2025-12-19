import streamlit as st
from typing import List

def call_stiker(title: str, img: str, 
                productor: List[str], actors: List[str], 
                writters: str, years: int, 
                resumer: str, imbdbid: int):
    hover_html = f"""
    <div style="position: relative; width: 200px; height: 300px;">
        <img src="{img}" style="width: 100%; height: 100%;">
        <div style="
            position: absolute; top: 0; left: 0; width: 100%; height: 100%;
            background-color: black; color: white; opacity: 0; padding: 10px;
        " class="hover-info">
            <b>De :</b> {', '.join(productor)}<br>
            <b>Par :</b> {writters}<br>
            <b>Avec :</b> {', '.join(actors)}<br>
            <b>Année :</b> {years}<br>
            <b>Note IMDB :</b> {imbdbid}
        </div>
    </div>
    <style>div:hover .hover-info {{opacity: 1;}}</style>
    """
    st.markdown(hover_html, unsafe_allow_html=True)
