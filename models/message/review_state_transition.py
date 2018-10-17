from .message import Message
from models.types.reference import Reference


class ReviewStateTransition(Message):
    type: 'ReviewStateTransition'
    oldState: Reference
    newState: Reference
    oldIncludedInStatistics: bool
    newIncludedInStatistics: bool
    target: Reference
    force: bool

    def __init__(self, type: str = 'ReviewStateTransition', oldState: Reference = None, newState: Reference = None, oldIncludedInStatistics: bool = None, newIncludedInStatistics: bool = None, target: Reference = None, force: bool = None, **kwargs):
        super().__init__(**kwargs)
        if oldState is not None:
            if isinstance(oldState, dict):
                self.oldState = Reference(**oldState)
            else:
                self.oldState = oldState
        if newState is not None:
            if isinstance(newState, dict):
                self.newState = Reference(**newState)
            else:
                self.newState = newState
        self.oldIncludedInStatistics = oldIncludedInStatistics
        self.newIncludedInStatistics = newIncludedInStatistics
        if target is not None:
            if isinstance(target, dict):
                self.target = Reference(**target)
            else:
                self.target = target
        self.force = force
