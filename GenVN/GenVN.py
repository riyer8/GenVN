from rxconfig import config
import reflex as rx
from monsterapi import client
import os
import env

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"

# Monster API client and request base info
#monster_client = client(os.environ["MONSTER_API_KEY"])
#models = {"text": 'llama2-7b-chat', "image": 'sdxl-base', "img_mod": 'photo-maker'}
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
  'prompt': 'HD photo of an astronaut with the face of a tiger, sitting in a forest, looking at the sunset, surreal',
  'negprompt': 'unreal, fake, meme, joke, disfigured, poor quality, bad, ugly',
  'samples': 2,
  'steps': 50,
  'aspect_ratio': 'square',
  'guidance_scale': 7.5,
  'seed': 2414,
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

class State(rx.State):
    """The app state."""
    prompt = ""
    background_image_url = ""
    character_image_url = ""

    processing = False
    complete = False
    # Returns llama generated text
    # result = monster_client.generate(models["text"], input_data["text"])

    def get_image(self):
        """Get the image from the prompt."""
        if self.prompt == "":
            return rx.window_alert("Prompt Empty")  
        self.background_image_url = "/favicon.ico" #Here we can get the api involved to get the image
        self.prompt = ""

    def get_character(self):
        """to get the character"""
        if self.prompt == "":
            return rx.window_alert("Prompt Empty")  
        self.character_image_url = "/favicon.ico" #Here we can get the api involved to get the image for charcter
        self.prompt = ""




def textBox() -> rx.Component:
     return rx.box(
        rx.container(
            rx.card(
                rx.text_area(value=State.prompt, read_only=True),
                rx.input(placeholder="Response here",
                         on_change=State.set_prompt,
                         value=State.prompt),
                width="100%",
            ),
            size="4",
        ),
        background_color="var(--gray-3)",
        width="100%",
    )




def index() -> rx.Component:
    image_style = {
        "position": "relative"
    }
    character_style = {
        "position": "absolute",
        # "bottom": "0",
        # "right": "0",
         "width": "10%", 
        #"height": "auto"
    }
    
    return rx.center(
        rx.box(
            rx.image(src=State.background_image_url, width="20em"),
            rx.image(src=State.character_image_url, width="20em"),
            #style=image_style
        ),
        textBox(),
        rx.button("Generate Image", on_click=State.get_image, width="25em"),
        rx.button("Generate Character Image", on_click=State.get_character, width="25em"),
        flex_direction="column",
        width="100%",
    )

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
    


app = rx.App()
app.add_page(index, route ="/story")
app.add_page(home, route="/")
