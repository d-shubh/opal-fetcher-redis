from typing import Optional
from pydantic import Field
from opal_common.fetcher.fetch_provider import BaseFetchProvider
from opal_common.fetcher.events import FetcherConfig, FetchEvent
from opal_common.logger import logger
import redis.asyncio as redis


class RedisFetcherConfig(FetcherConfig):
    fetcher: str = "RedisFetchProvider"
    command: str = Field(..., description="redis command to get data.")


class RedisFetchEvent(FetchEvent):
    """
    A FetchEvent shape for the Redis Fetch Provider.
    """
    fetcher: str = "RedisFetchProvider"
    config: RedisFetcherConfig = None


class RedisFetchProvider(BaseFetchProvider):
    """
    An OPAL custom fetch provider for Redis
    """

    def __init__(self, event: RedisFetchEvent) -> None:
        if event.config is None:
            event.config = RedisFetcherConfig
        super().__init__(event)
        self.connection: Optional[redis.Redis] = None

    def parse_event(self, event: RedisFetchEvent) -> RedisFetchEvent:
        return RedisFetchEvent(**event.dict(exclude={"config"}), config=event.config)

    async def __aenter__(self):
        self._event: RedisFetchEvent

        dsn: str = self._event.url

        self._connection: redis.Redis = redis.Redis.from_url(dsn)
        return self

    async def __aexit__(self, exec_type=None, exec_val=None, tb=None):
        if self.connection:
            await self.connection.aclose()

    async def _fetch_(self):
        self._event: RedisFetchEvent

        if self._event.config is None:
            logger.warning(
                "incomplete fetcher config: redis commands required to fetch data"
            )
            return

        try:
            logger.debug(f"{self.__class__.__name__} fetching from Redis with command: {self._event.config.command}")

            data = await self._connection.execute_command(*self._event.config.command.split())
            return data

        except Exception as e:
            logger.error(f"Failed to fetch data from Redis: {e}")
            return None
