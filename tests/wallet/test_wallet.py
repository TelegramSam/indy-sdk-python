from unittest import TestCase, mock
import pytest

from indypython import wallet

class AsyncMock(mock.MagicMock):
    async def __call__(self, *args, **kwargs):
        return super(AsyncMock, self).__call__(*args, **kwargs)

@pytest.mark.asyncio
async def test_create_wallet():
    with mock.patch('indy.wallet.create_wallet', new_callable=AsyncMock) as m:
        await wallet.create_wallet({'a': 1}, {'b': 2})
        m.assert_called_once_with('{"a": 1}', '{"b": 2}')
