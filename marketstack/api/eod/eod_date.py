from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.http_validation_error import HTTPValidationError
from ...models.response_listmodels_eod_price import ResponseListmodelsEodPrice
from ...models.sort import Sort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    date: str,
    *,
    client: Client,
    access_key: str,
    symbols: Union[Unset, None, str] = UNSET,
    exchange: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, Sort] = UNSET,
    date_from: Union[Unset, None, str] = UNSET,
    date_to: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/eod/{date}".format(client.base_url, date=date)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["access_key"] = access_key

    params["symbols"] = symbols

    params["exchange"] = exchange

    json_sort: Union[Unset, None, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value if sort else None

    params["sort"] = json_sort

    params["date_from"] = date_from

    params["date_to"] = date_to

    params["limit"] = limit

    params["offset"] = offset

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
) -> Optional[Union[HTTPValidationError, ResponseListmodelsEodPrice]]:
    if response.status_code == 200:
        response_200 = ResponseListmodelsEodPrice.from_dict(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[HTTPValidationError, ResponseListmodelsEodPrice]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    date: str,
    *,
    client: Client,
    access_key: str,
    symbols: Union[Unset, None, str] = UNSET,
    exchange: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, Sort] = UNSET,
    date_from: Union[Unset, None, str] = UNSET,
    date_to: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseListmodelsEodPrice]]:
    """Date

    Args:
        date (str): Date in the formats %Y-%m-%d, %Y-%m-%d %H:%M:%S or ISO-8601
            %Y-%m-%dT%H:%M:%S+%Z
        access_key (str):
        symbols (Union[Unset, None, str]):
        exchange (Union[Unset, None, str]):
        sort (Union[Unset, None, Sort]): An enumeration.
        date_from (Union[Unset, None, str]): Date in the formats %Y-%m-%d, %Y-%m-%d %H:%M:%S or
            ISO-8601 %Y-%m-%dT%H:%M:%S+%Z
        date_to (Union[Unset, None, str]): Date in the formats %Y-%m-%d, %Y-%m-%d %H:%M:%S or
            ISO-8601 %Y-%m-%dT%H:%M:%S+%Z
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):

    Returns:
        Response[Union[HTTPValidationError, ResponseListmodelsEodPrice]]
    """

    kwargs = _get_kwargs(
        date=date,
        client=client,
        access_key=access_key,
        symbols=symbols,
        exchange=exchange,
        sort=sort,
        date_from=date_from,
        date_to=date_to,
        limit=limit,
        offset=offset,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    date: str,
    *,
    client: Client,
    access_key: str,
    symbols: Union[Unset, None, str] = UNSET,
    exchange: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, Sort] = UNSET,
    date_from: Union[Unset, None, str] = UNSET,
    date_to: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseListmodelsEodPrice]]:
    """Date

    Args:
        date (str): Date in the formats %Y-%m-%d, %Y-%m-%d %H:%M:%S or ISO-8601
            %Y-%m-%dT%H:%M:%S+%Z
        access_key (str):
        symbols (Union[Unset, None, str]):
        exchange (Union[Unset, None, str]):
        sort (Union[Unset, None, Sort]): An enumeration.
        date_from (Union[Unset, None, str]): Date in the formats %Y-%m-%d, %Y-%m-%d %H:%M:%S or
            ISO-8601 %Y-%m-%dT%H:%M:%S+%Z
        date_to (Union[Unset, None, str]): Date in the formats %Y-%m-%d, %Y-%m-%d %H:%M:%S or
            ISO-8601 %Y-%m-%dT%H:%M:%S+%Z
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):

    Returns:
        Response[Union[HTTPValidationError, ResponseListmodelsEodPrice]]
    """

    return sync_detailed(
        date=date,
        client=client,
        access_key=access_key,
        symbols=symbols,
        exchange=exchange,
        sort=sort,
        date_from=date_from,
        date_to=date_to,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    date: str,
    *,
    client: Client,
    access_key: str,
    symbols: Union[Unset, None, str] = UNSET,
    exchange: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, Sort] = UNSET,
    date_from: Union[Unset, None, str] = UNSET,
    date_to: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseListmodelsEodPrice]]:
    """Date

    Args:
        date (str): Date in the formats %Y-%m-%d, %Y-%m-%d %H:%M:%S or ISO-8601
            %Y-%m-%dT%H:%M:%S+%Z
        access_key (str):
        symbols (Union[Unset, None, str]):
        exchange (Union[Unset, None, str]):
        sort (Union[Unset, None, Sort]): An enumeration.
        date_from (Union[Unset, None, str]): Date in the formats %Y-%m-%d, %Y-%m-%d %H:%M:%S or
            ISO-8601 %Y-%m-%dT%H:%M:%S+%Z
        date_to (Union[Unset, None, str]): Date in the formats %Y-%m-%d, %Y-%m-%d %H:%M:%S or
            ISO-8601 %Y-%m-%dT%H:%M:%S+%Z
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):

    Returns:
        Response[Union[HTTPValidationError, ResponseListmodelsEodPrice]]
    """

    kwargs = _get_kwargs(
        date=date,
        client=client,
        access_key=access_key,
        symbols=symbols,
        exchange=exchange,
        sort=sort,
        date_from=date_from,
        date_to=date_to,
        limit=limit,
        offset=offset,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    date: str,
    *,
    client: Client,
    access_key: str,
    symbols: Union[Unset, None, str] = UNSET,
    exchange: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, Sort] = UNSET,
    date_from: Union[Unset, None, str] = UNSET,
    date_to: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseListmodelsEodPrice]]:
    """Date

    Args:
        date (str): Date in the formats %Y-%m-%d, %Y-%m-%d %H:%M:%S or ISO-8601
            %Y-%m-%dT%H:%M:%S+%Z
        access_key (str):
        symbols (Union[Unset, None, str]):
        exchange (Union[Unset, None, str]):
        sort (Union[Unset, None, Sort]): An enumeration.
        date_from (Union[Unset, None, str]): Date in the formats %Y-%m-%d, %Y-%m-%d %H:%M:%S or
            ISO-8601 %Y-%m-%dT%H:%M:%S+%Z
        date_to (Union[Unset, None, str]): Date in the formats %Y-%m-%d, %Y-%m-%d %H:%M:%S or
            ISO-8601 %Y-%m-%dT%H:%M:%S+%Z
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):

    Returns:
        Response[Union[HTTPValidationError, ResponseListmodelsEodPrice]]
    """

    return (
        await asyncio_detailed(
            date=date,
            client=client,
            access_key=access_key,
            symbols=symbols,
            exchange=exchange,
            sort=sort,
            date_from=date_from,
            date_to=date_to,
            limit=limit,
            offset=offset,
        )
    ).parsed
