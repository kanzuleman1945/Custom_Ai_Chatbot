# Project 1 — Custom AI Chatbot with Memory

## Overview

This project is a terminal-based AI chatbot built with Python and a frontier Large Language Model (LLM).

The chatbot supports conversational interaction and maintains conversation history during an active session. Previous user messages and AI responses are stored in memory and included in subsequent requests, allowing the chatbot to preserve context throughout the conversation.

## Features

- Terminal-based conversational interface
- Integration with a frontier LLM using its official Python SDK
- API key authentication
- In-memory conversation history
- Maintains context across multiple messages
- Stores both user inputs and AI responses
- Simple and interactive command-line interface

## Technologies Used

- Python
- Google GenAI SDK
- Large Language Model (LLM)
- python-dotenv
- Environment variables

## Project Structure

```text
Project1/
│
├── chatbot.py
├── README.md
├── .env
└── .gitignore