from __future__ import annotations

from datetime import datetime, date

from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase

from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .team import Team
    from .user import User
    from .task import Task
    from .scope import Scope
    from .project_component import ProjectComponent
class Project(UUIDAuditBase):
    __tablename__ = "project"
    __table_args__ = {"comment": "Projects for the application"}
    
    project_name: Mapped[str] = mapped_column(String(255), nullable=False, comment="Project name")
    project_description: Mapped[str] = mapped_column(String(255), nullable=False, comment="Project description")
    project_status: Mapped[str] = mapped_column(String(255), nullable=False, comment="Project status")
    project_start_date: Mapped[date] = mapped_column(Date, nullable=False, comment="Project start date")
    project_end_date: Mapped[date] = mapped_column(Date, nullable=False, comment="Project end date")
    
    project_creator: Mapped[User] = relationship("User", back_populates="project", uselist=False, lazy="joined")
    team_assigned: Mapped[Team] = relationship("Team", back_populates="project", uselist=False, lazy="joined")
    project_scope: Mapped[Scope] = relationship("Scope", back_populates="project", uselist=False, lazy="joined")
    tasks: Mapped[list[Task]] = relationship("Task", back_populates="project", uselist=True, lazy="joined")
    project_components: Mapped[list[ProjectComponent]] = relationship("ProjectComponent", back_populates="project", uselist=True, lazy="joined")
    
    