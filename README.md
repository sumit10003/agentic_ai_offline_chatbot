# Using CrewAI for Defining and Running AI Agents

In this project, we will use CrewAI, a framework for defining and running AI agents for specific tasks. This project will guide you through setting up an agent, assigning a task, and running the process.

## Steps Overview
Define an Agent with a role, goal, and the LLM model it will use.
Define a Task that associates a description and expected output to the agent.
Initialize a Crew with the agent and task.
Kickoff the Crew with an input query and observe the response.

## Prerequisites
Install the crewai library.
install the LLM model you want to use (ollama-llama3.1:8b).
Set up a Python environment with necessary dependencies.
Code Walkthrough
Below is the implementation to define and use an AI agent for answering queries.


[ ]
## initial setup
### Create an instance of OpenAI's LLM
### Define your agent with OpenAI LLM

## Define the Task
### Define a task with a description and expected output

## Initialize the Crew
### Define the Crew with agents and tasks

## Run the Crew and Get the Response
### Kickoff the Crew with the input query
### Print the response

## Conclusion
This demonstrates the ability to define and execute tasks with CrewAI agents. You can now expand this framework to handle more complex tasks and use cases by modifying the agent's backstory, goals, or associated tasks.