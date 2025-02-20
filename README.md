# ALICE

README for ALICE.py
*Overview*
The ALICE.py script simulates social network interactions between agents with randomly assigned personality traits. It uses the OpenAI API to generate responses that simulate a conversation about the hypothesis of living in a simulation. The model utilizes the OCEAN (Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism) personality traits to guide these interactions.

*Key Features*
- OpenAI API Integration: Connecting to OpenAI's API to generate conversational responses via the GPT-3 model.
- OCEAN Personality Traits: Random assignment of personality traits to agents from the OCEAN model.
- Emotional States: Agents interact considering random emotional states including "happy," "angry," and "anxious."
- Multiple Agents Interaction: Simulates discussions among multiple agents to explore how personality and emotions influence conversations.

*Installation*
Clone the repository: 

> bash git clone <repository_url> cd <repository_directory>

Environment Setup: Make sure Python 3.x is installed.

Install Required Packages: The script requires openai and random. Install them using: 

> bash pip install openai

Setup OpenAI API Key: Set your OpenAI API key in the script by replacing the placeholder string in: python openai.api_key = "your_openai_api_key"

*Usage*

Run the script using Python: 

> bash python ALICE.py

This will commence the simulation of social network interactions based on the personality traits and emotional states.

*Functionality*
generate_response(emotional_state, prompt): This function generates a response from a GPT agent. It constructs the prompt using the agent's emotional state and then calls the GPT-3 API to generate a text response.
Simulation Process: Iterates through a loop to pair agents and simulate their interactions. Agent traits are displayed, and the conversation revolves around the simulation hypothesis.

*Use Cases*
Educational Tools: Enhance understanding of personality traits and emotional influence in conversations or decision-making.
Simulation Research: Aid researchers in studying interaction dynamics based on psychological traits.
AI Development: Develop AI models focused on natural language processing and personality-based interaction modeling.

Note
Make sure the API key is kept confidential to prevent unauthorized usage or potential security issues.

License
This project is licensed under the MIT License - see the LICENSE file for details.
