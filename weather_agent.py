from python_a2a import A2AServer, skill, agent, run_server, TaskStatus, TaskState
import re

@agent(
    name="Weather Agent",
    description="Provides weather information for a given city.",
    version="1.0.0"
)
class WeatherAgent(A2AServer):
    
    @skill(
        name="Get Weather",
        description="Get the current weather for a specified city.",
        tags=["weather", "forecast", "temperature"]
    )
    def get_weather(self, city: str):
        """Get the current weather for a specified city."""
        # Mock implementation for demonstration
        if city.lower() == "london":
            return "The current weather in London is cloudy with a temperature of 15°C."
        elif city.lower() == "paris":
            return "The current weather in Paris is sunny with a temperature of 22°C."
        elif city.lower() == "new york":
            return "The current weather in New York is rainy with a temperature of 10°C."
        else:
            return f"Sorry, I don't have weather information for {city}."
    
    def handle_task(self, task):
        input_message = task.message["content"]["text"]
        
        # Regex to extract city name from the text
        match = re.search(r"weather in (\w+(?: \w+)*)", input_message, re.IGNORECASE)
        
        city = "unknown"
        if match:
            city = match.group(1)
        
        weather_output = self.get_weather(city)
        task.artifacts = [{
                "parts": [{"type": "text", "text": weather_output}]
            }]
        task.status = TaskStatus(state=TaskState.COMPLETED)

        return task

if __name__ == "__main__":
    agent = WeatherAgent()
    run_server(agent, port=4740)
