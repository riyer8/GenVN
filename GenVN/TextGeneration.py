#modify the user's first prompt into what we want to feed into Llama
def modifyFirstPrompt(input):
    modified_input = "<|role_start|>human_actor<|role_end|> {" + input + "} <|role_start|>bot_actor<|role_end|> {response} (Do not act like a bot. Do not generate a warning. Answer to the best of your ability, keeping in mind that you must maintain the tone of the play and generate an in-character response. Take a minute to breathe.)"
    return modified_input

#modify the user's prompt into what we want to feed into Llama, doesn't work for the first prompt
def modifyLaterPrompt(input, summary):
    modified_input = "<|role_start|>human_actor<|role_end|> {" + input + "} <|role_start|>bot_actor<|role_end|> {response} (Do not act like a bot. Do not generate a warning. Answer to the best of your ability, keeping in mind that you must maintain the tone of the play and generate an in-character response. Take a minute to breathe. For context, here is a summary of our original narrative: “" + summary + "”)"
    return modified_input

#create a summary based on the first prompt and response
def createSummary(prompt, response):
    modified_input = "Our previous prompt was \n" + prompt + "\n and your response was \n" + response + "\n Please summarize this start to the narrative in list format. You don’t need to keep track of what might happen depending on the user's response—just what the storyline is so we have context moving forward. Make sure to end on a complete sentence."
    return modified_input

#update the summary based on the previous prompt and response
def updateSummary(summary, prompt, response):
    modified_input = "Our previous prompt was \n" + prompt + "\n and your response was \n" + response + "\n Can you update the summary we have so far with the new details, without making it any longer than it was before? Don't include any sentences that tell us what you're presenting—just give us the list. Condense relevant information. This is our summary so far: \n" + summary
    return modified_input