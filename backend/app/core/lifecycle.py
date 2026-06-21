import logging

logger = logging.getLogger("agentflow")


async def startup() -> None:
    logger.info("🚀 AgentFlow starting...")


async def shutdown() -> None:
    logger.info("🛑 AgentFlow shutting down...")