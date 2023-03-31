from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.mimir_response import MimirResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    address: str,
    *,
    client: Client,
    height: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/thorchain/mimir/node/{address}".format(client.base_url, address=address)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["height"] = height

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[MimirResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = MimirResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[MimirResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    address: str,
    *,
    client: Client,
    height: Union[Unset, None, int] = UNSET,
) -> Response[MimirResponse]:
    """Returns current node mimir configuration for the provided node address.

    Args:
        address (str):  Example: thor1zupk5lmc84r2dh738a9g3zscavannjy3nzplwt.
        height (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MimirResponse]
    """

    kwargs = _get_kwargs(
        address=address,
        client=client,
        height=height,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    address: str,
    *,
    client: Client,
    height: Union[Unset, None, int] = UNSET,
) -> Optional[MimirResponse]:
    """Returns current node mimir configuration for the provided node address.

    Args:
        address (str):  Example: thor1zupk5lmc84r2dh738a9g3zscavannjy3nzplwt.
        height (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MimirResponse
    """

    return sync_detailed(
        address=address,
        client=client,
        height=height,
    ).parsed


async def asyncio_detailed(
    address: str,
    *,
    client: Client,
    height: Union[Unset, None, int] = UNSET,
) -> Response[MimirResponse]:
    """Returns current node mimir configuration for the provided node address.

    Args:
        address (str):  Example: thor1zupk5lmc84r2dh738a9g3zscavannjy3nzplwt.
        height (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MimirResponse]
    """

    kwargs = _get_kwargs(
        address=address,
        client=client,
        height=height,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    address: str,
    *,
    client: Client,
    height: Union[Unset, None, int] = UNSET,
) -> Optional[MimirResponse]:
    """Returns current node mimir configuration for the provided node address.

    Args:
        address (str):  Example: thor1zupk5lmc84r2dh738a9g3zscavannjy3nzplwt.
        height (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MimirResponse
    """

    return (
        await asyncio_detailed(
            address=address,
            client=client,
            height=height,
        )
    ).parsed