from fastapi import Depends
from typing import Annotated
from .service import of_get_current_user

auth_dependency = Annotated[dict, Depends(of_get_current_user)]
