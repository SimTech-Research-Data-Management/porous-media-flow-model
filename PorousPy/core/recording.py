import sdRDM

from typing import Dict, Optional
from pydantic import PrivateAttr, model_validator, validator
from uuid import uuid4
from pydantic_xml import attr, element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict


@forge_signature
class Recording(sdRDM.DataModel, search_mode="unordered"):
    """*The Recording contains crucial information about the parameters used during the recording process.
    These parameters offer valuable insights into the experimental setup, facilitating accurate analysis and interpretation of the recorded data.
    The inclusion of the video frames allows for a visual reference and further examination of the recorded footage.*
    """

    id: Optional[str] = attr(
        name="id",
        description="Unique identifier of the given object.",
        default_factory=lambda: str(uuid4()),
        xml="@id",
    )

    time: float = element(
        description="Value of the investigated time period. \\[s]",
        tag="time",
        json_schema_extra=dict(),
    )

    repetition_rate: float = element(
        description="Value of the recording repetition rate. \\[Hz]",
        tag="repetition_rate",
        json_schema_extra=dict(),
    )

    field_of_view: str = element(
        description="Value of the field of view. \\[m x m]",
        tag="field_of_view",
        json_schema_extra=dict(),
    )

    n_frames: Optional[int] = element(
        description="Number of frames found in this video.",
        default=None,
        tag="n_frames",
        json_schema_extra=dict(),
    )

    frames: Optional[bytes] = element(
        description="The actual Videoframes of the raw video",
        default=None,
        tag="frames",
        json_schema_extra=dict(),
    )

    location: Optional[str] = element(
        description="Specify the local filepath to the location of the recordings.",
        default=None,
        tag="location",
        json_schema_extra=dict(),
    )
    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/SimTech-Research-Data-Management/porous-media-flow-model"
    )
    _commit: Optional[str] = PrivateAttr(
        default="07eea00104b98a757878bf718d0cd3baf4ea52d5"
    )
    _raw_xml_data: Dict = PrivateAttr(default_factory=dict)

    @model_validator(mode="after")
    def _parse_raw_xml_data(self):
        for attr, value in self:
            if isinstance(value, (ListPlus, list)) and all(
                (isinstance(i, _Element) for i in value)
            ):
                self._raw_xml_data[attr] = [elem2dict(i) for i in value]
            elif isinstance(value, _Element):
                self._raw_xml_data[attr] = elem2dict(value)
        return self

    @validator("camera_id")
    def get_camera_id_reference(cls, value):
        """Extracts the ID from a given object to create a reference"""

        from .camera import Camera

        if isinstance(value, Camera):
            return value.id
        elif isinstance(value, str):
            return value
        else:
            raise TypeError(
                f"Expected types [Camera, str] got '{type(value).__name__}' instead."
            )
