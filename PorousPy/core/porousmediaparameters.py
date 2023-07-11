import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class PorousMediaParameters(sdRDM.DataModel):
    """This is a container for information about parameters of the used porous media model"""

    id: Optional[str] = Field(
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
        ...,
        description="Value of the porous media model height in m",
    )

    width: float = Field(
        ...,
        description="Value of the porous media model width in m",
    )

    depth: float = Field(
        ...,
        description="Value of the porous media model depth in m",
    )

    porosity: float = Field(
        ...,
        description="Value of the porous media model porosity",
    )

    periodicity_x: Optional[float] = Field(
        default=None,
        description="Value of the porous media model periodicity in x-direction in m",
    )

    periodicity_y: Optional[float] = Field(
        default=None,
        description="Value of the porous media model periodicity in y-direction in m",
    )

    wall_thickness: Optional[float] = Field(
        default=None,
        description="Value of the porous media model wall thickness in m",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/SimTech-Research-Data-Management/porous-media-flow-model.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="9861f1edfafad8d066d12be2808992116bbd3b62"
    )
