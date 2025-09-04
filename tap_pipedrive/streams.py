"""Stream type classes for tap-pipedrive."""

from __future__ import annotations

import typing as t
from importlib import resources

from singer_sdk.authenticators import APIKeyAuthenticator

from tap_pipedrive.client import PipedriveStream

if t.TYPE_CHECKING:
    from singer_sdk.helpers import types
    from singer_sdk.helpers.types import Context
    from singer_sdk.streams.rest import _TToken

SCHEMAS_DIR = resources.files(__package__) / "schemas"


class DealsStream(PipedriveStream):
    """Pipedrive deals stream.

    API Documentation: https://developers.pipedrive.com/docs/api/v1/Deals
    """

    name = "deals"
    path = "v2/deals"
    replication_key = "update_time"
    records_jsonpath = "$.data[*]"
    schema_filepath = SCHEMAS_DIR / "deals.json"
    url_base = "https://preyinc2.pipedrive.com/api/"
    next_page_token_jsonpath = "$.additional_data.next_cursor"  # noqa: S105
    is_sorted = True

    @property
    def authenticator(self) -> APIKeyAuthenticator:
        """Return a new authenticator object with header authentication for v2 API."""
        return APIKeyAuthenticator.create_for_stream(
            self,
            key="x-api-token",
            value=self.config.get("api_token", ""),
            location="header",
        )

    def get_url_params(
        self,
        context: Context | None,
        next_page_token: _TToken | None,
    ) -> dict[str, t.Any]:
        """Return URL parameters for the request."""
        params: dict = {}
        params["limit"] = self.config.get("page_size", 500)
        params["sort_by"] = "update_time"
        params["status"] = "open,won,lost,deleted"  # include all deals

        starting_date = self.get_starting_timestamp(context)
        if starting_date:
            params["updated_since"] = starting_date.strftime("%Y-%m-%dT%H:%M:%SZ")
        if next_page_token is not None:
            params["cursor"] = next_page_token
        return params

    def post_process(
        self,
        row: types.Record,
        context: types.Context | None = None,  # noqa: ARG002
    ) -> dict | None:
        """Move custom_fields to the top level."""
        if "custom_fields" in row:
            row.update(row.pop("custom_fields"))
        return row

    def get_child_context(
        self,
        record: dict,
        context: Context | None = None,  # noqa: ARG002
    ) -> Context:
        """Return the context for child streams."""
        return {"deal_id": record["id"]}


class DealFieldsStream(PipedriveStream):
    """Pipedrive deal_fields stream.

    API Documentation: https://developers.pipedrive.com/docs/api/v1/DealFields
    """

    name = "deal_fields"
    path = "v1/dealFields"
    primary_keys = ("key",)
    schema_filepath = SCHEMAS_DIR / "deal_fields.json"


class GoalsStream(PipedriveStream):
    """Pipedrive goals stream.

    API Documentation: https://developers.pipedrive.com/docs/api/v1/Goals
    """

    name = "goals"
    path = "v1/goals/find"
    records_jsonpath = "$.data.goals[*]"
    schema_filepath = SCHEMAS_DIR / "goals.json"


class FilesStream(PipedriveStream):
    """Pipedrive files stream.

    API Documentation: https://developers.pipedrive.com/docs/api/v1/Files
    """

    name = "files"
    path = "v1/recents"
    replication_key = "update_time"
    records_jsonpath = "$.data[*].data[*]"
    schema_filepath = SCHEMAS_DIR / "files.json"

    def get_url_params(
        self,
        context: Context | None,
        next_page_token: _TToken | None,
    ) -> dict[str, t.Any]:
        """Return URL parameters for the request."""
        params: dict = super().get_url_params(context, next_page_token)
        starting_date = self.get_starting_timestamp(context)
        if starting_date:
            params["since_timestamp"] = starting_date.strftime("%Y-%m-%d %H:%M:%S")
        params["items"] = "file"
        return params


class FiltersStream(PipedriveStream):
    """Pipedrive filters stream.

    API Documentation: https://developers.pipedrive.com/docs/api/v1/Filters
    """

    name = "filters"
    path = "v1/filters"
    schema_filepath = SCHEMAS_DIR / "filters.json"


