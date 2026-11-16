"""
Web Search Tool.
"""
import os
from typing import List, Dict, Any

def web_search(query: str, num_results: int = 5) -> List[Dict[str, Any]]:
    api_key = os.getenv("SEARCH_API_KEY", "")
    if not api_key:
        return [{"title": "Placeholder", "url": "", "snippet": "No search API key configured."}]
    return [{"title": "Placeholder", "url": "", "snippet": "Search not implemented."}]
