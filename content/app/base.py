"""
Author: Muhammad Omer Khalil
"""
# Import all the models, so that Base has them before being
# imported by Alembic

# pylint: disable=W0611
# pylint: disable=E0611

from app.database import Base
from app.models import PersonalityTypes, TestPacks, QualificationMappings,\
                    RoleTemplates, TenantClients, ReferenceRequirements
