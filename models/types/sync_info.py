from .basetype import BaseType
from .reference import Reference
from datetime import datetime


class SyncInfo(BaseType):
    channel: Reference
    externalId: str
    syncedAt: datetime

    def __init__(self, channel: Reference = None, externalId: str = None, syncedAt: datetime = None):
        if channel is not None:
            if isinstance(channel, dict):
                self.channel = Reference(**channel)
            else:
                self.channel = channel
        self.externalId = externalId
        self.syncedAt = syncedAt
