from rxconfig import config
import reflex as rx
from monsterapi import client

#create a summary of the setting based on the first prompt and response
def createSettingSummary(prompt, response):
    prompt = "Our previous prompt was \n" + prompt + "\n and your response was \n" + response + "\n Can you update the summary we have so far with the new details, without making it any longer than it was before? Please summarize the single, most important setting aspects and do not provide anything other than a single most important setting."
    

def modifiedCreateImage(summary):
    return summary + "\n Please only have one, colored image that captures the setting without a collage of images. Don't have multiple panels."