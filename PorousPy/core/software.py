import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
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
        ..., description="Name of the used recording software manufacturer"
    )

    name: str = Field(..., description="Name of the used recording software")

    version: str = Field(..., description="Version of the used recording software")

    __repo__: Optional[str] = PrivateAttr(default="None")

    __commit__: Optional[str] = PrivateAttr(
        default="4720cfe81270a9ec51f1bb082be79185b982c2b2"
    )
