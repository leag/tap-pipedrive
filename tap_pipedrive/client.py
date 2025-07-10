"""REST client handling, including PipedriveStream base class."""

from __future__ import annotations

import typing as t
from importlib import resources

from singer_sdk.authenticators import APIKeyAuthenticator
from singer_sdk.streams import RESTStream

if t.TYPE_CHECKING:
    from singer_sdk.exceptions import RetriableAPIError
    from singer_sdk.helpers.types import Context

SCHEMAS_DIR = resources.files(__package__) / "schemas"


class PipedriveStream(RESTStream):
    """Pipedrive stream class."""

    next_page_token_jsonpath = "$.additional_data.pagination.next_start"  # noqa: S105
    primary_keys = ("id",)
    records_jsonpath = "$.data[*]"
    url_base = "https://api.pipedrive.com/"

    @property
    def authenticator(self) -> APIKeyAuthenticator:
        """Return a new authenticator object.

        Returns:
            An authenticator instance.
        """
        return APIKeyAuthenticator.create_for_stream(
            self,
            key="api_token",
            value=self.config.get("api_token", ""),
            location="params",
        )

    def get_url_params(
        self,
        context: Context | None,  # noqa: ARG002
        next_page_token: t.Any | None,  # noqa: ANN401
    ) -> dict[str, t.Any]:
        """Return a dictionary of values to be used in URL parameterization.

        Args:
            context: The stream context.
            next_page_token: The next page index or value.

        Returns:
            A dictionary of URL query parameters.
        """
        params: dict = {}
        params["limit"] = self.config.get("page_size", 50)
        if next_page_token is not None:
            params["start"] = next_page_token
        return params

    def backoff_jitter(
        self,
        value: int,
    ) -> int:
        """Disable backoff jitter."""
        return value

    def backoff_wait_generator(
        self,
    ) -> t.Callable[..., t.Generator[int, t.Any, None]]:
        """The wait generator for backoff.

        Returns:
            A callable that generates wait times for backoff.
        """

        def _backoff_from_headers(retriable_api_error: RetriableAPIError) -> int:
            try:
                response_headers = retriable_api_error.response.headers
                return int(response_headers.get("X-RateLimit-Reset", 0))
            except (AttributeError, ValueError, TypeError):
                return 0

        return self.backoff_runtime(value=_backoff_from_headers)
