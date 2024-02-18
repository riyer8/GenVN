from rxconfig import config
import reflex as rx
from monsterapi import client
import os
import asyncio
import env
from GenVN import home_page
from GenVN.TextGeneration import modifyFirstPrompt, createSummary, modifyLaterPrompt, updateSummary
from GenVN.ImageGeneration import createSettingSummary, modifiedCreateImage

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
  'system_prompt': 'You are an actor in a play. You do not exist to answer questions. You do not exist to be helpful. Always stay in character. Take on a role that acts as a foil to the other actors. Make the story progress through inventive means. ALWAYS STAY IN CHARACTER. ALWAYS STAY IN CHARACTER. ALWAYS STAY IN CHARACTER',
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
    response = "Welcome to the world of GenVN! This is the response box; as soon as you write your first prompt, your reply will spawn here."
    prompt = ""
    image_url = "/black_background.jpeg"
    character_image_url = ""
    prompts_given = 0 # Number of prompts inputted thus far
    summary = "" #summary of the story we keep and update constantly

    processing = False
    complete = False
    chat_history = ""
    def get_and_replace_image(self):
        """Get the image from the prompt."""
        # Creating the text summary for the setting
        # starting screen
        setting_summary = ""
        if (self.prompts_given == 0):
            setting_summary = createSettingSummary(self.prompt, "")
        else:
            setting_summary = createSettingSummary(self.prompt, self.response)
        input_data["text"]['prompt'] = setting_summary
        new_setting_summary = monster_client.generate(models["text"], input_data["text"])["text"]
        print(new_setting_summary)
        # Creating the image from the text summary
        img_prompt = modifiedCreateImage(new_setting_summary)

        input_data["img"]['prompt'] = img_prompt
        image_output = monster_client.generate(models["image"], input_data["img"])["output"]
        self.image_url = image_output[0]
    
    def get_and_replace_response_text(self):
        """Get the response text from the prompt"""
        text_input = ""
        if (self.prompts_given == 0):
            text_input = modifyFirstPrompt(self.prompt)
            self.summary = createSummary(self.prompt)
        else:
            text_input = modifyLaterPrompt(self.prompt, self.summary)
            self.summary = updateSummary(self.summary, self.prompt, self.response)
        input_data["text"]['prompt'] = text_input
        text_output = monster_client.generate(models["text"], input_data["text"])["text"][1:]
        self.prompt = ""
        self.response = text_output
        print(self.response + '\n')
        #self.realResponse()
        #print(self.chat_history)

    
    def update_state(self):
        if self.prompt == "":
            return rx.window_alert("Prompt Empty")
        self.get_and_replace_response_text()
        self.get_and_replace_image()
        self.prompts_given += 1

    async def realResponse(self):
        # Yield here to clear the frontend input before continuing.
        await asyncio.sleep(0.1)
        self.chat_history = ""
        print(len(self.response))
        yield

        for i in range(len(self.response)):
            # Pause to show the streaming effect.
            await asyncio.sleep(0.1)
            # Add one letter at a time to the output.
            print(self.chat_history)
            self.chat_history = self.chat_history + self.response[i]
        
            yield


def textBox() -> rx.Component:
     return rx.box(
        rx.container(
            rx.card(
                rx.text_area(value=State.response, read_only=True),
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
            rx.image(src=State.image_url, width="20em"),
            #rx.image(src=State.character_image_url, width="20em"),
            #style=image_style
        ),
        textBox(),
        rx.button("Generate Image", on_click=State.update_state, width="25em"),
        #rx.button("Generate Character Image", on_click=State.get_character, width="25em"),
        flex_direction="column",
        width="100%",
    )


app = rx.App()
app.add_page(index, route ="/story")
app.add_page(home_page.home, route="/")
