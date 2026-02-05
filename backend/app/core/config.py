from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    @staticmethod
    def _get_env(key: str) -> str:
        value = os.getenv(key)
        if value is None:
            raise ValueError(f"Environment variable '{key}' is not set.")
        return value

    def __init__(self):
        self.DATABASE_URL: str = self._get_env("DATABASE_URL")
        self.JWT_SECRET_KEY: str = self._get_env("JWT_SECRET_KEY")
        self.JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
        self.ACCESS_TOKEN_EXPIRE_MINUTES: int = int(
            os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60)
        )

settings = Settings()
