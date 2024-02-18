from rxconfig import config
import reflex as rx
import os
import asyncio
import env
from GenVN import navbar

def home() -> rx.Component:
    home_style = {
         "display": "flex",
        "flex-direction": "column",
        "align-items": "center",
        "height": "100vh",
        
    }
    title_style = {      
        "font-size": "9rem",
        "font-weight": "bold",
        "margin-bottom": "30px"
    }
    subheading_title = {
        "padding-top": "10px",
        "font-size": "2rem",
        "margin-bottom": "20px"
    }
    return rx.center(
        navbar.navbar(),
        rx.flex(
            rx.container(
            rx.heading("GenVN", style=title_style),
            
                rx.text("A choose your own adventure story powered by LLMs",style=subheading_title),   
            
            
        rx.text("📚 Explore a galaxy of creativity with our AI-powered platform! 🌌 Dive into a universe of possibilities, where every story is unique! Romance, mystery, fantasy, sci-fi, horror – you name it, we've got it! 🚀🔮 Unleash your imagination and craft your own destiny! 🎭📝 Start your adventure today and let the storytelling begin! 🎮"),
           
           
            
            height="auto",
            ),
            direction="column",
            spacing="3",
        ),
        rx.link(rx.button("Get Fantasizing", size = "4")), href="http://localhost:3000/story/"),
        background="#d5ebc7",
        style=home_style
    )

      


