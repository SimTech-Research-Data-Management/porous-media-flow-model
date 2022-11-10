import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from h5py._hl.dataset import Dataset as H5Dataset
from numpy.typing import NDArray
from pydantic import Field
from pydantic import validator
from pydantic.types import PositiveInt
from typing import Optional
from typing import Union


@forge_signature
class Video(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("videoINDEX"),
        xml="@id",
    )
    camera_id: Union[str, "Camera"] = Field(
        ...,
        description="ID of the camera that has been used",
    )

    height: Optional[PositiveInt] = Field(
        description="Height of the image",
        default=None,
    )

    width: Optional[PositiveInt] = Field(
        description="Width of the image",
        default=None,
    )

    total_frames: Optional[int] = Field(
        description="Number of frames found in this video",
        default=None,
    )

    frames: Union[NDArray, H5Dataset, None] = Field(
        description="Videoframes",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(default="None")

    @validator("camera_id", pre=True)
    def get_camera_id_reference(cls, value):
        """Extracts the ID from a given object to create a reference"""

        from .camera import Camera

        if not isinstance(value, (Camera, str)):
            raise TypeError(
                f"Expected 'Camera' or 'str' got '{type(value).__name__}' instead."
            )
        elif isinstance(value, Camera):
            return value.id
        elif isinstance(value, str):
            return value
