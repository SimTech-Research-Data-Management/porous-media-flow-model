import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from .software import Software
from .video import Video


@forge_signature
class ProcessStep(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("processstepINDEX"),
        xml="@id",
    )

    name: str = Field(..., description="Name of the processing step")

    processed_video: Video = Field(
        description="Resulting video from the processing", default=None
    )

    software: Software = Field(
        description="Software that has been used to perform the processing step",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/SimTech-Research-Data-Management/porous-media-flow-model.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="53d30eba563d0bc6bcf3db15575fa61d02387eb0"
    )
