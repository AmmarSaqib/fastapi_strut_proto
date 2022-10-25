"""
Author: Muhammad Omer Khalil
"""
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    CheckConstraint,
    Text,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Float

from app.database import Base


class TenantClients(Base):
    """
    Table for storing Tenant Clients
    """

    __tablename__ = "tenant_clients"

    id = Column(Integer, primary_key=True)

    name = Column(String(255), nullable=False)

    tenant_id = Column(Integer, nullable=False)

    logo = Column(String(255), nullable=True)

    roles = relationship("Roles")
