import os
from telethon import TelegramClient
from fastapi import HTTPException
from telethon.errors import (
    SessionPasswordNeededError,
    PhoneNumberInvalidError,
    PhoneCodeEmptyError,
    PhoneCodeExpiredError,
    PhoneCodeInvalidError,
    PhoneNumberUnoccupiedError
)

from ..core.config import api_id, api_hash


async def send_code_request(req):
    client = TelegramClient(req.phone, api_id, api_hash)
    try:
        await client.connect()
    except OSError:
        raise HTTPException(status_code=400, detail="Failed to connect")

    try:
        phone = await client.send_code_request(
            phone=req.phone,
            force_sms=req.force_sms
        )
        return phone.phone_code_hash
    except PhoneNumberInvalidError:
        os.remove(f"{req.phone}.session")
        raise HTTPException(
            status_code=400,
            detail="The phone number is invalid")

    except Exception:
        os.remove(f"{req.phone}.session")
        raise HTTPException(
            status_code=400,
            detail="something went wrong")


async def sign_in(req):
    client = TelegramClient(req.phone, api_id, api_hash)

    try:
        await client.connect()
    except OSError:
        raise HTTPException(status_code=400, detail="Failed to connect")

    try:
        await client.sign_in(
            phone=req.phone,
            code=req.code,
            phone_code_hash=req.phone_code_hash
        )
        me = await client.get_me()
        await client.disconnect()
        os.remove(f"{req.phone}.session")
        return me.id, me.first_name, me.last_name
    except SessionPasswordNeededError:
        raise HTTPException(
            status_code=400,
            detail="please disable 2 factor login this app not suppot yet !!")

    except PhoneCodeEmptyError:
        raise HTTPException(
            status_code=400,
            detail="The phone code is missing")

    except PhoneCodeExpiredError:
        raise HTTPException(
            status_code=400,
            detail="The confirmation code has expired")

    except PhoneCodeInvalidError:
        raise HTTPException(
            status_code=400,
            detail="The phone code entered was invalid")

    except PhoneNumberInvalidError:
        raise HTTPException(
            status_code=400,
            detail="The phone number is invalid")

    except PhoneNumberUnoccupiedError:
        raise HTTPException(
            status_code=400,
            detail="The phone number is not yet being used")

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="someting went wrong")
