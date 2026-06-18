from typing import Any, Optional


def success(data: Any = None, message: str = "Success") -> dict:
    return {
        "success": True,
        "message": message,
        "data": data,
    }


def failed(message: str, data: Optional[Any] = None) -> dict:
    return {
        "success": False,
        "message": message,
        "data": data,
    }
