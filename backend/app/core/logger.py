from loguru import logger
import os


# setup loggers
def setup_logging():
    logger.remove()  # Remove default handler

    # Console logging with color and bold text
    logger.add(
        os.sys.stderr,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <level>{message}</level>",
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
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level><b>{level}</b></level> | <level>{message}</level>",
        colorize=True,
        level="WARNING"
    )
    logger.add(
        os.sys.stderr,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level><b>{level}</b></level> | <level>{message}</level>",
        colorize=True,
        level="ERROR"
    )
    logger.add(
        os.sys.stderr,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level><b>{level}</b></level> | <level>{message}</level>",
        colorize=True,
        level="DEBUG"
    )

    return logger

logger = setup_logging()