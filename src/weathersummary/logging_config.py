import logging


def setup_logging():
    """Configure logging for the weather application."""
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
