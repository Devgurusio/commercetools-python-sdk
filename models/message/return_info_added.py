from .message import Message
from models.types.return_info import ReturnInfo


class ReturnInfoAdded(Message):
    type: 'ReturnInfoAdded'
    returnInfo: ReturnInfo

    def __init__(self, type: str = 'ReturnInfoAdded', returnInfo: ReturnInfo = None, **kwargs):
        super().__init__(**kwargs)
        self.deliveryId = deliveryId
        if returnInfo is not None:
            if isinstance(returnInfo, dict):
                self.returnInfo = ReturnInfo(**returnInfo)
            else:
                self.returnInfo = returnInfo
