from fastapi import HTTPException
from starlette import status
from typing import Optional


def of_result_msg(
    ab_success: bool, as_msg: Optional[str] = None, alt_result: Optional[list] = None
):
    ld_dictR = {}
    ld_dictR["Success"] = ab_success

    if as_msg is not None:
        ld_dictR["Message"] = as_msg

    if alt_result is not None:
        ld_dictR["result"] = alt_result

    return ld_dictR


def of_return_http(as_msg: str, ai_status_code: int):
    if not as_msg:
        as_msg = "Error Occurred!!"

    status_dict = {
        400: status.HTTP_400_BAD_REQUEST,
        404: status.HTTP_404_NOT_FOUND,
        204: status.HTTP_204_NO_CONTENT,
    }

    if ai_status_code not in status_dict:
        ai_status_code = 400

    raise HTTPException(
        status_code=status_dict[ai_status_code],
        detail=as_msg,
    )


def of_update_model(model, schema, ab_commit: bool = False, db=None):

    for key, value in schema.dict().items():
        setattr(model, key, value)

    if ab_commit and db:
        db.commit()
        db.refresh(model)
