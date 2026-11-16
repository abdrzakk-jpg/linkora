
from loguru import logger
import os


# setup loggers
def setup_logging():
    logger.remove()  # Remove default handler

    log_format = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <level>{message}</level>"
    # Console logging with color and bold text
    logger.add(
        os.sys.stderr,
        format=log_format,
        colorize=True,
        level="INFO"
    )

    # File logging
    logger.add(
        "logs/app.log",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
        rotation="5 MB",
        retention="15 days",
        level="DEBUG"
    )

    # Specific levels
    logger.add(
        os.sys.stderr,
        format=log_format,
        colorize=True,
        level="WARNING"
    )
    logger.add(
        os.sys.stderr,
        format=log_format,
        colorize=True,
        level="ERROR"
    )
    logger.add(
        os.sys.stderr,
        format=log_format,
        colorize=True,
        level="DEBUG"
    )

    return logger

logger = setup_logging()