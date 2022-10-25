"""
Author: Ammar Saqib
"""
from typing import Optional
import json
from fastapi import (
    APIRouter,
    Response,
    Depends,
    Header,
    HTTPException,
    Form,
    UploadFile,
    File,
)
from sqlalchemy.orm import Session

from app.schemas import TenantClientUpdate, TenantClient
from app.database import get_db
from controllers.content_controller import ContentController

NO_CLIENT_ERROR = "This tenant is not allowed to have clients. Change your company status in user settings".replace(
    "\t", ""
)

router = APIRouter(prefix="/v1/tenant_clients", tags=["Tenant Clients"])


@router.post("/", status_code=201)
def post_tenant_clients(
    _response: Response,
    name: str = Form(...),
    logo: Optional[UploadFile] = File(None),
    tenant_id: int = Header(...),
    has_clients: int = Header(...),
    user_id: int = Header(...),
    _db: Session = Depends(get_db),
):
    """
    Adds a tenant client
    """

    if not has_clients:
        raise HTTPException(status_code=400, detail=NO_CLIENT_ERROR)

    # logo_url = CloudStorageManager().upload_logo(logo)

    status_code, _id, logo_url = ContentController().insert_tenant_client(
        _db, user_id, TenantClient(tenant_id=tenant_id, logo=logo, name=name)
    )
    _response.status_code = status_code

    return {"_id": _id, "logo": logo_url, "name": name}


@router.get("/")
def get_tenant_clients(
    _response: Response,
    tenant_id: int = Header(...),
    has_clients: int = Header(...),
    allowed_scopes: Optional[str] = Header(None),
    _db: Session = Depends(get_db),
):
    """
    Gets a list of tenant clients
    """

    if not has_clients:
        raise HTTPException(status_code=400, detail=NO_CLIENT_ERROR)

    if allowed_scopes:
        allowed_scopes = json.loads(allowed_scopes)

    status_code, _data = ContentController().get_tenant_clients(
        _db, tenant_id, allowed_scopes
    )
    _response.status_code = status_code

    return _data


@router.get("/{_id}")
def get_tenant_client(
    _id: int,
    _response: Response,
    tenant_id: int = Header(...),
    has_clients: int = Header(...),
    allowed_scopes: Optional[str] = Header(None),
    _db: Session = Depends(get_db),
):
    """
    Gets a certain tenant client specified by ID
    """

    if not has_clients:
        raise HTTPException(status_code=400, detail=NO_CLIENT_ERROR)

    if allowed_scopes:
        allowed_scopes = json.loads(allowed_scopes)

    status_code, _data = ContentController().get_tenant_client(
        _db, _id, tenant_id, allowed_scopes
    )
    _response.status_code = status_code

    return _data


@router.patch("/{_id}", status_code=200)
def patch_tenant_client(
    _id: int,
    _response: Response,
    name: str = Form(None),
    logo: UploadFile = File(None),
    tenant_id: int = Header(...),
    has_clients: int = Header(...),
    user_id: int = Header(...),
    _db: Session = Depends(get_db),
):
    """
    Patches a tenant client
    """

    if not has_clients:
        raise HTTPException(status_code=400, detail=NO_CLIENT_ERROR)

    if not name and not logo:
        raise HTTPException(status_code=422, detail="Update atleast one attribute.")

    status_code, _id, logo_url = ContentController().patch_tenant_client(
        _db, user_id, _id, TenantClientUpdate(tenant_id=tenant_id, logo=logo, name=name)
    )
    _response.status_code = status_code

    return {"_id": _id, "name": name, "logo": logo_url}


@router.delete("/{_id}")
def delete_tenant_client(
    _id: int,
    _response: Response,
    tenant_id: int = Header(...),
    has_clients: int = Header(...),
    user_id: int = Header(...),
    _db: Session = Depends(get_db),
):
    """
    Deletes a certain tenant client specified by ID
    """

    if not has_clients:
        raise HTTPException(status_code=400, detail=NO_CLIENT_ERROR)

    status_code, _status = ContentController().del_tenant_client(
        _db, _id, tenant_id, user_id, del_logo=True
    )
    _response.status_code = status_code

    if isinstance(_status, tuple):
        return {"delete_status": _status[0], "message": _status[1]}

    return {"delete_status": _status}
