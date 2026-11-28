# Day 5 -- Memory and RAG

## Project: Sweet Crumbs Bakery AI Agent

This project extends the Day 4 bakery AI agent with Retrieval-Augmented Generation (RAG) and conversation memory. The agent retrieves business information from ChromaDB, remembers customer conversations, automatically selects tools and saves confirmed orders in Google Sheets.

## Objectives

-   Store 20 business facts in ChromaDB, one fact per chunk.
-   Use embeddings and semantic search to retrieve relevant information.
-   Integrate a RAG search tool with the existing agent.
-   Maintain separate customer conversations using thread IDs and a checkpointer.
-   Reduce hallucinations and test the agent with unknown questions.
-   Calculate the test pass rate with a target of at least 80%.

## Technologies Used

-   Python and Google Colab
-   Groq (GPT-OSS-20B)
-   LangChain and LangGraph
-   ChromaDB
-   Pydantic
-   Google Sheets and gspread
-   Pandas

## Agent Tools

  Tool           Purpose
  -------------- --------------------------------------------------------
  `get_price`    Calculates product prices and total cost.
  `is_open`      Provides bakery opening hours.
  `log_order`    Validates and saves confirmed orders in Google Sheets.
  `search_faq`   Retrieves relevant business policies from ChromaDB.

## Working Process

1.  The customer enters a question.
2.  The checkpointer retrieves conversation history using the thread ID.
3.  The Groq agent automatically selects the appropriate tool when needed.
4.  For policy questions, ChromaDB retrieves relevant business facts using semantic search.
5.  The agent generates a response using the available information.
6.  Confirmed orders are saved in Google Sheets.

## Conversation Memory

`InMemorySaver` maintains conversation history for each thread. Different thread IDs keep customer conversations separate. The interactive chatbot automatically generates thread IDs using UUIDs.

## Testing

The test cases cover RAG retrieval, automatic tool selection, model call counting, price calculation, conversation memory, thread isolation, unknown questions, order validation and Google Sheets logging.

Example: Asking about delivery charges should return Rs. 50. Asking for an unknown bakery branch should produce a response acknowledging that the information is unavailable.

**Target pass rate:** 80% or above.

**Actual pass rate:** To be recorded after executing the tests.

## How to Run

1.  Open the notebook in Google Colab.
2.  Install the required libraries.
3.  Configure the Groq API key using Colab Secrets (`Groqapi`).
4.  Authenticate Google Sheets.
5.  Execute all notebook cells in order.
6.  Run the test cases and record the results.
7.  Start the interactive chatbot. Type `new` for a new conversation or `exit` to stop.

## Learning Outcomes

-   Understanding RAG, embeddings and vector databases.
-   Implementing semantic search and tool calling.
-   Managing conversation memory and separate threads.
-   Reducing hallucinations through system instructions.
-   Testing and evaluating an AI agent.

## Limitations

The bakery facts and prices are sample data. In-memory conversation history and ChromaDB data are lost when the runtime restarts. Actual API execution and test results must be verified in Colab.
