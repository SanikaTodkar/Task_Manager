from passlib.context import CryptContext
from jose import JWTError, jwt
from app.core.config import settings
from datetime import datetime, timedelta

from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import User

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def _to_bcrypt_safe(password: str) -> bytes:
    password_bytes = password.encode("utf-8")
    return password_bytes[:72]

def hash_password(password: str) -> str:
    return pwd_context.hash(_to_bcrypt_safe(password))

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(
        _to_bcrypt_safe(plain_password),
        hashed_password
    )

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(
                                    minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
                                    )
    to_encode.update({"exp": expire})

    return jwt.encode(
                to_encode,
                settings.JWT_SECRET_KEY,
                algorithm=settings.JWT_ALGORITHM
            )

def decode_access_token(token: str) -> dict | None:
    try:
        return jwt.decode(
                    token,
                    settings.JWT_SECRET_KEY,
                    algorithms=[settings.JWT_ALGORITHM]
                )
    except JWTError:
        return None
    

#Auth dependency
security = HTTPBearer()

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    token = credentials.credentials
    payload = decode_access_token(token)

    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    user_id = payload.get("sub")
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user