class LeadLabelsStream(PipedriveStream):
    """Pipedrive lead_labels stream.

    API Documentation: https://developers.pipedrive.com/docs/api/v1/LeadLabels
    """

    name = "lead_labels"
    path = "v1/leadLabels"
    schema_filepath = SCHEMAS_DIR / "lead_labels.json"


class LeadsStream(PipedriveStream):
    """Pipedrive leads stream.

    API Documentation: https://developers.pipedrive.com/docs/api/v1/Leads
    """

    name = "leads"
    path = "v1/leads"
    schema_filepath = SCHEMAS_DIR / "leads.json"


class NotesStream(PipedriveStream):
    """Pipedrive notes stream.

    API Documentation: https://developers.pipedrive.com/docs/api/v1/Notes
    """

    name = "notes"
    path = "v1/recents"
    replication_key = "update_time"
    records_jsonpath = "$.data[*].data[*]"
    schema_filepath = SCHEMAS_DIR / "notes.json"

    def get_url_params(
        self,
        context: Context | None,
        next_page_token: _TToken | None,
    ) -> dict[str, t.Any]:
        """Return URL parameters for the request."""
        params: dict = super().get_url_params(context, next_page_token)
        starting_date = self.get_starting_timestamp(context)
        if starting_date:
            params["since_timestamp"] = starting_date.strftime("%Y-%m-%d %H:%M:%S")
        params["items"] = "note"
        return params


class ActivitiesStream(PipedriveStream):
    """Pipedrive activities stream.

    API Documentation: https://developers.pipedrive.com/docs/api/v1/Activities
    """

    name = "activities"
    path = "v2/activities"
    replication_key = "update_time"
    records_jsonpath = "$.data[*]"
    schema_filepath = SCHEMAS_DIR / "activities.json"
    url_base = "https://preyinc2.pipedrive.com/api/"
    next_page_token_jsonpath = "$.additional_data.next_cursor"  # noqa: S105
    is_sorted = True

    @property
    def authenticator(self) -> APIKeyAuthenticator:
        """Return a new authenticator object with header authentication for v2 API."""
        return APIKeyAuthenticator.create_for_stream(
            self,
            key="x-api-token",
            value=self.config.get("api_token", ""),
            location="header",
        )

    def get_url_params(
        self,
        context: Context | None,
        next_page_token: _TToken | None,
    ) -> dict[str, t.Any]:
        """Return URL parameters for the request."""
        params: dict = {}
        params["limit"] = self.config.get("page_size", 500)
        params["sort_by"] = "update_time"

        starting_date = self.get_starting_timestamp(context)
        if starting_date:
            params["updated_since"] = starting_date.strftime("%Y-%m-%dT%H:%M:%SZ")
        if next_page_token is not None:
            params["cursor"] = next_page_token
        return params


class ActivityTypesStream(PipedriveStream):
    """Pipedrive activity_types stream.

    API Documentation: https://developers.pipedrive.com/docs/api/v1/ActivityTypes
    """

    name = "activity_types"
    path = "v1/recents"
    replication_key = "update_time"
    records_jsonpath = "$.data[*].data[*]"
    schema_filepath = SCHEMAS_DIR / "activity_types.json"

    def get_url_params(
        self,
        context: Context | None,
        next_page_token: _TToken | None,
    ) -> dict[str, t.Any]:
        """Return URL parameters for the request."""
        params: dict = super().get_url_params(context, next_page_token)
        starting_date = self.get_starting_timestamp(context)
        if starting_date:
            params["since_timestamp"] = starting_date.strftime("%Y-%m-%d %H:%M:%S")
        params["items"] = "activityType"
        return params


class ActivityFieldsStream(PipedriveStream):
    """Pipedrive activity_fields stream.

    API Documentation: https://developers.pipedrive.com/docs/api/v1/ActivityFields
    """

    name = "activity_fields"
    path = "v1/activityFields"
    primary_keys = ("key",)
    schema_filepath = SCHEMAS_DIR / "activity_fields.json"


class CurrenciesStream(PipedriveStream):
    """Pipedrive currencies stream.

    API Documentation: https://developers.pipedrive.com/docs/api/v1/Currencies
    """

    name = "currencies"
    path = "v1/currencies"
    schema_filepath = SCHEMAS_DIR / "currencies.json"


