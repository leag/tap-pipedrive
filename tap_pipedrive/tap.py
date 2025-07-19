"""Pipedrive tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th

from tap_pipedrive import streams


class TapPipedrive(Tap):
    """Pipedrive tap class."""

    name = "tap-pipedrive"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_token",
            th.StringType(nullable=False),
            required=True,
            secret=True,
            title="Auth Token",
            description="The token to authenticate against the API service",
        ),
        th.Property(
            "start_date",
            th.DateTimeType(nullable=True),
            description="The earliest record date to sync",
            required=True,
        ),
        th.Property(
            "page_size",
            th.IntegerType(minimum=1, maximum=500),
            default=50,
            description="Number of records to return per API request (1-500)",
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.PipedriveStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.DealsStream(self),
            # streams.DealFieldsStream(self),
            # streams.GoalsStream(self),
            # streams.FilesStream(self),
            # streams.FiltersStream(self),
            # streams.LeadLabelsStream(self),
            # streams.LeadsStream(self),
            # streams.NotesStream(self),
            # streams.ActivitiesStream(self),
            # streams.ActivityFieldsStream(self),
            # streams.ActivityTypesStream(self),
            # streams.CurrenciesStream(self),
            # streams.MailThreadsStream(self),
            # streams.MailStream(self),
            # streams.OrganizationsStream(self),
            # streams.OrganizationFieldsStream(self),
            # streams.PermissionSetsStream(self),
            # streams.PersonsStream(self),
            # streams.PersonFieldsStream(self),
            # streams.PipelinesStream(self),
            # streams.ProductsStream(self),
            # streams.ProductFieldsStream(self),
            # streams.RolesStream(self),
            # streams.StagesStream(self),
            # streams.UsersStream(self),
            streams.DealProductsStream(self),
        ]


if __name__ == "__main__":
    TapPipedrive.cli()
