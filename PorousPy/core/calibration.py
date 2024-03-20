import sdRDM

from typing import Dict, Optional
from uuid import uuid4
from pydantic import PrivateAttr, model_validator
from pydantic_xml import attr, element
from lxml.etree import _Element

from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict


@forge_signature
class Calibration(
    sdRDM.DataModel,
    search_mode="unordered",
):
    """*The Calibration contains information about the parameters used during the recording process.
    The parameters are providing insights into the camera position relative to the experiment for correcting possible misalignments.*
    """

    id: Optional[str] = attr(
        name="id",
        description="Unique identifier of the given object.",
        default_factory=lambda: str(uuid4()),
        xml="@id",
    )

    calibration_type: str = element(
        description=(
            "Specify the calibration plate and/or the calibration facility which was"
            " used for calibration."
        ),
        tag="calibration_type",
        json_schema_extra=dict(),
    )

    camera_position_translation: Optional[float] = element(
        description=(
            "Value of the translation of the camera position relative to the"
            " calibration plate. \[m]"
        ),
        default=None,
        tag="camera_position_translation",
        json_schema_extra=dict(),
    )

    camera_position_rotation: Optional[float] = element(
        description=(
            "Value of the rotation of the camera position relative to the calibration"
            " plate. \[°]"
        ),
        default=None,
        tag="camera_position_rotation",
        json_schema_extra=dict(),
    )

    scale_factor: float = element(
        description=(
            "Value of the scale factor of the recordings.The amount of pixels"
            " corresponding to the length of 1 mm. \[px/mm]"
        ),
        tag="scale_factor",
        json_schema_extra=dict(),
    )

    calibration_image: Optional[bytes] = element(
        description="The actual calibration image which was used.",
        default=None,
        tag="calibration_image",
        json_schema_extra=dict(),
    )

    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/SimTech-Research-Data-Management/porous-media-flow-model"
    )
    _commit: Optional[str] = PrivateAttr(
        default="2535a1c6d00880d1546dce3ed835fcc5e3bfb375"
    )
    _raw_xml_data: Dict = PrivateAttr(default_factory=dict)

    @model_validator(mode="after")
    def _parse_raw_xml_data(self):
        for attr, value in self:
            if isinstance(value, (ListPlus, list)) and all(
                isinstance(i, _Element) for i in value
            ):
                self._raw_xml_data[attr] = [elem2dict(i) for i in value]
            elif isinstance(value, _Element):
                self._raw_xml_data[attr] = elem2dict(value)

        return self