class MailThreadsStream(PipedriveStream):
    """Pipedrive mailThreads stream.

    API Documentation: https://developers.pipedrive.com/docs/api/v1/Mailbox
    """

    name = "mailThreads"
    path = "v1/mailbox/mailThreads"
    schema_filepath = SCHEMAS_DIR / "mailThreads.json"

    def get_child_context(
        self,
        record: dict,
        context: Context | None = None,  # noqa: ARG002
    ) -> Context:
        """Return the context for child streams."""
        return {"thread_id": record["id"]}


class MailStream(PipedriveStream):
    """Pipedrive mail stream.

    API Documentation: https://developers.pipedrive.com/docs/api/v1/Mailbox
    """

    name = "mail"
    path = "v1/mailbox/mailThreads/{thread_id}/mailMessages"
    parent_stream_type = MailThreadsStream
    schema_filepath = SCHEMAS_DIR / "mail.json"


class OrganizationsStream(PipedriveStream):
    """Pipedrive organizations stream.

    API Documentation: https://developers.pipedrive.com/docs/api/v1/Organizations
    """

    name = "organizations"
    path = "v2/organizations"
    replication_key = "update_time"
    records_jsonpath = "$.data[*]"
    schema_filepath = SCHEMAS_DIR / "organizations.json"
    url_base = "https://preyinc2.pipedrive.com/api/"
    next_page_token_jsonpath = "$.additional_data.next_cursor"  # noqa: S105
    is_sorted = True

    @property
    def authenticator(self) -> APIKeyAuthenticator:
        """Return a new authenticator object with header authentication for v2 API."""
        return APIKeyAuthenticator.create_for_stream(
            self,
            key="x-api-token",
            value=self.config.get("api_token", ""),
            location="header",
        )

    def get_url_params(
        self,
        context: Context | None,
        next_page_token: _TToken | None,
    ) -> dict[str, t.Any]:
        """Return URL parameters for the request."""
        params: dict = {}
        params["limit"] = self.config.get("page_size", 500)
        params["sort_by"] = "update_time"

        starting_date = self.get_starting_timestamp(context)
        if starting_date:
            params["updated_since"] = starting_date.strftime("%Y-%m-%dT%H:%M:%SZ")
        if next_page_token is not None:
            params["cursor"] = next_page_token
        return params

    def post_process(
        self,
        row: types.Record,
        context: types.Context | None = None,  # noqa: ARG002
    ) -> dict | None:
        """Move custom_fields to the top level."""
        if "custom_fields" in row:
            row.update(row.pop("custom_fields"))
        return row


class OrganizationFieldsStream(PipedriveStream):
    """Pipedrive organization_fields stream.

    API Documentation: https://developers.pipedrive.com/docs/api/v1/OrganizationFields
    """

    name = "organization_fields"
    path = "v1/organizationFields"
    primary_keys = ("key",)
    schema_filepath = SCHEMAS_DIR / "organization_fields.json"


class PermissionSetsStream(PipedriveStream):
    """Pipedrive permission_sets stream.

    API Documentation: https://developers.pipedrive.com/docs/api/v1/PermissionSets
    """

    name = "permission_sets"
    path = "v1/permissionSets"
    schema_filepath = SCHEMAS_DIR / "permission_sets.json"


class PersonsStream(PipedriveStream):
    """Pipedrive persons stream.

    API Documentation: https://developers.pipedrive.com/docs/api/v1/Persons
    """

    name = "persons"
    path = "v2/persons"
    replication_key = "update_time"
    records_jsonpath = "$.data[*]"
    schema_filepath = SCHEMAS_DIR / "persons.json"
    url_base = "https://preyinc2.pipedrive.com/api/"
    next_page_token_jsonpath = "$.additional_data.next_cursor"  # noqa: S105

    @property
    def authenticator(self) -> APIKeyAuthenticator:
        """Return a new authenticator object with header authentication for v2 API."""
        return APIKeyAuthenticator.create_for_stream(
            self,
            key="x-api-token",
            value=self.config.get("api_token", ""),
            location="header",
        )

    def get_url_params(
        self,
        context: Context | None,
        next_page_token: _TToken | None,
    ) -> dict[str, t.Any]:
        """Return URL parameters for the request."""
        params: dict = {}
        params["limit"] = self.config.get("page_size", 100)  # v2 supports up to 500

        starting_date = self.get_starting_timestamp(context)
        if starting_date:
            params["updated_since"] = starting_date.strftime("%Y-%m-%dT%H:%M:%SZ")

        if next_page_token is not None:
            params["cursor"] = next_page_token
        return params

    def post_process(
        self,
        row: types.Record,
        context: types.Context | None = None,  # noqa: ARG002
    ) -> dict | None:
        """Move custom_fields to the top level."""
        if "custom_fields" in row:
            row.update(row.pop("custom_fields"))
        return row



