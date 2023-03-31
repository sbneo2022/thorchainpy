from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.liquidity_provider_summary import LiquidityProviderSummary
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset: str,
    *,
    client: Client,
    height: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/thorchain/pool/{asset}/liquidity_providers".format(client.base_url, asset=asset)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[List["LiquidityProviderSummary"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_liquidity_providers_response_item_data in _response_200:
            componentsschemas_liquidity_providers_response_item = LiquidityProviderSummary.from_dict(
                componentsschemas_liquidity_providers_response_item_data
            )

            response_200.append(componentsschemas_liquidity_providers_response_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[List["LiquidityProviderSummary"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset: str,
    *,
    client: Client,
    height: Union[Unset, None, int] = UNSET,
) -> Response[List["LiquidityProviderSummary"]]:
    """Returns all liquidity provider information for an asset.

    Args:
        asset (str):  Example: BTC.BTC.
        height (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['LiquidityProviderSummary']]
    """

    kwargs = _get_kwargs(
        asset=asset,
        client=client,
        height=height,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset: str,
    *,
    client: Client,
    height: Union[Unset, None, int] = UNSET,
) -> Optional[List["LiquidityProviderSummary"]]:
    """Returns all liquidity provider information for an asset.

    Args:
        asset (str):  Example: BTC.BTC.
        height (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['LiquidityProviderSummary']
    """

    return sync_detailed(
        asset=asset,
        client=client,
        height=height,
    ).parsed


async def asyncio_detailed(
    asset: str,
    *,
    client: Client,
    height: Union[Unset, None, int] = UNSET,
) -> Response[List["LiquidityProviderSummary"]]:
    """Returns all liquidity provider information for an asset.

    Args:
        asset (str):  Example: BTC.BTC.
        height (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['LiquidityProviderSummary']]
    """

    kwargs = _get_kwargs(
        asset=asset,
        client=client,
        height=height,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset: str,
    *,
    client: Client,
    height: Union[Unset, None, int] = UNSET,
) -> Optional[List["LiquidityProviderSummary"]]:
    """Returns all liquidity provider information for an asset.

    Args:
        asset (str):  Example: BTC.BTC.
        height (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['LiquidityProviderSummary']
    """

    return (
        await asyncio_detailed(
            asset=asset,
            client=client,
            height=height,
        )
    ).parsed
