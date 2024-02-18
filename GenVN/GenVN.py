from rxconfig import config
import reflex as rx
from monsterapi import client
import os
import env

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"

# Monster API client and request base info
monster_client = client(os.environ["MONSTER_API_KEY"])
models = {"text": 'llama2-7b-chat', "image": 'sdxl-base', "img_mod": 'photo-maker'}
input_data = {
"text": {
  'prompt': 'Whats the meaning of life?',
  'top_k': 10,
  'top_p': 0.9,
  'temp': 0.9,
  'max_length': 1000,
  'beam_size': 1,
  'system_prompt': 'You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe...',
  'repetition_penalty': 1.2,
},
"img": {
    "aspect_ratio": "landscape",
    "guidance_scale": 40,
    "negprompt": "deformed, bad anatomy, disfigured, poorly drawn face",
    "prompt": "landscape of an astronaut with the face of a tiger, sitting in a forest, looking at the sunset, surreal",
    "samples": 1,
    "seed": 943134198,
    "steps": 70,
    "style": "anime"
},
"img_mod": {
  "prompt": "a man wearing a leather jacket",
  "init_image_url": "www.example.com/image_jpeg",
  "negprompt": "deformed, bad anatomy, disfigured, poorly drawn face",
  "steps": 40,
  "samples": 1,
  "strength": 40,
  "seed": 2414, 
}}
image_output = None

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
        input_data["img"]['prompt'] = self.prompt # Replace this with auto-determined
        image_output = monster_client.generate(models["image"], input_data["img"])["output"]
        self.image_url = image_output[0]
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
