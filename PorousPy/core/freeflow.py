import sdRDM

from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from .flowparameters import FlowParameters


@forge_signature
class FreeFlow(sdRDM.DataModel):
    """This is a container for information about the free flow channel and the working fluid.
    """

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("freeflowINDEX"),
        xml="@id",
    )

    shape: str = Field(..., description="Shape of the flow channels cross section")

    hydraulic_diameter: float = Field(
        ..., description="Value of the hydraulic diameter in m"
    )

    height: Optional[float] = Field(
        description="Value of the flow channel height in m", default=None
    )

    width: Optional[float] = Field(
        description="Value of the flow channel width in m", default=None
    )

    depth: Optional[float] = Field(
        description="Value of the flow channel depth in m", default=None
    )

    diameter: Optional[float] = Field(
        description="Value of the flow channel diameter in m", default=None
    )

    fluid: FlowParameters = Field(
        description="Description of flow parameters", default=None
    )

    __repo__: Optional[str] = PrivateAttr(default="None")

    __commit__: Optional[str] = PrivateAttr(
        default="4720cfe81270a9ec51f1bb082be79185b982c2b2"
    )
