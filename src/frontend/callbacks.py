from dash.dependencies import Input, Output
import requests
from src.utils.logger import setup_logger
from src.utils.config import API_URL
from src.frontend.app import app

logger = setup_logger("callbacks")


@app.callback(
    Output("table", "data"),
    Input("interval", "n_intervals"),
    prevent_initial_call=False,
)
def update_table(n):
    try:
        response = requests.get(f"{API_URL}/items")
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        logger.error(f"Error fetching items: {e}")
        return []
