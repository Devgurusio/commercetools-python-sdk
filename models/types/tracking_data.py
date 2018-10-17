from .basetype import BaseType


class TrackingData(BaseType):
    trackingId: str
    carrier: str
    provider: str
    providerTransaction: str
    isReturn: bool

    def __init__(self, trackingId: str = None, carrier: str = None, provider: str = None, providerTransaction: str = None, isReturn: bool = None):
        self.trackingId = trackingId
        self.carrier = carrier
        self.provider = provider
        self.providerTransaction = providerTransaction
        self.isReturn = isReturn
