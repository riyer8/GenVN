# create character description from the prompt
def characterDescription(input):
    return "I'm creating a narrative based on a conversation with myself and a character and the first thing I say to the character is “" + input + "“. Can you create a character that fits the prompt that's starting the narrative and give a list of physical and personality traits? Please make sure to end on a complete sentence and keep it under 800 characters"

# from the text description, modify character prompt for the image
def modifyCharacterPrompt(input):
    return "Given the following characteristics: " + input + "Provide a picture of a character that would embody these characteristics. Make sure it is appropriate and fits the narrative. Make the picture focused on the head and upper body."