import logging
import os
from datetime import datetime

def set_logger(name, log_dir="logs"):
    """
    Set up a logger with the specified name, logging to both console and a file.
    
    Args:
        name (str): Name of the logger (e.g., "frontend").
        log_dir (str): Directory to store log files (default: "logs").
    
    Returns:
        logging.Logger: Configured logger instance.
    """
    # Create logs directory if it doesn't exist
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Create a logger with the specified name
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Avoid adding handlers if they already exist (prevents duplicate logs)
    if not logger.handlers:
        # Define the log format
        log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Console handler (logs to terminal)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_format)
        logger.addHandler(console_handler)

        # File handler (logs to a file with timestamp)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = os.path.join(log_dir, f"{name}_{timestamp}.log")
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(log_format)
        logger.addHandler(file_handler)

    return logger