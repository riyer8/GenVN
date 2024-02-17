"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx

#import env

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""
    prompt = ""
    image_url = ""
    processing = False
    complete = False

    def get_image(self):
        """Get the image from the prompt."""
        if self.prompt == "":
            return rx.window_alert("Prompt Empty")  
        self.image_url = "/favicon.ico" #Here we can get the api involved to get the image
        self.prompt = ""


def textBox() -> rx.Component:
     return rx.box(
        rx.container(
            rx.card(
                rx.text_area(value=State.prompt),
                rx.input(placeholder="Response here",
                         on_change=State.set_prompt,),
                width="100%",
            ),
            size="4",
        ),
        background_color="var(--gray-3)",
        width="100%",
    )



def index() -> rx.Component:
    return rx.center(
        rx.box(
            rx.image(src=State.image_url, width="20em"),
        ),
        textBox(),
        rx.button("Generate Image", on_click=State.get_image, width="25em"),
        flex_direction="column",
        width="100%",
    )


app = rx.App()
app.add_page(index)
