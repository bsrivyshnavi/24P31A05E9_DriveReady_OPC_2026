# Day 3 – Clothing Store AI Agent

## Overview

A conversational AI agent for a clothing store built using Groq and
LangChain. It automatically selects tools, answers customer questions,
calculates order totals and saves confirmed orders to Google Sheets.

## Features

- Automatic tool selection using `@tool`.
- Product price checking and order total calculation.
- Structured order extraction using Pydantic.
- Google Sheets integration using `log_order`.
- Conversation history and interactive chatbot interface.
- Agent trace inspection and model/tool call counting.

## Tasks Covered

1.  Create `check_price` and `calculate_total` tools with clear
    docstrings.
2.  Define a `ClothingOrder` Pydantic model and test structured output
    on five customer messages.
3.  Create a Google Sheet and save orders using `log_order`.
4.  Rename a tool to `tool1`, compare tool selection and restore the
    original tool.
5.  Inspect agent traces using `pretty_print()` and count model and tool
    calls.

## Tech Stack

Python, Groq API, GPT-OSS 120B, LangChain, Pydantic, gspread, Google
Sheets, Google Colab and Gradio (optional).

## How to Run

1.  Open the notebook in Google Colab.
2.  Install the required packages: `langchain`, `langchain-groq`,
    `pydantic` and `gspread`.
3.  Store your Groq API key in Colab Secrets and enable notebook access.
    Match the secret name in the code.
4.  Run the cells in order and authorize Google Sheets access.
5.  Start the interactive chatbot and enter a question. Type `exit` to
    stop the console chatbot.

## Example Interaction

- User: What is the total price of 3 shirts?
- Agent: The total cost is Rs 1500.

The agent uses the price-checking and calculation tools to answer the
question. Confirmed orders can be recorded in Google Sheets with
customer name, product, quantity, size and color.

## Learning Outcomes

- Understand how AI agents select and execute tools.
- Extract structured data from natural language.
- Integrate external storage with an AI agent.
- Understand the importance of tool names and descriptions.
- Build an interactive chatbot with conversation history.

## Notes

Prices and customer records are sample data. Example responses are
illustrative; actual tool selection, call counts and order logging must
be verified by running the notebook. Never commit API keys to GitHub.
