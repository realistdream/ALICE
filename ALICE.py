import openai
import random

# Set up the OpenAI API key
openai.api_key = "<your_api_key>"

# Define the OCEAN personality traits and their associated prompts
personality_traits = {
    "Openness": "As someone open to philosophical questions, what are your thoughts on the possibility of us being in a simulation?",
    "Conscientiousness": "Being conscientious, how would you approach investigating the question of whether or not we are in a simulation?",
    "Extraversion": "As an outgoing individual, how would you engage others in discussions and debates about the simulation hypothesis?",
    "Agreeableness": "As an agreeable person, how would you foster respectful dialogue and consider different perspectives on the simulation theory?",
    "Neuroticism": "Being high in neuroticism, what concerns or doubts do you have about the idea of living in a simulation, and how would you address them?"
}

# Define the number of agents
num_agents = 5

# Generate random OCEAN traits for each agent
agents_traits = [{trait: random.randint(1, 7) for trait in personality_traits.keys()} for i in range(num_agents)]

# Define a function to generate a response from a GPT agent based on their emotional state and the prompt
def generate_response(emotional_state, prompt):
    # Construct the prompt based on the agent's emotional state
    prompt = f"{prompt}\n\nEmotional state: {emotional_state}\n"
    
    # Generate the response using the GPT-3 API
    response = openai.Completion.create(
        engine="davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.8,
    )
    
    # Extract the generated response from the API output
    return response.choices[0].text.strip()

# Simulate social network interactions
for i in range(num_agents):
    for j in range(num_agents):
        if i != j:
            agent1 = agents_traits[i]
            agent1_emotional_state = random.choice(["happy", "angry", "anxious"])
            agent1_traits = ', '.join(f'{k}: {v}' for k, v in agent1.items())
            
            agent2 = agents_traits[j]
            agent2_emotional_state = random.choice(["happy", "angry", "anxious"])
            agent2_traits = ', '.join(f'{k}: {v}' for k, v in agent2.items())
            
            prompt = f"Agent 1 (OCEAN traits: {agent1_traits}): Let's discuss the intriguing question of whether or not we are living in a simulation!\n\n"
            agent1_response = generate_response(agent1_emotional_state, prompt)
            
            prompt = f"Agent 2 (OCEAN traits: {agent2_traits}): I agree, here are my thoughts on the simulation hypothesis.\n\n"
            agent2_response = generate_response(agent2_emotional_state, prompt)
            
            # Print the responses to the console
            print(f"Agent 1 (emotional state: {agent1_emotional_state}, OCEAN traits: {agent1_traits}): {agent1_response}\n")
            print(f"Agent 2 (emotional state: {agent2_emotional_state}, OCEAN traits: {agent2_traits}): {agent2_response}\n")
