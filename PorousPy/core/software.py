import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Software(sdRDM.DataModel):
    """This is a container for general information about the used software."""

    id: Optional[str] = Field(
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
        default="https://github.com/SimTech-Research-Data-Management/porous-media-flow-model.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="bcd0026275c43b975bd1ffb5d0a0a434786df0e4"
    )
