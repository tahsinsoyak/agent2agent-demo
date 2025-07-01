from python_a2a import A2AServer, skill, agent, run_server, TaskStatus, TaskState
import re

@agent(
    name="Restaurant Agent",
    description="Recommends restaurants for a given city and cuisine.",
    version="1.0.0"
)
class RestaurantAgent(A2AServer):
    
    @skill(
        name="Get Restaurants",
        description="Get restaurant recommendations for a specified city and cuisine.",
        tags=["restaurants", "food", "dining"]
    )
    def get_restaurants(self, city: str, cuisine: str = "any"):
        """Get restaurant recommendations for a specified city and cuisine."""
        # Mock implementation for demonstration
        if city.lower() == "london":
            if cuisine.lower() == "italian":
                return "In London, for Italian, I recommend 'Padella' or 'Bocca di Lupo'."
            else:
                return "In London, I recommend 'Dishoom' (Indian) or 'Borough Market' for various options."
        elif city.lower() == "paris":
            if cuisine.lower() == "french":
                return "In Paris, for French, try 'Le Comptoir du Relais' or 'Septime'."
            else:
                return "In Paris, I recommend 'L'As du Fallafel' (Middle Eastern) or 'Pink Mamma' (Italian)."
        elif city.lower() == "new york":
            if cuisine.lower() == "pizza":
                return "In New York, for pizza, try 'Joe's Pizza' or 'Roberta's'."
            else:
                return "In New York, I recommend 'Katz's Delicatessen' (Deli) or 'Shake Shack' (Burgers)."
        else:
            return f"Sorry, I don't have restaurant information for {city}."
    
    def handle_task(self, task):
        input_message = task.message["content"]["text"]
        
        # Regex to extract city and optional cuisine from the text
        match = re.search(r"restaurants in (\w+(?: \w+)*)(?: for (\w+))?", input_message, re.IGNORECASE)
        
        city = "unknown"
        cuisine = "any"
        if match:
            city = match.group(1)
            if match.group(2):
                cuisine = match.group(2)
        
        restaurant_output = self.get_restaurants(city, cuisine)
        task.artifacts = [{
                "parts": [{"type": "text", "text": restaurant_output}]
            }]
        task.status = TaskStatus(state=TaskState.COMPLETED)

        return task

if __name__ == "__main__":
    agent = RestaurantAgent()
    run_server(agent, port=4742)
