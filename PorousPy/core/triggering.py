
from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .device import Device


@forge_signature
class Triggering(Device):
    """This is a container for information regarding of the used triggering system."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("triggeringINDEX"),
        xml="@id",
    )

    recording_mode: str = Field(
        ...,
        description="Type of recording mode (time-based, cyclic time-based, ...)",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/SimTech-Research-Data-Management/porous-media-flow-model.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="9861f1edfafad8d066d12be2808992116bbd3b62"
    )
