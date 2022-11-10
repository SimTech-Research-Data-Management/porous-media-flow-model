import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field


@forge_signature
class Recording(sdRDM.DataModel):

    """This is a container for information about the recording parameters"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("recordingINDEX"),
        xml="@id",
    )
    time: float = Field(
        ...,
        description="Value of the investigated time period in s",
    )

    number_of_pictures: int = Field(
        ...,
        description="Value of the total number of pictures which were investigated",
    )

    repetition_rate: float = Field(
        ...,
        description="Value of the recording repetition rate in Hz",
    )

    field_of_view: str = Field(
        ...,
        description="Value of the field of view in m x m",
    )

    resolution: str = Field(
        ...,
        description="Value of the picture resolution in px x px",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/SimTech-Research-Data-Management/porous-media-flow-model.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="53d30eba563d0bc6bcf3db15575fa61d02387eb0"
    )
