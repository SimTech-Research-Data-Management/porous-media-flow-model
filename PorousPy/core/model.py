import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .porousmediaparameters import PorousMediaParameters


@forge_signature
class Model(sdRDM.DataModel):

    """This is a container for information about a possible object in/adjascent to the free flow"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("modelINDEX"),
        xml="@id",
    )

    type: str = Field(
        ...,
        description=(
            "What kind of object is located inside the flow channel? (porous media"
            " model, cylinder, ...)"
        ),
    )

    location: str = Field(
        ...,
        description=(
            "Where is the object located inside the flow channel? (in, adjascent to,"
            " ... the free flow)"
        ),
    )

    porous_media: Optional[PorousMediaParameters] = Field(
        default=None,
        description="Description of porous media parameters",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/SimTech-Research-Data-Management/porous-media-flow-model.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="7663b173df67fd6098a9e76ea7a354fcf151c549"
    )
