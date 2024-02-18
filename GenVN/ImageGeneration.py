# create a summary of the setting based on the first prompt and response
def createSettingSummary(prompt, response1, response2, response3):
    return "The user just said \n" + prompt + "\n. Your response(s) prior to the user's input were \n" + response1 + ", " + response2 + ", " + response3 + ".\n Please describe the environment of this interaction based on the context in a series of randomly-determined contextually based comma-separated keywords and artistic stylings. Be sure to play up the drama and down-play joy/calm. Do not include anything that would create a NSFW image."
    
# modify character descriptions to create the starter character image
def modifiedCreateImage(summary):
    return summary + "\n Please only have one, colored image that captures the setting without a collage of images. Don't have multiple panels."