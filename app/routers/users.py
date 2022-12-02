from fastapi import (
    FastAPI,
    Depends,
    status,
    Request,
    Response,
    HTTPException,
    APIRouter,
)
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..database import engine, get_db

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/")
def create_users(
    user: schemas.Usercreate,
    db: Session = Depends(get_db),
):
    # new_user = models.User(
    #     email=user.email,
    #     password=user.password,
    # )
    # print(**user.dict())
    # hase the password
    hased_password = utils.hased(user.password)
    user.password = hased_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{id}")
def get_user(id: int, db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id: {id} does not exits",
        )

    return user
