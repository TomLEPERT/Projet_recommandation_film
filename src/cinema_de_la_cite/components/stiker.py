import streamlit as st
from typing import List
import streamlit.components.v1 as components

def call_stiker(
    title: str,
    img: str,
    productor: List[str],
    actors: List[str],
    writters: str,
    years: int,
    resumer: str,
    imbdbid: str
):
    html = f"""
<!DOCTYPE html>
<html>
<head>
<style>
.movie-sticker {{
    position: relative;
    width: 200px;
    height: 300px;
    border-radius: 14px;
    overflow: hidden;
    cursor: pointer;
}}

.movie-sticker img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.3s ease;
}}

.movie-hover {{
    position: absolute;
    inset: 0;
    background: rgba(0,0,0,0.85);
    color: white;
    opacity: 0;
    padding: 12px;
    transition: opacity 0.3s ease;
    font-size: 0.85rem;
}}

.movie-sticker:hover img {{
    transform: scale(1.05);
}}

.movie-sticker:hover .movie-hover {{
    opacity: 1;
}}
</style>
</head>

<body>
<div class="movie-sticker">
    <img src="{img}" />
    <div class="movie-hover">
        <h4>{title}</h4>
        <p>
            <b>Production :</b> {", ".join(productor[:2])}<br>
            <b>Acteurs :</b> {", ".join(actors[:3])}<br>
            <b>Année :</b> {years}
        </p>
    </div>
</div>
</body>
</html>
"""
    components.html(html, height=320)
