"""Pipedrive entry point."""

from __future__ import annotations

from tap_pipedrive.tap import TapPipedrive

TapPipedrive.cli()
