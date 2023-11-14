import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .flowparameters import FlowParameters


@forge_signature
class FreeFlow(sdRDM.DataModel):
    """The Free Flow section contains information about the shape, dimensions, and working fluid of the free flow channel.
    It provides details such as the shape of the flow channel's cross-section, the hydraulic diameter, height, width and depth of the channel and a description of the flow parameters of the working fluid.
    """

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("freeflowINDEX"),
        xml="@id",
    )

    shape: str = Field(
        ...,
        description="Shape of the flow channels cross section",
    )

    hydraulic_diameter: float = Field(
        ...,
        description="Value of the hydraulic diameter in m",
    )

    height: Optional[float] = Field(
        default=None,
        description="Value of the flow channel height in m",
    )

    width: Optional[float] = Field(
        default=None,
        description="Value of the flow channel width in m",
    )

    depth: Optional[float] = Field(
        default=None,
        description="Value of the flow channel depth in m",
    )

    diameter: Optional[float] = Field(
        default=None,
        description="Value of the flow channel diameter in m",
    )

    fluid: FlowParameters = Field(
        ...,
        description="Description of flow parameters",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/SimTech-Research-Data-Management/porous-media-flow-model.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="6ceb1857568aa5664c3d40d0d0d5ed03742f2f00"
    )
