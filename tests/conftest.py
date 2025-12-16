"""Pytest configuration and hooks for tap-pipedrive tests."""

import pytest


# Streams with dynamic custom fields (hex-named fields from Pipedrive API)
STREAMS_WITH_CUSTOM_FIELDS = ["deals", "leads", "organizations", "persons"]


def pytest_collection_modifyitems(config, items):
    """Skip catalog schema tests for streams with dynamic custom fields."""
    for item in items:
        # Check if this is the catalog schema match test
        if "test_tap_stream_record_schema_matches_transformed_catalog" in item.nodeid:
            # Extract stream name from parametrized test name
            # Format: test_name[stream_name]
            if "[" in item.nodeid and "]" in item.nodeid:
                stream_name = item.nodeid.split("[")[-1].rstrip("]")
                if stream_name in STREAMS_WITH_CUSTOM_FIELDS:
                    item.add_marker(
                        pytest.mark.skip(
                            reason=f"Stream '{stream_name}' has dynamic custom fields"
                        )
                    )
