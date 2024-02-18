from rxconfig import config
import reflex as rx
import os
import env


def navbar():
    nav_style = {
        #"border-bottom-left-radius": "20px",
        #"border-bottom-right-radius": "20px"
    
    }
    return rx.hstack(
    
            rx.container(
            rx.link(rx.heading("GenVN", font_size="2em",color="white"),href="http://localhost:3000/"),
            ),
        
        rx.spacer(),
      
        rx.link(rx.chakra.button("Help"), href="https://www.google.com"),
          
        position="fixed",
        top="0px",
        background_color="black",
        padding="1em",
        height="4em",
        width="100%",
        z_index="5",
        style = nav_style
    )