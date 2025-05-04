from sqlalchemy import Column, String

# from db.db_init import Base
# from base_code.base_model import BaseMixin

from ..db.db_init import Base
from ..base_code.base_model import BaseMixin


class User(Base, BaseMixin):
    __tablename__ = "users_mst"

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"
