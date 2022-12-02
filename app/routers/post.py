from email.policy import HTTP
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
from .. import models, schemas, oauth2
from ..database import engine, get_db
from typing import Optional, List
from sqlalchemy import func


router = APIRouter(prefix="/posts", tags=["posts"])


# @post.get("/posts", response_model=List[schemas.Post])
# async def root(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).filter(models.Post.id == id).all()
#     posts = cursor.fetchall()
#     return {"data": posts}


@router.get("/")
def get_all_posts(
    db: Session = Depends(get_db),
    user_id: int = Depends(oauth2.get_current_user),
    Limit: int = 10,
    skip: int = 0,
    search: Optional[str] = " ",
):
    postss = (
        db.query(models.Post)
        .filter(models.Post.title.contains(search))
        .limit(Limit)
        .offset(skip)
        .all()
    )
    data = (
        db.query(models.Post, func.count(models.Vote.post_id).label("votes"))
        .join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True)
        .group_by(models.Post.id)
        .filter(models.Post.title.contains(search))
        .limit(Limit)
        .offset(skip)
        .all()
    )
    print(data)
    # postss = db.query(models.Post).filter(models.Post.owner_id == user_id.id).all()
    return data


@router.post("/")
def create_posts(
    post: schemas.Postcreate,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    # cursor.execute(
    #     """insert into posts (title,content,published) values (%s,%s,%s) returning *""",
    #     (post.title, post.content, post.published),
    # )
    # new_post = cursor.fetchone()
    # conn.commit()
    # print(user_id)
    print(current_user.id)
    # print(postsed.owner_id)
    print(post.title)
    print(post.content)
    new_post = models.Post(
        title=post.title,
        content=post.content,
        published=post.published,
        # owner_id=current_user.id,
    )

    new_post = models.Post(owner_id=current_user.id, **post.dict())
    # new_post.add(owner_id=current_user.id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/{id}")
def get_post(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    # posts = db.query(models.Post).filter(models.Post.id == id).first()
    posts = (
        db.query(models.Post, func.count(models.Vote.post_id).label("votes"))
        .join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True)
        .group_by(models.Post.id)
        .filter(models.Post.id == id)
        .first()
    )
    # cursor.execute("""select * from posts where id=%s""", (str(id)))
    # posts = cursor.fetchone()
    # # post = find_post(id)

    # postss = posts.first()
    print(posts)

    if not posts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id:{id} was not found",
        )
    data_int = int(current_user.id)
    print(posts["Post"].owner_id)
    if posts["Post"].owner_id != data_int:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="not authorized user"
        )

    # if posts.owner_id != current_user.id:
    #     raise HTTPException(
    #         status_code=status.HTTP_403_FORBIDDEN, detail=f"not authorized user"
    #     )

    return posts


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    posts = db.query(models.Post).filter(models.Post.id == id)

    # cursor.execute("""delete from posts where id=%s returning *""", ((str(id))))
    # deleted_post = cursor.fetchone()
    # # index = find_index_post(id)
    # conn.commit()
    postss = posts.first()
    data_int = int(current_user.id)

    if posts.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post bwith id {id} doesn't exit",
        )
    if postss.owner_id != data_int:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="not authorized user"
        )

    posts.delete(synchronize_session=False)
    db.commit()
    # my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}")
def update_post(
    id: int,
    data_post: schemas.Postcreate,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):

    # cursor.execute(
    #     """update posts set title=%s,content=%s,published=%s where id=%s returning *""",
    #     (post.title, post.content, post.published, str(id)),
    # )
    # # ndex = find_index_post(id)
    # posts = cursor.fetchone()
    # conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    print(post_query.first())
    postsed = post_query.first()
    print(current_user.id)
    print(postsed.owner_id)
    print("dolewjdohjsoijfd")
    print(current_user)

    data_int = int(current_user.id)

    if postsed == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post bwith id {id} doesn't exit",
        )

        # to validate same user doing crud operation
    if postsed.owner_id != data_int:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="not authorized user"
        )

    print("post_dict", data_post.dict())
    post_query.update(data_post.dict(), synchronize_session=False)
    db.commit()

    return {"data": post_query.first()}
