# Day 1 – How LLMs Work and First API Call

## Project Overview

This task introduces Large Language Models (LLMs) and demonstrates how to integrate an AI model into a Python application using the Groq API. The case study is an AI-powered customer support chatbot for Sweet Crumbs Home Bakery.

## Objectives

- Understand the fundamentals of LLMs and next-token prediction.
- Learn about tokens, temperature, context windows, memory and hallucinations.
- Connect Python to an LLM through an API.
- Use system prompts to generate relevant, fact-based customer responses.

## Technologies Used

- Python
- Google Colab
- Groq API
- OpenAI Python SDK
- GPT-OSS-20B model (`openai/gpt-oss-20b`)

## Chatbot Features

- Answers questions about bakery products and prices.
- Provides information about eggless cakes and order requirements.
- Uses bakery facts and rules to reduce hallucinations.
- Supports English and Telugu responses through prompt instructions.
- Uses a low temperature of 0.2 for factual responses.

## Working Process

1. Install the OpenAI Python library.
2. Retrieve the API key securely from Google Colab Secrets.
3. Initialize the API client with the Groq endpoint.
4. Define the system prompt with bakery facts and rules.
5. Send the customer question to the model.
6. Extract and display the generated response.

## How to Run

1. Open `task.py` in Google Colab or copy its code into a notebook.
2. Install the required library using `pip install openai`.
3. Add `GROQ_API_KEY` to Colab Secrets and enable notebook access.
4. Execute the code in order and enter or supply a customer question.

**Security:** Never include your actual API key in the source code or upload it to GitHub.

## Sample Input and Expected Output

**Input:** Can I get an eggless cake today evening?

**Expected output:** Eggless cakes are available, but orders require 24 hours' notice, so an order for this evening is not possible.

## Learning Outcomes

- Understanding how LLMs generate responses.
- Making API requests using Python.
- Designing system prompts for business applications.
- Understanding the importance of grounding, token usage and secure API key management.

## Conclusion

This task demonstrates the fundamentals of integrating LLMs into real-world applications through a bakery customer support chatbot and provides a foundation for developing AI agents.
