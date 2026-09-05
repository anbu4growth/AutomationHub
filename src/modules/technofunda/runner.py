"""
TechnoFunda Runner
Login Test
"""

import random

from src.modules.technofunda.login import login
from src.modules.technofunda.logout import logout
from src.services.logger import logger


def run(page):

    logger.banner()

    try:

        logger.start("TechnoFunda Login")

        login(page)

        page.wait_for_load_state("networkidle")

        wait_minutes = random.randint(5, 10)

        logger.info(
            f"Waiting {wait_minutes} minutes..."
        )

        page.wait_for_timeout(wait_minutes * 60 * 1000)

        logger.start("Logout")

        logout(page)

        logger.finish("Logout")

        logger.finish("TechnoFunda Login")

    except Exception as ex:

        logger.exception(ex)

        raise