class PersonFieldsStream(PipedriveStream):
    """Pipedrive person_fields stream.

    API Documentation: https://developers.pipedrive.com/docs/api/v1/PersonFields
    """

    name = "person_fields"
    path = "v1/personFields"
    primary_keys = ("key",)
    schema_filepath = SCHEMAS_DIR / "person_fields.json"


class PipelinesStream(PipedriveStream):
    """Pipedrive pipelines stream.

    API Documentation: https://developers.pipedrive.com/docs/api/v1/Pipelines
    """

    name = "pipelines"
    path = "v1/recents"
    replication_key = "update_time"
    records_jsonpath = "$.data[*].data[*]"
    schema_filepath = SCHEMAS_DIR / "pipelines.json"

    def get_url_params(
        self,
        context: Context | None,
        next_page_token: _TToken | None,
    ) -> dict[str, t.Any]:
        """Return URL parameters for the request."""
        params: dict = super().get_url_params(context, next_page_token)
        starting_date = self.get_starting_timestamp(context)
        if starting_date:
            params["since_timestamp"] = starting_date.strftime("%Y-%m-%d %H:%M:%S")
        params["items"] = "pipeline"
        return params


class ProductsStream(PipedriveStream):
    """Pipedrive products stream.

    API Documentation: https://developers.pipedrive.com/docs/api/v1/Products
    """

    name = "products"
    path = "v1/recents"
    replication_key = "update_time"
    records_jsonpath = "$.data[*].data[*]"
    schema_filepath = SCHEMAS_DIR / "products.json"

    def get_url_params(
        self,
        context: Context | None,
        next_page_token: _TToken | None,
    ) -> dict[str, t.Any]:
        """Return URL parameters for the request."""
        params: dict = super().get_url_params(context, next_page_token)
        starting_date = self.get_starting_timestamp(context)
        if starting_date:
            params["since_timestamp"] = starting_date.strftime("%Y-%m-%d %H:%M:%S")
        params["items"] = "product"
        return params


class ProductFieldsStream(PipedriveStream):
    """Pipedrive product_fields stream.

    API Documentation: https://developers.pipedrive.com/docs/api/v1/ProductFields
    """

    name = "product_fields"
    path = "v1/productFields"
    primary_keys = ("key",)
    schema_filepath = SCHEMAS_DIR / "product_fields.json"


class RolesStream(PipedriveStream):
    """Pipedrive roles stream.

    API Documentation: https://developers.pipedrive.com/docs/api/v1/Roles
    """

    name = "roles"
    path = "v1/roles"
    schema_filepath = SCHEMAS_DIR / "roles.json"


class StagesStream(PipedriveStream):
    """Pipedrive stages stream.

    API Documentation: https://developers.pipedrive.com/docs/api/v1/Stages
    """

    name = "stages"
    path = "v1/stages"
    schema_filepath = SCHEMAS_DIR / "stages.json"


class UsersStream(PipedriveStream):
    """Pipedrive users stream.

    API Documentation: https://developers.pipedrive.com/docs/api/v1/Users
    """

    name = "users"
    path = "v1/recents"
    records_jsonpath = "$.data[*].data[*]"
    replication_key = "modified"
    schema_filepath = SCHEMAS_DIR / "users.json"

    def get_url_params(
        self,
        context: Context | None,
        next_page_token: _TToken | None,
    ) -> dict[str, t.Any]:
        """Return URL parameters for the request."""
        params: dict = super().get_url_params(context, next_page_token)
        starting_date = self.get_starting_timestamp(context)
        if starting_date:
            params["since_timestamp"] = starting_date.strftime("%Y-%m-%d %H:%M:%S")
        params["items"] = "user"
        return params


class DealProductsStream(PipedriveStream):
    """Pipedrive deal_products stream.

    API Documentation: https://developers.pipedrive.com/docs/api/v1/Deals
    """

    name = "deal_products"
    path = "v1/deals/{deal_id}/products"
    parent_stream_type = DealsStream
    schema_filepath = SCHEMAS_DIR / "deal_products.json"
