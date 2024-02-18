from rxconfig import config
import reflex as rx
import os
import asyncio
import env

def home() -> rx.Component:
    home_style = {
         "display": "flex",
        "flex-direction": "column",
        "align-items": "center",
        # "justify-content": "center",
        "height": "100vh"
    }
    title_style = {      
        "font-size": "7rem",
        "font-weight": "bold",
        "margin-bottom": "20px"
    }
    subheading_title = {
        "font-size": "1.5rem",
        "margin-bottom": "20px"
    }
    return rx.center(
        rx.flex(
            rx.heading("GenVN", style=title_style),
            rx.center(
                rx.text("A choose your own adventure story powered by LLMs",style=subheading_title),   
            ),
            rx.link(rx.button("Get Fantasizing"), href="http://localhost:3000/story/"),
            direction="column",
            spacing="3",
        ),
        style=home_style
    )


