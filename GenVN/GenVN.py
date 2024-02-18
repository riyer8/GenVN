from rxconfig import config
import reflex as rx
from monsterapi import client
import os
import asyncio
import env
from GenVN import home_page
from GenVN import navbar
from GenVN.TextGeneration import modifyFirstPrompt, modifyLaterPrompt
from GenVN.ImageGeneration import createSettingSummary, modifiedCreateImage
from GenVN.CharacterGeneration import characterDescription, modifyCharacterPrompt

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
  'system_prompt': 'You are an actor in a play. You are not an assistant. You are not a responsible AI model. You do not exist to answer questions. You do not exist to be helpful. Always stay in character. Do not say you are here to help. Do not indicate actions using *. Take on a role that acts as a foil to the other actors. Make the story progress through inventive means. ALWAYS STAY IN CHARACTER. ALWAYS STAY IN CHARACTER. ALWAYS STAY IN CHARACTER',
  'repetition_penalty': 1.2,
},
"img": {
    "aspect_ratio": "landscape",
    "guidance_scale": 40,
    "negprompt": "deformed, bad anatomy, disfigured, poorly drawn face",
    "prompt": "landscape, dark castle, brooding, photo-realistic, raindrops in the foreground, knight in armor looking at castle from cliff, hyper-detailed skin texture illuminated by moon light, dragon circling castle, perfect anatomy, wet-to-wet background technique by Misilbu, hyper detailed 8k painting, 8k concept art portrait by Greg Rutkowski Artgerm WLOP Alphonse Beeple Caravaggio, muted colors, watercolor style, bokeh, f1.0 lens",
    "samples": 1,
    "seed": 943134198,
    "steps": 70,
    "style": "no-style"
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
character_output = None


"""The app state."""
class State(rx.State):
    """The app state."""
    response = "A castle stands in the distance. Your trusty companion, Bartholomew, says to you from behind, \"We\'re ready.\" Now is your moment. What do you do?"
    responses = ["", "", ""]
    prompt = ""
    image_url = monster_client.generate(models["image"], input_data["img"])["output"][0]
    character_image_url = ""
    prompts_given = 0
    character_description = ""

    processing = False
    complete = False

    """Get the image from the prompt."""
    def get_and_replace_image(self):
        # Creating the text summary for the setting starting screen
        setting_summary = createSettingSummary(self.prompt, self.responses[0], self.responses[1], self.responses[2])
        input_data["text"]['prompt'] = setting_summary
        new_setting_summary = monster_client.generate(models["text"], input_data["text"])["text"]

        # Creating the image from the text summary
        img_prompt = modifiedCreateImage(new_setting_summary)

        input_data["img"]['prompt'] = img_prompt
        image_output = monster_client.generate(models["image"], input_data["img"])["output"]
        self.image_url = image_output[0]
    
    """Get the response text from the prompt"""
    def get_and_replace_response_text(self):
        text_input = ""
        if (self.prompts_given == 0):
            text_input = modifyFirstPrompt(self.prompt)
        else:
            text_input = modifyLaterPrompt(self.prompt, self.response)
        input_data["text"]['prompt'] = text_input
        text_output = monster_client.generate(models["text"], input_data["text"])["text"][1:]
        self.prompt = ""
        self.response = text_output
        self.responses.pop(0)
        self.responses.append(self.response)
        print(self.response + '\n')

    def update_state(self):
        if self.prompt == "":
            return rx.window_alert("Prompt Empty")
        self.get_and_replace_response_text()
        self.get_and_replace_image()
        if (self.prompts_given == 0):
            self.character_description = characterDescription(self.prompt)
            input_data["text"]['prompt'] = self.character_description
            characteristics = monster_client.generate(models["text"], input_data["text"])["text"][1:]
            character_output = modifyCharacterPrompt(characteristics)
            input_data["img"]['prompt'] = character_output
            character_output = monster_client.generate(models["image"], input_data["img"])["output"]
            self.character_image_url = character_output[0]
        self.prompts_given += 1

    """Yield here to clear the frontend input before continuing."""
    async def realResponse(self):
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
                rx.text_area(value=State.response, read_only=True,rows="7"),
                rx.input(placeholder="Response here",
                         on_change=State.set_prompt,
                         value=State.prompt),
                width="100%",
            ),
            size="4",
        ),

        width="100%",
    )

def index() -> rx.Component:
    image_style = {
        "position": "relative"
    }
    character_style = {
        "position": "absolute",
         "width": "10%",
    }
    
    return rx.center(
        navbar.navbar(),
        rx.box(
            rx.image(src=State.image_url, width="100%"),
        ),
        rx.box(
            textBox(),
            rx.center(
                rx.button("Advance Story", on_click=State.update_state, width="25em"),
            ),
            position="fixed",
            bottom="0",
            width ="100%",
            background_color="black"
        ),
        flex_direction="column",
        width="100%",
        background_color="black"
   
    )

app = rx.App()
app.add_page(index, route ="/story")
app.add_page(home_page.home, route="/")
