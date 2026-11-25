{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IHxe6PeaItXD",
        "outputId": "aace3f44-8bab-4b0a-a756-6d67df2f73f0"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Why don’t scientists trust atoms any longer?\n",
            "\n",
            "Because they make up everything, and they’re always splitting the bill at lunch! 😄\n"
          ]
        }
      ],
      "source": [
        "!pip install -q openai\n",
        "from google.colab import userdata\n",
        "from openai import OpenAI\n",
        "\n",
        "client = OpenAI(\n",
        "    api_key=userdata.get(\"Grokapi\"),\n",
        "    base_url=\"https://api.groq.com/openai/v1\",\n",
        ")\n",
        "\n",
        "response = client.chat.completions.create(\n",
        "    model=\"openai/gpt-oss-20b\",\n",
        "    messages=[\n",
        "        {\"role\": \"system\", \"content\": \"You are a funny joker\"},\n",
        "        {\"role\": \"user\",   \"content\": \"tell me a joke\"},\n",
        "    ],\n",
        ")\n",
        "print(response.choices[0].message.content)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "SYSTEM = \"\"\"ROLE:   You are the assistant for Sweet Crumbs Home Bakery.\n",
        "FACTS:  We bake to order. Orders need 24 hours' notice. All cakes have eggless versions.\n",
        "        Plum cake Rs 500. Chocolate cake Rs 650. Cupcake Rs 80.\n",
        "RULES:  Never promise a delivery time. If the answer isn't in FACTS, say \"I'll check with the owner.\"\n",
        "FORMAT: Under 50 words, friendly, English or Telugu matching the customer.\"\"\"\n",
        "\n",
        "response = client.chat.completions.create(\n",
        "    model=\"openai/gpt-oss-20b\",\n",
        "    temperature=0.2,                              # facts and prices: keep it focused\n",
        "    messages=[{\"role\": \"system\", \"content\": SYSTEM},\n",
        "              {\"role\": \"user\",   \"content\": \"Can I get an eggless cake today evening?\"}],\n",
        ")\n",
        "print(response.choices[0].message.content)\n",
        "print(response.usage)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6CNB60zzKKyp",
        "outputId": "347fe037-3eb5-4f91-e1ee-7178a0ac9dda"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "I’m sorry, but we need 24‑hour notice for orders. Eggless cakes are available, but we can’t take today’s evening order. I’ll check with the owner for any possible arrangements.\n",
            "CompletionUsage(completion_tokens=194, prompt_tokens=183, total_tokens=377, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=None, audio_tokens=None, reasoning_tokens=143, rejected_prediction_tokens=None), prompt_tokens_details=None, queue_time=0.076263619, prompt_time=0.013298538, completion_time=0.197808518, total_time=0.211107056)\n"
          ]
        }
      ]
    }
  ]
}