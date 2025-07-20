"""Tests standard tap features using the built-in SDK tests library."""

import datetime

from singer_sdk.testing import SuiteConfig, get_tap_test_class

from tap_pipedrive.tap import TapPipedrive

SAMPLE_CONFIG = {
    "start_date": (
        datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=30)
    ).strftime("%Y-%m-%d %H:%M:%S"),
}

TestTapPipedrive = get_tap_test_class(
    tap_class=TapPipedrive,
    config=SAMPLE_CONFIG,
    suite_config=SuiteConfig(ignore_no_records=True, max_records_limit=50),
)
