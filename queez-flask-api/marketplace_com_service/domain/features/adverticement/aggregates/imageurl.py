
from ..valueobjects.id import Id
from ..valueobjects.image_url import ImageURL
from ..valueobjects.id import Id
from ..valueobjects.id import Id
from ..valueobjects.state import State
from ..valueobjects.transection_type import TransectionType


class ImageDetails:
    def __init__(self, image_details_id: Id, image_url: ImageURL, transec_ref_id: Id):
        self.image_details_id = image_details_id
        self.transec_ref_id = transec_ref_id
        self.image_url = image_url
        
      
        
        
        



