import logging


def setup_logging() -> None:
    """Configure logging for the weather application."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
