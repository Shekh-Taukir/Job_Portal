from sqlalchemy import Column, String, Date, Boolean

# from db.db_init import Base
# from base_code.base_model import BaseMixin

from ..db.db_init import Base
from ..base_code.base_model import BaseMixin


class Company(Base, BaseMixin):
    __tablename__ = "company_mst"

    name = Column(String, index=True)
    founder = Column(String)
    founded_date = Column(Date)
    isActive = Column(Boolean, default=True)

    def __str__(self):
        return self.name
