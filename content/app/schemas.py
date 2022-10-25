"""
Author: Ammar Saqib
"""
# pylint: disable=no-self-argument
# pylint: disable=no-name-in-module
# pylint: disable=missing-class-docstring
from datetime import datetime

from typing import Optional, List, Dict, Tuple
from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, validator, root_validator, HttpUrl
from fastapi import UploadFile


class TenantClientUpdate(BaseModel):
    name: Optional[str]
    logo: Optional[UploadFile]
    tenant_id: int


class TenantClientUpdateDB(BaseModel):
    name: Optional[str]
    logo: Optional[HttpUrl]
    tenant_id: int


class TenantClient(TenantClientUpdate):
    name: str


# Sample Schemas


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
