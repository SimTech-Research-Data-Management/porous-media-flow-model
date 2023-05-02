import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


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
        default="https://github.com/SimTech-Research-Data-Management/porous-media-flow-model.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="217170c9b861fd33ddc40de1715b3fedae23bbe6"
    )
