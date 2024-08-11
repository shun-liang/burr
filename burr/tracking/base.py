import abc

from burr.lifecycle import (
    PostApplicationCreateHook,
    PostEndSpanHook,
    PostRunStepHook,
    PreRunStepHook,
    PreStartSpanHook,
)
from burr.lifecycle.base import DoLogAttributeHook


class SyncTrackingClient(
    PostApplicationCreateHook,
    PreRunStepHook,
    PostRunStepHook,
    PreStartSpanHook,
    PostEndSpanHook,
    DoLogAttributeHook,
    abc.ABC,
):
    """Base class for synchronous tracking clients. All tracking clients must implement from this
    TODO -- create an async tracking client"""

    def copy(self):
        pass


TrackingClient = SyncTrackingClient
