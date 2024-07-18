from __future__ import annotations

from datetime import datetime  # noqa: TCH003
from uuid import UUID  # noqa: TCH003

import msgspec

from ...database.models.team_roles import TeamRoles
from ...library.schema import CamelizedBaseStruct

__all__ = (
    "AccountLogin",
    "AccountRegister",
    "UserRoleAdd",
    "UserRoleRevoke",
    "UserCreate",
    "User",
    "UserRole",
    "UserTeam",
    "UserUpdate",
)


class UserTeam(CamelizedBaseStruct):
    """Holds team details for a user.

    This is nested in the User Model for 'team'
    """

    team_id: UUID
    team_name: str
    is_owner: bool = False
    role: TeamRoles = TeamRoles.MEMBER


class UserRole(CamelizedBaseStruct):
    """Holds role details for a user.

    This is nested in the User Model for 'roles'
    """

    role_id: UUID
    role_slug: str
    role_name: str
    assigned_at: datetime


class User(CamelizedBaseStruct):
    """User properties to use for a response."""

    id: UUID
    email: str
    xmpp: str | None = None
    name: str | None = None
    is_superuser: bool = False
    is_active: bool = False
    is_verified: bool = False
    teams: list[UserTeam] = []
    roles: list[UserRole] = []


class UserCreate(CamelizedBaseStruct):
    email: str
    password: str
    xmpp: str | None = None
    name: str | None = None
    is_superuser: bool = False
    is_active: bool = True
    is_verified: bool = False


class UserUpdate(CamelizedBaseStruct, omit_defaults=True):
    email: str | None | msgspec.UnsetType = msgspec.UNSET
    password: str | None | msgspec.UnsetType = msgspec.UNSET
    name: str | None | msgspec.UnsetType = msgspec.UNSET
    is_superuser: bool | None | msgspec.UnsetType = msgspec.UNSET
    is_active: bool | None | msgspec.UnsetType = msgspec.UNSET
    is_verified: bool | None | msgspec.UnsetType = msgspec.UNSET


class AccountLogin(CamelizedBaseStruct):
    username: str
    password: str


class AccountRegister(CamelizedBaseStruct):
    email: str
    password: str
    name: str | None = None


class UserRoleAdd(CamelizedBaseStruct):
    """User role add ."""

    user_name: str


class UserRoleRevoke(CamelizedBaseStruct):
    """User role revoke ."""

    user_name: str