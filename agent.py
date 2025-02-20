import re
from tools import ecommerce_search_aggregator, shipping_time_estimator, discount_checker, competitor_price_comparison, return_policy_analyzer

class ShoppingAgent:
    def __init__(self):
        self.tools = {
            "search_aggregator": ecommerce_search_aggregator,
            "shipping_estimator": shipping_time_estimator,
            "discount_checker": discount_checker,
            "price_comparator": competitor_price_comparison,
            "return_policy_analyzer": return_policy_analyzer
        }
        self.system_prompt = """
        You are an AI-powered shopping assistant. Your job is to assist users in online shopping by:
        - Searching for products based on criteria like price, size, and availability.
        - Checking shipping times and feasibility based on user location.
        - Validating discount or promo codes and calculating final prices.
        - Comparing competitor prices to find the best deal.
        - Summarizing return policies of different e-commerce platforms.
        Respond concisely and provide structured results.
        """
    
    def reasoning_module(self, query):
        """Determines which tool(s) should be used based on the query."""
        query = query.lower()
        
        if any(keyword in query for keyword in ["find", "search", "show me", "look for", "get"]):
            return "search_aggregator"
        elif any(keyword in query for keyword in ["shipping", "delivery", "arrival", "when will it arrive"]):
            return "shipping_estimator"
        elif any(keyword in query for keyword in ["discount", "promo code", "apply coupon", "sale"]):
            return "discount_checker"
        elif any(keyword in query for keyword in ["compare price", "cheapest", "better deal", "price comparison"]):
            return "price_comparator"
        elif any(keyword in query for keyword in ["return policy", "can I return", "refund", "exchange"]):
            return "return_policy_analyzer"
        else:
            return "Invalid Query"
    
    def process_query(self, query_type, query):
        """Handles the query by extracting relevant details and calling the respective tool."""
        
        if query_type == "search_aggregator":
            match = re.search(r"find (.+?) under (\$\d+)", query, re.IGNORECASE)
            if match:
                product_name = match.group(1)
                price_range = match.group(2)
                size_match = re.search(r"size (\w+)", query, re.IGNORECASE)
                size = size_match.group(1) if size_match else "Unknown"
                return self.tools[query_type](product_name, "any", price_range, size)
        
        elif query_type == "shipping_estimator":
            deadline_match = re.search(r"arrive by (\w+)", query, re.IGNORECASE)
            deadline = deadline_match.group(1) if deadline_match else "Unknown"
            store_match = re.search(r"from (\w+)", query, re.IGNORECASE)
            store = store_match.group(1) if store_match else "StoreA"
            return self.tools[query_type](store, deadline)
        
        elif query_type == "discount_checker":
            match = re.search(r"apply a discount code ‘(.+?)’", query, re.IGNORECASE)
            promo_code = match.group(1) if match else None
            return self.tools[query_type]("Product", 35)
        
        elif query_type == "price_comparator":
            match = re.search(r"compare price of (.+?)", query, re.IGNORECASE)
            product_name = match.group(1) if match else "Unknown"
            return self.tools[query_type](product_name)
        
        elif query_type == "return_policy_analyzer":
            match = re.search(r"return policy of (.+?)", query, re.IGNORECASE)
            store = match.group(1) if match else "Unknown"
            return self.tools[query_type](store)
        
        return "Invalid Query Type"
    
    def respond_to_query(self, query):
        """Processes the query by determining the tool and retrieving relevant data in a structured reasoning format."""
        reasoning = f"I will analyze the query: '{query}' and determine the best tools to use."
        
        tool = self.reasoning_module(query)
        if tool == "Invalid Query":
            return "Sorry, I couldn't process your request."
        
        action = f"Calling the {tool} tool to get relevant information."
        tool_result = self.process_query(tool, query)
        
        observation = f"Tool returned the following information: {tool_result}"
        
        final_response = f"Based on my findings, here is the result:\n{tool_result}"
        
        return {
            "Reasoning": reasoning,
            "Action": action,
            "Observation": observation,
            "Final Response": final_response
        }
    
    def run_demo_tasks(self):
        """Runs predefined demonstration queries and returns results."""
        demo_queries = [
            "Find a floral skirt under $40 in size S. Is it in stock, and can I apply a discount code ‘SAVE10’?",
            "I need white sneakers (size 8) for under $70 that can arrive by Friday.",
            "I found a ‘casual denim jacket’ at $80 on SiteA. Any better deals?",
            "I want to buy a cocktail dress from SiteB, but only if returns are hassle-free. Do they accept returns?",
            "Find running shoes under $80, check reviews, discounts, and fastest shipping.",
            "I need a red dress under $100 that arrives in 3 days. Apply discount and compare prices."
        ]
        
        results = []
        for query in demo_queries:
            response = self.respond_to_query(query)
            results.append({"Task": query, "Result": response})
        return results

if __name__ == "__main__":
    agent = ShoppingAgent()
    demo_results = agent.run_demo_tasks()
    for result in demo_results:
        print(f"\nTask: {result['Task']}\nResult: {result['Result']}")
