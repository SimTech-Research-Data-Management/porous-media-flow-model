import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field


@forge_signature
class Software(sdRDM.DataModel):

    """This is a container for general information about the used software."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("softwareINDEX"),
        xml="@id",
    )
    manufacturer: str = Field(
        ...,
        description="Name of the used recording software manufacturer",
    )

    name: str = Field(
        ...,
        description="Name of the used recording software",
    )

    version: str = Field(
        ...,
        description="Version of the used recording software",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/SimTech-Research-Data-Management/porous-media-flow-model.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="0df357be5c077418934ea7ba50004f15e2374916"
    )