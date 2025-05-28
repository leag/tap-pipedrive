"""Stream type classes for tap-pipedrive."""

from __future__ import annotations

import typing as t
from importlib import resources

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_pipedrive.client import PipedriveStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = resources.files(__package__) / "schemas"
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.


class DealsStream(PipedriveStream):
    """Pipedrive deals stream."""


class DealFieldsStream(PipedriveStream):
    """Pipedrive deal_fields stream."""


class GoalsStream(PipedriveStream):
    """Pipedrive goals stream."""


class FilesStream(PipedriveStream):
    """Pipedrive files stream."""


class FiltersStream(PipedriveStream):
    """Pipedrive filters stream."""


class LeadLabelsStream(PipedriveStream):
    """Pipedrive lead_labels stream."""


class LeadsStream(PipedriveStream):
    """Pipedrive leads stream."""


class NotesStream(PipedriveStream):
    """Pipedrive notes stream."""


class ActivitiesStream(PipedriveStream):
    """Pipedrive activities stream."""


class ActivityTypesStream(PipedriveStream):
    """Pipedrive activity_types stream."""


class ActivityFieldsStream(PipedriveStream):
    """Pipedrive activity_fields stream."""


class CurrenciesStream(PipedriveStream):
    """Pipedrive currencies stream."""


class MailStream(PipedriveStream):
    """Pipedrive mail stream."""


class OrganizationsStream(PipedriveStream):
    """Pipedrive organizations stream."""


class OrganizationFieldsStream(PipedriveStream):
    """Pipedrive organization_fields stream."""


class PermissionSetsStream(PipedriveStream):
    """Pipedrive permission_sets stream."""


class PersonsStream(PipedriveStream):
    """Pipedrive persons stream."""


class PersonFieldsStream(PipedriveStream):
    """Pipedrive person_fields stream."""


class PipelinesStream(PipedriveStream):
    """Pipedrive pipelines stream."""


class ProductsStream(PipedriveStream):
    """Pipedrive products stream."""


class ProductFieldsStream(PipedriveStream):
    """Pipedrive product_fields stream."""


class RolesStream(PipedriveStream):
    """Pipedrive roles stream."""


class StagesStream(PipedriveStream):
    """Pipedrive stages stream."""


class UsersStream(PipedriveStream):
    """Pipedrive users stream."""


class DealProductsStream(PipedriveStream):
    """Pipedrive deal_products stream."""


class MailThreadsStream(PipedriveStream):
    """Pipedrive mailThreads stream."""