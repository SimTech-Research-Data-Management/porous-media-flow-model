import sdRDM

from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class PorousMediaParameters(sdRDM.DataModel):
    """This is a container for information about parameters of the used porous media model
    """

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("porousmediaparametersINDEX"),
        xml="@id",
    )

    topology: str = Field(
        ...,
        description=(
            "Definition of the porous media model topology (rods, cylinders, minimal"
            " surface, ...)"
        ),
    )

    height: float = Field(
        ..., description="Value of the porous media model height in m"
    )

    width: float = Field(..., description="Value of the porous media model width in m")

    depth: float = Field(..., description="Value of the porous media model depth in m")

    porosity: float = Field(..., description="Value of the porous media model porosity")

    periodicity_x: Optional[float] = Field(
        description="Value of the porous media model periodicity in x-direction in m",
        default=None,
    )

    periodicity_y: Optional[float] = Field(
        description="Value of the porous media model periodicity in y-direction in m",
        default=None,
    )

    wall_thickness: Optional[float] = Field(
        description="Value of the porous media model wall thickness in m", default=None
    )

    __repo__: Optional[str] = PrivateAttr(default="None")

    __commit__: Optional[str] = PrivateAttr(
        default="4720cfe81270a9ec51f1bb082be79185b982c2b2"
    )
