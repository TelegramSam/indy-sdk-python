from indy import wallet
from typing import Dict, Optional
import json


async def test_method(arg1, arg2):
    return None

async def create_wallet(config: Dict,
                        credentials: Dict) -> None:
    return await wallet.create_wallet(json.dumps(config), json.dumps(credentials))

async def open_wallet(config: str,
                      credentials: str) -> int:
    pass

async def close_wallet(handle: int) -> None:
    pass

async def delete_wallet(config: str,
                        credentials: str) -> None:
    pass

async def export_wallet(handle: int,
                        export_config_json: str) -> None:
    pass


async def import_wallet(config: str,
                        credentials: str,
                        import_config_json: str) -> None:
    pass

async def generate_wallet_key(config: Optional[str]) -> str:
    pass

