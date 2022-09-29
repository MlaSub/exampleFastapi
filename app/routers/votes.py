from typing import List
from .. import models, schemas, utils, oauth2
from fastapi import Body, FastAPI, Response, status, HTTPException, Depends, APIRouter
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/vote", tags=["vote"])


@router.post("/{id}", status_code=status.HTTP_201_CREATED)
def voting(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    vote_query = db.query(models.Votes).filter(models.Votes.post_id ==
                                               id, models.Votes.user_id == current_user.id)
    vote = vote_query.first()
    print(vote)
    if vote == None:
        new_vote = models.Votes(post_id=id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
    else:
        vote_query.delete(synchronize_session=False)
        db.commit()
    return Response(status_code=status.HTTP_200_OK)
