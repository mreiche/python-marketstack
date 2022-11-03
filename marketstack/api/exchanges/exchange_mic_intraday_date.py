from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.http_validation_error import HTTPValidationError
from ...models.response_exchange_intraday import ResponseExchangeIntraday
from ...types import UNSET, Response


def _get_kwargs(
    mic: str,
    date: str,
    *,
    client: Client,
    access_key: str,
) -> Dict[str, Any]:
    url = "{}/exchanges/{mic}/intraday/{date}".format(
        client.base_url, mic=mic, date=date
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["access_key"] = access_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[HTTPValidationError, ResponseExchangeIntraday]]:
    if response.status_code == 200:
        response_200 = ResponseExchangeIntraday.from_dict(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[HTTPValidationError, ResponseExchangeIntraday]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    mic: str,
    date: str,
    *,
    client: Client,
    access_key: str,
) -> Response[Union[HTTPValidationError, ResponseExchangeIntraday]]:
    """Mic Intraday Date

    Args:
        mic (str):
        date (str): Date in the formats %Y-%m-%d, %Y-%m-%d %H:%M:%S or ISO-8601
            %Y-%m-%dT%H:%M:%S+%Z
        access_key (str):

    Returns:
        Response[Union[HTTPValidationError, ResponseExchangeIntraday]]
    """

    kwargs = _get_kwargs(
        mic=mic,
        date=date,
        client=client,
        access_key=access_key,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    mic: str,
    date: str,
    *,
    client: Client,
    access_key: str,
) -> Optional[Union[HTTPValidationError, ResponseExchangeIntraday]]:
    """Mic Intraday Date

    Args:
        mic (str):
        date (str): Date in the formats %Y-%m-%d, %Y-%m-%d %H:%M:%S or ISO-8601
            %Y-%m-%dT%H:%M:%S+%Z
        access_key (str):

    Returns:
        Response[Union[HTTPValidationError, ResponseExchangeIntraday]]
    """

    return sync_detailed(
        mic=mic,
        date=date,
        client=client,
        access_key=access_key,
    ).parsed


async def asyncio_detailed(
    mic: str,
    date: str,
    *,
    client: Client,
    access_key: str,
) -> Response[Union[HTTPValidationError, ResponseExchangeIntraday]]:
    """Mic Intraday Date

    Args:
        mic (str):
        date (str): Date in the formats %Y-%m-%d, %Y-%m-%d %H:%M:%S or ISO-8601
            %Y-%m-%dT%H:%M:%S+%Z
        access_key (str):

    Returns:
        Response[Union[HTTPValidationError, ResponseExchangeIntraday]]
    """

    kwargs = _get_kwargs(
        mic=mic,
        date=date,
        client=client,
        access_key=access_key,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    mic: str,
    date: str,
    *,
    client: Client,
    access_key: str,
) -> Optional[Union[HTTPValidationError, ResponseExchangeIntraday]]:
    """Mic Intraday Date

    Args:
        mic (str):
        date (str): Date in the formats %Y-%m-%d, %Y-%m-%d %H:%M:%S or ISO-8601
            %Y-%m-%dT%H:%M:%S+%Z
        access_key (str):

    Returns:
        Response[Union[HTTPValidationError, ResponseExchangeIntraday]]
    """

    return (
        await asyncio_detailed(
            mic=mic,
            date=date,
            client=client,
            access_key=access_key,
        )
    ).parsed
