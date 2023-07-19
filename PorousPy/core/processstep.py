import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .software import Software
from .recording import Recording


@forge_signature
class ProcessStep(sdRDM.DataModel):
    """The Process Step outlines the specific processing steps applied to the flow measurement video data.
    t includes the name of each processing step, the resulting video from the processing, and the software used to post-process the data.
    Additionally, files with the extension ".lvs" from the Davis 10 software can be embedded within this section, providing a comprehensive record of the processing workflow and ensuring the availability of relevant files for reference and replication.
    """

    id: Optional[str] = Field(
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
        default="0a1753bd2d9d680e8290be0d84d604b5bccf852b"
    )
