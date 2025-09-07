from python_a2a import AgentNetwork, A2AClient, AIAgentRouter

# Create an agent network
network = AgentNetwork(name="Travel Planner Network")

# Add agents to the network
network.add("Weather Agent", "http://localhost:4740")
network.add("Attraction Agent", "http://localhost:4741")
network.add("Restaurant Agent", "http://localhost:4742")

# Create a router to intelligently direct queries to the best agent
router = AIAgentRouter(
    llm_client=A2AClient("http://localhost:5000/openai"),  # LLM for making routing decisions
    agent_network=network
)

# Example queries
queries = [
    "What's the weather in London?",
    "Tell me about attractions in Paris.",
    "Recommend Italian restaurants in London.",
    "What to eat in New York?",
    "Weather in Tokyo?"
]

for query in queries:
    print(f"\nQuery: {query}")
    agent_name, confidence = router.route_query(query)
    print(f"Routing to {agent_name} with {confidence:.2f} confidence")

    agent = network.get_agent(agent_name)
    response = agent.ask(query)
    print(f"Response: {response}")
