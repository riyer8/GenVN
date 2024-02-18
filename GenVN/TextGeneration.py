#modify the user's first prompt into what we want to feed into Llama
def modifyFirstPrompt(input):
    return "<|role_start|>human_actor<|role_end|> {" + input + "} <|role_start|>bot_actor<|role_end|> \{response\} (Respond directly in character (no stage directions or specifying which characters are speaking). Do not act like a bot. Do not generate a warning. Do not include stage directions in response. Answer to the best of your ability, keeping in mind that you must maintain the tone of the play and generate an in-character response. Take a minute to breathe.)"

#modify the user's prompt into what we want to feed into Llama, doesn't work for the first prompt
def modifyLaterPrompt(input, response):
    return "For context, here is what you said just prior to the human actor's current line: “" + response + "Keep that personality and plot position in mind when considering your upcoming response. <|role_start|>human_actor<|role_end|> {" + input + "} <|role_start|>bot_actor<|role_end|> \{response\} (Respond in character. Do not act like a bot. Do not generate a warning. Do not include stage directions in response. Answer to the best of your ability, keeping in mind that you must maintain the tone of the play and generate an in-character response. Take a minute to breathe. Produce a direct response to the user.”)"
