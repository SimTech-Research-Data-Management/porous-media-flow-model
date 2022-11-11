import sdRDM

from typing import Optional, Union
from typing import Optional
from typing import Union
from pydantic import PrivateAttr
from pydantic import Field
from pydantic import validator
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from h5py._hl.dataset import Dataset as H5Dataset
from numpy.typing import NDArray
from pydantic.types import PositiveInt

@forge_signature
class Recording(sdRDM.DataModel):
    """This is a container for information about the recording parameters"""


    id: str = Field(description='Unique identifier of the given object.', default_factory=IDGenerator('recordingINDEX'), xml='@id')


    time: float = Field(..., description='Value of the investigated time period in s')


    repetition_rate: float = Field(..., description='Value of the recording repetition rate in Hz')


    field_of_view: str = Field(..., description='Value of the field of view in m x m')


    camera_id: Union[str, 'Camera'] = Field(..., description='ID of the camera that has been used')


    height: Optional[PositiveInt] = Field(description='Height of the image', default=None)


    width: Optional[PositiveInt] = Field(description='Width of the image', default=None)


    n_frames: Optional[int] = Field(description='Number of frames found in this video', default=None)


    frames: Union[NDArray, H5Dataset, None] = Field(description='Videoframes', default=None)


    __repo__: Optional[str] = PrivateAttr(default='None')


    __commit__: Optional[str] = PrivateAttr(default='4720cfe81270a9ec51f1bb082be79185b982c2b2')

    @validator('camera_id', pre=True)
    def get_camera_id_reference(cls, value):
        """Extracts the ID from a given object to create a reference"""
        
from .camera import Camera
        if not isinstance(value, (Camera, str)):
            raise TypeError(f"Expected 'Camera' or 'str' got '{type(value).__name__}' instead.")
        elif isinstance(value, Camera):
            return value.id
        elif isinstance(value, str):
            return value