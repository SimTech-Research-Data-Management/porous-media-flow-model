import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from .software import Software
from .recording import Recording


@forge_signature
class ProcessStep(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("processstepINDEX"),
        xml="@id",
    )

    name: str = Field(..., description="Name of the processing step")

    software: Software = Field(
        description="Software that has been used to perform the processing step",
        default=None,
    )

    processed_recording: Recording = Field(
        description="Resulting video from the processing", default=None
    )

    __repo__: Optional[str] = PrivateAttr(default="None")

    __commit__: Optional[str] = PrivateAttr(
        default="4720cfe81270a9ec51f1bb082be79185b982c2b2"
    )
