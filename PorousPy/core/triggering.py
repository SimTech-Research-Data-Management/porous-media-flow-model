import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field


@forge_signature
class Triggering(sdRDM.DataModel):

    """This is a container for information regarding of the used triggering system."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("triggeringINDEX"),
        xml="@id",
    )
    recording_mode: str = Field(
        ...,
        description="Type of recording mode (time-based, cyclic time-based, ...)",
    )

    __repo__: Optional[str] = PrivateAttr(default="None")
