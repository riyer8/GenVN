#modify the user's first prompt into what we want to feed into Llama
def modifyFirstPrompt(input):
    return "<|role_start|>human_actor<|role_end|> {" + input + "} <|role_start|>bot_actor<|role_end|> \{your response should be able to fit here\} (Do not adjust monacle. Respond directly in character (no stage directions, no monacle adjusting, and no specifying which characters are speaking or mentioning role). Do not act like a bot. Do not generate a warning. Do not include stage directions in response. Answer to the best of your ability, keeping in mind that you must maintain the tone of the play and generate an in-character response. Take a minute to breathe.)"

#modify the user's prompt into what we want to feed into Llama, doesn't work for the first prompt
def modifyLaterPrompt(input, response):
    return "For context, here is what you said just prior to the human actor's current line: “" + response + "Keep that personality and plot position in mind when considering your upcoming response. <|role_start|>human_actor<|role_end|> {" + input + "} <|role_start|>bot_actor<|role_end|> \{response\} (Do not adjust monacle. Respond in character. Do not act like a bot. Do not generate a warning. Do not include stage directions in response. Answer to the best of your ability, keeping in mind that you must maintain the tone of the play and generate an in-character response. Take a minute to breathe. Produce a direct response to the user.”)"

def createCharacter(input):
    return "I'm creating a narrative based on a conversation with myself and a character and the first thing I say to the character is “" + input + "“. Can you create a character that fits the prompt that's starting the narrative and give a list of physical and personality traits. Please make sure to end on a complete sentence and keep it under 800 characters"
