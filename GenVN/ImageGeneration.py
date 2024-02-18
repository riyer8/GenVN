from rxconfig import config
import reflex as rx
from monsterapi import client
import os
import asyncio
import env

#create a summary of the setting based on the first prompt and response
def createSettingSummary(prompt, repsonse):
    modified_input = "Our previous prompt was \n" + prompt + "\n and your response was \n" + response + "\n Can you update the summary we have so far with the new details, without making it any longer than it was before? Please summarize the single, most important setting aspects and do not provide anything other than a single most important setting."
    return modified_input

def createImage(summary):
    modified_input = summary + "\n Please only have one, colored image that captures the setting without a collage of images. Don't have multiple panels."
    return modified_input