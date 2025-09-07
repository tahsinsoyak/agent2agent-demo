# Agent-to-Agent Communication Example: Travel Planner Network

This project demonstrates a sophisticated agent-to-agent communication system using the `python-a2a` library. It features a "Travel Planner Network" where specialized AI agents collaborate to provide comprehensive travel information.

## Project Overview

The core idea is to showcase how different agents, each with a specific domain of expertise, can work together seamlessly through an `AIAgentRouter`. This router intelligently directs user queries to the most appropriate agent, enabling a collaborative problem-solving approach.

## Features

*   **Modular Agent Design:** Each agent (`Weather Agent`, `Attraction Agent`, `Restaurant Agent`) is a standalone service, focusing on a specific aspect of travel planning.
*   **Intelligent Query Routing:** An `AIAgentRouter` (powered by an LLM) analyzes incoming queries and routes them to the most relevant agent within the network.
*   **Collaborative Information Retrieval:** Demonstrates how a complex query can be broken down and handled by multiple specialized agents.
*   **Scalable Architecture:** The `python-a2a` framework allows for easy addition of new agents and expansion of the network's capabilities.

## Agents

### 1. Weather Agent (`weather_agent.py`)
*   **Description:** Provides current weather information for specified cities.
*   **Skills:** `Get Weather` (tags: `weather`, `forecast`, `temperature`)
*   **Port:** `4740`

### 2. Attraction Agent (`attraction_agent.py`)
*   **Description:** Suggests popular tourist attractions for specified cities.
*   **Skills:** `Get Attractions` (tags: `attractions`, `sights`, `tourism`)
*   **Port:** `4741`

### 3. Restaurant Agent (`restaurant_agent.py`)
*   **Description:** Recommends restaurants for a given city and optional cuisine.
*   **Skills:** `Get Restaurants` (tags: `restaurants`, `food`, `dining`)
*   **Port:** `4742`

## Setup Instructions

To run this project, you need to have Python and `uv` (or `pip`) installed.

1.  **Install `python-a2a`:**
    ```bash
    uv pip install python-a2a
    # or using pip:
    # pip install python-a2a
    ```

2.  **Run the Agents:**
    Open **three separate terminal windows** in the project directory (`c:/Users/tahsinsoyak/Desktop/Prompts/agent2agent-demo`). In each terminal, run one of the agent scripts:

    *   **Terminal 1 (Weather Agent):**
        ```bash
        python weather_agent.py
        ```
    *   **Terminal 2 (Attraction Agent):**
        ```bash
        python attraction_agent.py
        ```
    *   **Terminal 3 (Restaurant Agent):**
        ```bash
        python restaurant_agent.py
        ```
    Keep these terminals open and the agents running.

3.  **Run the Agent Network Demonstrator:**
    Open a **fourth terminal window** in the same directory and run the `run_agents.py` script:

    ```bash
    python run_agents.py
    ```

## Usage Example

The `run_agents.py` script contains example queries that demonstrate how the `AIAgentRouter` directs requests to the appropriate agents. When you run `python run_agents.py`, you will see output similar to this:

```
Query: What's the weather in London?
Routing to Weather Agent with 0.XX confidence
Response: The current weather in London is cloudy with a temperature of 15°C.

Query: Tell me about attractions in Paris.
Routing to Attraction Agent with 0.XX confidence
Response: Popular attractions in Paris include the Eiffel Tower, Louvre Museum, and Notre-Dame Cathedral.

Query: Recommend Italian restaurants in London.
Routing to Restaurant Agent with 0.XX confidence
Response: In London, for Italian, I recommend 'Padella' or 'Bocca di Lupo'.

Query: What to eat in New York?
Routing to Restaurant Agent with 0.XX confidence
Response: In New York, I recommend 'Katz's Delicatessen' (Deli) or 'Shake Shack' (Burgers).

Query: Weather in Tokyo?
Routing to Weather Agent with 0.XX confidence
Response: Sorry, I don't have weather information for Tokyo.
```

*(Note: The confidence scores will vary based on the LLM used for routing decisions.)*

## Technologies Used

*   **Python:** The primary programming language.
*   **`python-a2a`:** A framework for building and connecting AI agents.
*   **`uv` (or `pip`):** Python package installer.
*   **LLM (e.g., OpenAI):** Used by the `AIAgentRouter` for intelligent query routing. (Assumes an LLM client is running on `http://localhost:5000/openai` for routing decisions.)
