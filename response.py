## import libraries
from langchain_ollama import OllamaLLM
from crewai import Crew
from crewai import Task
from crewai import Agent
from crewai import Process

# Create an instance of OllamaLLM
ollama_llm = OllamaLLM(
    model="ollama/llama3.1:8b",
    temperature=0.7,
    #num_predict=256,
    # base_url="http://localhost:11434",
    # other params...
)

# Define your agent with LLM
chat_bot = Agent(
    role='Critical Thinker',
    goal='Analyse the text and identify if any conflicting information within',
    llm=ollama_llm,  # Pass the LLM instance here
    verbose=False,
    backstory=(
        'You are a critical thinker who understands details very well and expert negotiator.'
        "You can identify conflicting statements, information in given text"
    ),
)

# Define a task with a description and expected output
chat_task = Task(
    description=('Find if there are any conflicting statement / information in text. \n Text : \n{text}'),
    expected_output="Respond with 'conflict' / 'no conflict'",
    agent=chat_bot,
)

# Define the Crew with agents and tasks
crew = Crew(
    agents=[chat_bot],
    tasks=[chat_task],
)

# Kickoff the Crew with the input query
Text = "After a long day at office, I was going back home in the late evening. Then, I met my friend on the way to office."

result = crew.kickoff(inputs={'text': Text})

# Print the response
print("Response:", result)