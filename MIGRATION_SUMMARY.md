# Pipedrive API v2 Migration Summary

## Overview
This document summarizes the migration of Pipedrive tap streams from v1 to v2 API where supported.

## Migrated Streams (v1 → v2)

### ✅ Successfully Migrated to v2 API

1. **DealsStream**
   - **Endpoint**: `v1/recents` → `v2/deals`
   - **Records Path**: `$.data[*].data[*]` → `$.data[*]`
   - **Authentication**: Query param → Header (`x-api-token`)
   - **Pagination**: `start` → `cursor` with `next_cursor`
   - **Date Filter**: `since_timestamp` → `updated_since` (RFC3339 format)
   - **Documentation**: https://developers.pipedrive.com/docs/api/v1/Deals

2. **ActivitiesStream**
   - **Endpoint**: `v1/recents` → `v2/activities`
   - **Records Path**: `$.data[*].data[*]` → `$.data[*]`
   - **Authentication**: Query param → Header (`x-api-token`)
   - **Pagination**: `start` → `cursor` with `next_cursor`
   - **Date Filter**: `since_timestamp` → `updated_since` (RFC3339 format)
   - **Documentation**: https://developers.pipedrive.com/docs/api/v1/Activities

3. **OrganizationsStream** (Previously migrated)
   - **Documentation**: https://developers.pipedrive.com/docs/api/v1/Organizations

4. **PersonsStream** (Previously migrated)
   - **Documentation**: https://developers.pipedrive.com/docs/api/v1/Persons

## Streams Remaining on v1 API

The following streams do not have v2 API support and remain on v1:

### Field Streams
- **DealFieldsStream** - https://developers.pipedrive.com/docs/api/v1/DealFields
- **ActivityFieldsStream** - https://developers.pipedrive.com/docs/api/v1/ActivityFields
- **OrganizationFieldsStream** - https://developers.pipedrive.com/docs/api/v1/OrganizationFields
- **PersonFieldsStream** - https://developers.pipedrive.com/docs/api/v1/PersonFields
- **ProductFieldsStream** - https://developers.pipedrive.com/docs/api/v1/ProductFields

### Configuration Streams
- **GoalsStream** - https://developers.pipedrive.com/docs/api/v1/Goals
- **FiltersStream** - https://developers.pipedrive.com/docs/api/v1/Filters
- **PipelinesStream** - https://developers.pipedrive.com/docs/api/v1/Pipelines
- **StagesStream** - https://developers.pipedrive.com/docs/api/v1/Stages
- **RolesStream** - https://developers.pipedrive.com/docs/api/v1/Roles
- **PermissionSetsStream** - https://developers.pipedrive.com/docs/api/v1/PermissionSets
- **CurrenciesStream** - https://developers.pipedrive.com/docs/api/v1/Currencies

### Data Streams
- **FilesStream** - https://developers.pipedrive.com/docs/api/v1/Files
- **NotesStream** - https://developers.pipedrive.com/docs/api/v1/Notes
- **LeadsStream** - https://developers.pipedrive.com/docs/api/v1/Leads
- **LeadLabelsStream** - https://developers.pipedrive.com/docs/api/v1/LeadLabels
- **ProductsStream** - https://developers.pipedrive.com/docs/api/v1/Products
- **UsersStream** - https://developers.pipedrive.com/docs/api/v1/Users
- **ActivityTypesStream** - https://developers.pipedrive.com/docs/api/v1/ActivityTypes

### Mail Streams
- **MailThreadsStream** - https://developers.pipedrive.com/docs/api/v1/Mailbox
- **MailStream** - https://developers.pipedrive.com/docs/api/v1/Mailbox

### Child Streams
- **DealProductsStream** - https://developers.pipedrive.com/docs/api/v1/Deals

## Key Changes in v2 API Migration

### Authentication
- **v1**: API token passed as query parameter (`api_token`)
- **v2**: API token passed as header (`x-api-token`)

### Base URL
- **v1**: `https://api.pipedrive.com/`
- **v2**: `https://preyinc2.pipedrive.com/api/`

### Pagination
- **v1**: Offset-based with `start` parameter and `pagination.next_start`
- **v2**: Cursor-based with `cursor` parameter and `next_cursor`

### Records Path
- **v1**: Nested data structure `$.data[*].data[*]` (for recents endpoint)
- **v2**: Direct data array `$.data[*]`

### Date Filtering
- **v1**: `since_timestamp` with format `"%Y-%m-%d %H:%M:%S"`
- **v2**: `updated_since` with RFC3339 format `"%Y-%m-%dT%H:%M:%SZ"`

### Page Size Limits
- **v1**: Default 50, configurable via `page_size`
- **v2**: Default 100, maximum 500

### Custom Fields Handling
- **v2**: Added `post_process` method to flatten custom_fields to top level for better schema compatibility

## Benefits of v2 Migration

1. **Performance**: v2 API generally offers better performance and lower latency
2. **Pagination**: Cursor-based pagination is more reliable for large datasets
3. **Authentication**: Header-based authentication is more secure
4. **Field Selection**: v2 supports `custom_fields` parameter for optimized queries
5. **Sorting**: Better sorting capabilities with `sort_by` and `sort_direction`
6. **Filtering**: More advanced filtering options

## Testing
All migrations have been tested and pass the existing test suite.
