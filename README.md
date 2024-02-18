# GenVN (Generative Visual Novel)
Created by: Luis Sanchez, Matt Hsu, Matthew Mattei, Ramya Iyer

## Inspiration
Today, Generative AI offers an impressive number of innovative solutions to previously unsolvable problems. However, the interactions between users and generative AI continue to feel, well, artificial. Generative AI offers the potential for a machine to take on roles that people have previously had to take and, as population decline affects many communities, will be made naturally vacant. To ensure a smoother transition to a world in which Generative AI is commonplace, we need to explore how users and Generative AI interact. To solve this problem, we devised the Generative Visual Novel (GenVN for short), a tool in which users and Generative AI models interact to form a visual narrative.

## What it does
GenVN is designed to offer a “choose your own adventure” style narrative that provides visuals and related dialogue for an educational and engaging experience. Tightly packaged together are an image theater, a dialogue box, and a button to submit inputs. From start to finish, the user is able to type an input to kickstart a story. GenVN then works wonders by combining Stable Diffusion XL and Llama 2 to dually generate response text meant to advance the narrative according to the user’s decisions and represent the scene in color. From there, the back-and-forth, a harmony between machine and man, can continue forever. The only limitation is the user’s appetite for engagement.

## How we built it
For the web app, the base of our application, we utilized Reflex to build our frontend and backend experiences in Python. We brought in components from Reflex’s library, while also folding in our CSS flair, to create our frontend display and constructed our backend in Python. In the next layer, we incorporated Monster API’s Stable Diffusion XL model for image generation and Llama 2’s 7B parameter model for effective narrative text generation. What really makes the project our own, though, has been our unique prompt engineering, carefully designed and tested to hone in on the narrative experience. Through cultivating a number of back-and-forth conversations with these models and utilizing user feedback at each step, we’ve been able to refine the cooperative element of the program.

## Challenges we ran into
When working on this project, problems appeared one after another. From troubleshooting technologies the team had never seen before to struggling to obtain sufficient user feedback, we had to stop, rethink, and rebuild again and again. While we eventually overcame the many small issues we encountered, the greatest challenge we found was our own ambition. We had so many interests and ideas to explore that we never had the time to realize that, even as we finished our project, we were forced to consider what more we could have made. If nothing else, the greatest reconciliation is that, even after Treehacks ends, the chance to make a more perfect GenVN is always ahead of us.

## Accomplishments that we're proud of
We made an entire website from scratch in effectively less than 24 hours. On top of that, it was primarily built upon an API that no member of the team had used before along with a framework that no member of the team had used before. However, most of all, we made a project that captured a piece of our original vision. It may not have been everything we wanted, but it has a piece of the soul of human-AI collaboration that we hoped to better understand. We were able to interact with Generative AI in a new medium that we never had before and share that experience with other students who, like us, want to know what lies on our shared horizon.

## What we learned
Learning new frameworks from scratch and under time constraints is a fun challenge—definitely easier than learning an entirely new language (which was the mistake of some of our members last year)—but still a daunting one. Additionally, finding diverse user feedback from a user base that has a genuine interest in your work is incredibly useful and should be sought out as soon as a minimally viable product exists. Finally, bringing people together who share a vision is what distinguishes an ordinary project from a great one. After all, almost anyone can just work together, but it takes a common heart and mind to endure the real lows and challenges that an ambitious project entails.

## What's Next for Generative Visual Novel (GenVN)
In a word, soul. While cut out of necessity in our demo, we want adaptive character portraits/models (which change based on the tone of the AI’s reply) to be integrated into our narrative experience to represent the characters that the user talks to. We can only really improve further human-AI cooperation if we can put a face to each mechanical voice. Our first step would be to generate base character designs with Stable Diffusion XL and then modify these base models with PhotoMaker (a Monster API model that modifies images based on text) to breathe life into the generated personalities. We also want to implement a streaming stylization to text generation, printing the model’s response to the user one character at a time to give a more human feel to the model and improve the connection between the user and the machine. Finally, we want to implement a chat history system in which the user can easily swap between any moment in the conversation with the models to better enable specific interactions and outcomes in the narrative process.