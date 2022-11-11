import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field

from .recording import Recording
from .software import Software


@forge_signature
class ProcessStep(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("processstepINDEX"),
        xml="@id",
    )
    name: str = Field(
        ...,
        description="Name of the processing step",
    )

    processed_recording: Recording = Field(
        description="Resulting video from the processing",
        default=None,
    )

    software: Software = Field(
        description="Software that has been used to perform the processing step",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/SimTech-Research-Data-Management/porous-media-flow-model.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="0df357be5c077418934ea7ba50004f15e2374916"
    )
