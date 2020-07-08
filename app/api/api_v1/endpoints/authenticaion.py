from fastapi import APIRouter
from ....models.auth import (
    SignIn,
    SignInResponse,
    Confirm,
    ConfirmResponse
)
from ....Telegram.auth import send_code_request, sign_in

router = APIRouter()


@router.post(
    '/login/telegram_auth',
    tags=['login'],
    status_code=200
)
async def login(
    req: SignIn
):
    _hash = await send_code_request(req)

    return SignInResponse(
        phone=req.phone,
        phone_code_hash=_hash
    )


@router.post(
    '/login/telegram_confirm',
    tags=['login'],
    status_code=200
)
async def confirm(
    req: Confirm
):
    _id, fname, lname = await sign_in(req)
    return ConfirmResponse(
        id=_id,
        phone=req.phone,
        first_name=fname,
        last_name=lname
    )
