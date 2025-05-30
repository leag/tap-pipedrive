"""Stream type classes for tap-pipedrive."""

from __future__ import annotations

import typing as t
from importlib import resources

from tap_pipedrive.client import PipedriveStream

if t.TYPE_CHECKING:
    from singer_sdk.helpers.types import Context
    from singer_sdk.streams.rest import _TToken

SCHEMAS_DIR = resources.files(__package__) / "schemas"


class DealsStream(PipedriveStream):
    """Pipedrive deals stream."""

    name = "deals"
    path = "v1/recents"
    replication_key = "update_time"
    records_jsonpath = "$.data[*].data[*]"
    schema_filepath = SCHEMAS_DIR / "deals.json"

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
        params["items"] = "deal"
        return params

    def get_child_context(
        self,
        record: dict,
        context: Context | None = None,  # noqa: ARG002
    ) -> Context:
        """Return the context for child streams."""
        return {"deal_id": record["id"]}


class DealFieldsStream(PipedriveStream):
    """Pipedrive deal_fields stream."""

    name = "deal_fields"
    path = "v1/dealFields"
    schema_filepath = SCHEMAS_DIR / "deal_fields.json"
    primary_keys = ("key",)


class GoalsStream(PipedriveStream):
    """Pipedrive goals stream."""

    name = "goals"
    path = "v1/goals/find"
    records_jsonpath = "$.data.goals[*]"
    schema_filepath = SCHEMAS_DIR / "goals.json"


class FilesStream(PipedriveStream):
    """Pipedrive files stream."""

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
    """Pipedrive filters stream."""

    name = "filters"
    path = "v1/filters"
    schema_filepath = SCHEMAS_DIR / "filters.json"


class LeadLabelsStream(PipedriveStream):
    """Pipedrive lead_labels stream."""

    name = "lead_labels"
    path = "v1/leadLabels"
    schema_filepath = SCHEMAS_DIR / "lead_labels.json"


class LeadsStream(PipedriveStream):
    """Pipedrive leads stream."""

    name = "leads"
    path = "v1/leads"
    schema_filepath = SCHEMAS_DIR / "leads.json"


class NotesStream(PipedriveStream):
    """Pipedrive notes stream."""

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
    """Pipedrive activities stream."""

    name = "activities"
    path = "v1/recents"
    replication_key = "update_time"
    records_jsonpath = "$.data[*].data[*]"
    schema_filepath = SCHEMAS_DIR / "activities.json"

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
        params["items"] = "activity"
        return params


class ActivityTypesStream(PipedriveStream):
    """Pipedrive activity_types stream."""

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
    """Pipedrive activity_fields stream."""

    name = "activity_fields"
    path = "v1/activityFields"
    schema_filepath = SCHEMAS_DIR / "activity_fields.json"


class CurrenciesStream(PipedriveStream):
    """Pipedrive currencies stream."""

    name = "currencies"
    path = "v1/currencies"
    schema_filepath = SCHEMAS_DIR / "currencies.json"


class MailThreadsStream(PipedriveStream):
    """Pipedrive mailThreads stream."""

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
    """Pipedrive mail stream."""

    name = "mail"
    path = "v1/mailbox/mailThreads/{thread_id}/mailMessages"
    parent_stream_type = MailThreadsStream
    schema_filepath = SCHEMAS_DIR / "mail.json"


class OrganizationsStream(PipedriveStream):
    """Pipedrive organizations stream."""

    name = "organizations"
    path = "v1/recents"
    replication_key = "update_time"
    records_jsonpath = "$.data[*].data[*]"
    schema_filepath = SCHEMAS_DIR / "organizations.json"

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
        params["items"] = "organization"
        return params


class OrganizationFieldsStream(PipedriveStream):
    """Pipedrive organization_fields stream."""

    name = "organization_fields"
    path = "v1/organizationFields"
    schema_filepath = SCHEMAS_DIR / "organization_fields.json"


class PermissionSetsStream(PipedriveStream):
    """Pipedrive permission_sets stream."""

    name = "permission_sets"
    path = "v1/permissionSets"
    schema_filepath = SCHEMAS_DIR / "permission_sets.json"


class PersonsStream(PipedriveStream):
    """Pipedrive persons stream."""

    name = "persons"
    path = "v1/recents"
    replication_key = "update_time"
    records_jsonpath = "$.data[*].data[*]"
    schema_filepath = SCHEMAS_DIR / "persons.json"

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
        params["items"] = "person"
        return params


class PersonFieldsStream(PipedriveStream):
    """Pipedrive person_fields stream."""

    name = "person_fields"
    path = "v1/personFields"
    schema_filepath = SCHEMAS_DIR / "person_fields.json"


class PipelinesStream(PipedriveStream):
    """Pipedrive pipelines stream."""

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
    """Pipedrive products stream."""

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
    """Pipedrive product_fields stream."""

    name = "product_fields"
    path = "v1/productFields"
    schema_filepath = SCHEMAS_DIR / "product_fields.json"
    primary_keys = ("key",)


class RolesStream(PipedriveStream):
    """Pipedrive roles stream."""

    name = "roles"
    path = "v1/roles"
    schema_filepath = SCHEMAS_DIR / "roles.json"


class StagesStream(PipedriveStream):
    """Pipedrive stages stream."""

    name = "stages"
    path = "v1/stages"
    schema_filepath = SCHEMAS_DIR / "stages.json"


class UsersStream(PipedriveStream):
    """Pipedrive users stream."""

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
    """Pipedrive deal_products stream."""

    name = "deal_products"
    path = "v1/deals/{deal_id}/products"
    parent_stream_type = DealsStream
    schema_filepath = SCHEMAS_DIR / "deal_products.json"
