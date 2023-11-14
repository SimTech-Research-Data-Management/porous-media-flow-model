import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr, Field, validator
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic.types import PositiveInt
from numpy.typing import NDArray
from h5py._hl.dataset import Dataset as H5Dataset
from typing import Union

from .camera import Camera


@forge_signature
class Recording(sdRDM.DataModel):
    """The Recording contains crucial information about the parameters used during the recording process.
    These parameters offer valuable insights into the experimental setup, facilitating accurate analysis and interpretation of the recorded data.
    The inclusion of the video frames allows for a visual reference and further examination of the recorded footage.
    """

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("recordingINDEX"),
        xml="@id",
    )

    camera_id: Union[Camera, str] = Field(
        ...,
        reference="Camera.id",
        description="ID of the camera that has been used",
    )

    time: float = Field(
        ...,
        description="Value of the investigated time period in s",
    )

    repetition_rate: float = Field(
        ...,
        description="Value of the recording repetition rate in Hz",
    )

    field_of_view: str = Field(
        ...,
        description="Value of the field of view in m x m",
    )

    height: Optional[PositiveInt] = Field(
        default=None,
        description="Height of the image",
    )

    width: Optional[PositiveInt] = Field(
        default=None,
        description="Width of the image",
    )

    n_frames: Optional[int] = Field(
        default=None,
        description="Number of frames found in this video",
    )

    frames: Optional[Union[NDArray, H5Dataset]] = Field(
        default=None,
        description="Videoframes",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/SimTech-Research-Data-Management/porous-media-flow-model.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="6ceb1857568aa5664c3d40d0d0d5ed03742f2f00"
    )

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
