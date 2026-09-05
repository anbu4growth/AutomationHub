from src.services.logger import logger

logger.banner()

logger.info("Logger initialized")

logger.start("Dashboard")

logger.info("Reading Dashboard")

logger.success("Dashboard uploaded")

logger.warning("This is a warning")

logger.error("This is an error")

logger.finish("Dashboard")