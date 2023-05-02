import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .software import Software
from .recording import Recording


@forge_signature
class ProcessStep(sdRDM.DataModel):

    """"""

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
        ...,
        description="Resulting video from the processing",
    )

    software: Software = Field(
        ...,
        description="Software that has been used to perform the processing step",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/SimTech-Research-Data-Management/porous-media-flow-model.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="7663b173df67fd6098a9e76ea7a354fcf151c549"
    )
