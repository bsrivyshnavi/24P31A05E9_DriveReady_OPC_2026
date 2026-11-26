# Day 3 – Introduction to AI Agents and LangChain

## Overview

Day 3 focuses on understanding AI agents and building a bakery chatbot using LangChain. The original workshop uses Groq; this implementation uses Google's Gemma model through Ollama in Google Colab, without API keys or API credits.

## Topics Covered

- Chatbots vs AI agents
- Four components of an agent: model, instructions, tools and memory
- ReAct loop: Think → Act → Observe → Repeat
- Traditional, generative and agentic AI
- When to use an agent
- LangChain models, prompt templates and chains
- Conversation memory and automated chatbot testing

## Project: Sweet Crumbs Home Bakery Assistant

The chatbot answers questions about cake prices, eggless options and ordering policies. It remembers previous messages and follows a system prompt containing bakery facts and rules.

## Tech Stack

- Python
- Google Colab
- LangChain
- Ollama
- Gemma 3 (1B)
- CSV for test cases

## How to Run

1. Install Ollama and its required dependencies in Colab.
2. Start the Ollama server and download `gemma3:1b`.
3. Install `langchain-ollama` and initialize `ChatOllama`.
4. Run the chatbot code to create the prompt, chain and conversation history.
5. Create `test1.csv` with the columns `question` and `must_include`.
6. Run `run_tests("test1.csv")` to evaluate the chatbot.

## Workflow

```text
User Question → Prompt Template + History → Gemma Model → Output Parser → Response
```

## Testing

The testing function reads questions from the CSV file, generates answers, checks for expected keywords and displays PASS, FAIL and the overall pass rate.

| Question | Expected keyword |
| --- | --- |
| Do you make eggless cakes? | eggless |
| What is the price of plum cake? | 500 |
| How much do 3 cupcakes cost? | 240 |

## Learning Outcome

Learned how to build a conversational assistant with LangChain, switch model providers, maintain conversation history and evaluate responses using CSV test cases.

## Limitations

- Ollama must be running in the Colab runtime.
- Keyword-based tests do not guarantee complete answer correctness.
- The chatbot does not yet use external tools or perform autonomous actions. Tool integration is introduced on Day 4.
