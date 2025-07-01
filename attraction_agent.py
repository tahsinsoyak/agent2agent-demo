from python_a2a import A2AServer, skill, agent, run_server, TaskStatus, TaskState
import re

@agent(
    name="Attraction Agent",
    description="Suggests popular attractions for a given city.",
    version="1.0.0"
)
class AttractionAgent(A2AServer):
    
    @skill(
        name="Get Attractions",
        description="Get popular attractions for a specified city.",
        tags=["attractions", "sights", "tourism"]
    )
    def get_attractions(self, city: str):
        """Get popular attractions for a specified city."""
        # Mock implementation for demonstration
        if city.lower() == "london":
            return "Popular attractions in London include the Tower of London, British Museum, and Buckingham Palace."
        elif city.lower() == "paris":
            return "Popular attractions in Paris include the Eiffel Tower, Louvre Museum, and Notre-Dame Cathedral."
        elif city.lower() == "new york":
            return "Popular attractions in New York include Times Square, Central Park, and the Statue of Liberty."
        else:
            return f"Sorry, I don't have attraction information for {city}."
    
    def handle_task(self, task):
        input_message = task.message["content"]["text"]
        
        # Regex to extract city name from the text
        match = re.search(r"attractions in (\w+(?: \w+)*)", input_message, re.IGNORECASE)
        
        city = "unknown"
        if match:
            city = match.group(1)
        
        attraction_output = self.get_attractions(city)
        task.artifacts = [{
                "parts": [{"type": "text", "text": attraction_output}]
            }]
        task.status = TaskStatus(state=TaskState.COMPLETED)

        return task

if __name__ == "__main__":
    agent = AttractionAgent()
    run_server(agent, port=4741)
