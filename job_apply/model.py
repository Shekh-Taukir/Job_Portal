from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship

# from db.db_init import Base
# from base_code.base_model import BaseMixin

from ..db.db_init import Base
from ..base_code.base_model import BaseMixin


class Status(Base):
    __tablename__ = "job_status"

    id = Column(Integer, primary_key=True, nullable=False)
    status_name = Column(String, nullable=False)

    def __str__(self):
        return self.status_name


class Job_Apply(Base, BaseMixin):

    __tablename__ = "job_apply_mst"

    applied_date = Column(DateTime, default=func.now())

    status_id = Column(
        Integer, ForeignKey("job_status.id", ondelete="CASCADE"), default=1
    )
    user_id = Column(Integer, ForeignKey("users_mst.id", ondelete="CASCADE"))
    job_id = Column(Integer, ForeignKey("jobs_mst.id", ondelete="CASCADE"))

    # status = relationship("Status")
    # user = relationship("User")
    # job = relationship("Jobs")

    # @property
    # def status_desc(self):
    #     return (
    #         f"{self.status.status_name}"
    #         if self.status is not None
    #         else "Error in status"
    #     )

    # @property
    # def user_name(self):
    #     return f"{self.user.first_name}, {self.user.last_name}"

    # @property
    # def jobs_title(self):
    #     return self.job.title
