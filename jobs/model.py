from sqlalchemy import Column, String, Date, Text, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship

# from db.db_init import Base
# from base_code.base_model import BaseMixin

from ..db.db_init import Base
from ..base_code.base_model import BaseMixin


class Jobs(Base, BaseMixin):
    __tablename__ = "jobs_mst"

    title = Column(String, index=True)
    description = Column(Text)
    posted_date = Column(Date)
    isActive = Column(Boolean, default=True)
    company = Column(Integer, ForeignKey("company_mst.id", ondelete="CASCADE"))

    company_details = relationship("Company", backref="job_list")

    def __str__(self):
        return self.title

    @property
    def company_name(self):
        return self.company_details.name
