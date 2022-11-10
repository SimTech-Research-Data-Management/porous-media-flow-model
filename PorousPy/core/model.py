import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import Optional

from .porousmediaparameters import PorousMediaParameters


@forge_signature
class Model(sdRDM.DataModel):

    """This is a container for information about a possible object in/adjascent to the free flow
    """

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
        description="Description of porous media parameters",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/SimTech-Research-Data-Management/porous-media-flow-model.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="53d30eba563d0bc6bcf3db15575fa61d02387eb0"
    )