from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import Optional

from .device import Device


@forge_signature
class Laser(Device):

    """This is a container for information regarding lasers which were used within the dataset.
    """

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("laserINDEX"),
        xml="@id",
    )
    wavelength: float = Field(
        ...,
        description="Value of the used wavelength",
    )

    type: Optional[str] = Field(
        description="Pulsed or continous wave laser?",
        default=None,
    )

    power: Optional[float] = Field(
        description="value of the laser power",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/SimTech-Research-Data-Management/porous-media-flow-model.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="53d30eba563d0bc6bcf3db15575fa61d02387eb0"
    )
