import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .porousmediaparameters import PorousMediaParameters


@forge_signature
class Model(sdRDM.DataModel):
    """The Model section contains information about the location of the object in the flow channel.
    It provides details regarding the type of the present porous media model, its location relative to the free flow and if applicable, detailed parameters related to the porous media model which is used.
    """

    id: Optional[str] = Field(
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
        default="0a1753bd2d9d680e8290be0d84d604b5bccf852b"
    )
