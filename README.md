# tap-pipedrive

`tap-pipedrive` is a Singer tap for Pipedrive, designed to extract data from the Pipedrive API and output it in a format compatible with the Singer specification. This allows for easy integration with a variety of data warehousing and analysis tools.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps, this tap provides a robust and maintainable way to sync your Pipedrive data.

## Installation

Install from GitHub:

```bash
uv tool install git+https://github.com/leag/tap-pipedrive.git@main
```

## Configuration

This tap can be configured by creating a `config.json` file in your project directory or by using environment variables (see "Configure using environment variables" below). The required and optional settings are detailed in the "Settings" table.

## Capabilities

* `catalog`
* `state`
* `discover`
* `about`
* `stream-maps`
* `schema-flattening`
* `batch`

## Supported Python Versions

* 3.9
* 3.10
* 3.11
* 3.12
* 3.13

## Settings

| Setting | Required | Default | Description |
|:--------|:--------:|:-------:|:------------|
| api_token | True     | None    | The token to authenticate against the API service |
| start_date | True     | None    | The earliest record date to sync |
| stream_maps | False    | None    | Config object for stream maps capability. For more information check out [Stream Maps](https://sdk.meltano.com/en/latest/stream_maps.html). |
| stream_map_config | False    | None    | User-defined config values to be used within map expressions. |
| faker_config | False    | None    | Config for the [`Faker`](https://faker.readthedocs.io/en/master/) instance variable `fake` used within map expressions. Only applicable if the plugin specifies `faker` as an additional dependency (through the `singer-sdk` `faker` extra or directly). |
| faker_config.seed | False    | None    | Value to seed the Faker generator for deterministic output: https://faker.readthedocs.io/en/master/#seeding-the-generator |
| faker_config.locale | False    | None    | One or more LCID locale strings to produce localized output for: https://faker.readthedocs.io/en/master/#localization |
| flattening_enabled | False    | None    | 'True' to enable schema flattening and automatically expand nested properties. |
| flattening_max_depth | False    | None    | The max depth to flatten schemas. |
| batch_config | False    | None    | Configuration for BATCH message capabilities. |
| batch_config.encoding | False    | None    | Specifies the format and compression of the batch files. |
| batch_config.encoding.format | False    | None    | Format to use for batch files. |
| batch_config.encoding.compression | False    | None    | Compression format to use for batch files. |
| batch_config.storage | False    | None    | Defines the storage layer to use when writing batch files |
| batch_config.storage.root | False    | None    | Root path to use when writing batch files. |
| batch_config.storage.prefix | False    | None    | Prefix to use when writing batch files. |

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-pipedrive --about
```

## Available Data Streams

This tap supports the following data streams from the Pipedrive API:

* Deals
* Deal Fields
* Goals
* Files
* Filters
* Lead Labels
* Leads
* Notes
* Activities
* Activity Fields
* Activity Types
* Currencies
* Mail Threads
* Mail
* Organizations
* Organization Fields
* Permission Sets
* Persons
* Person Fields
* Pipelines
* Products
* Product Fields
* Roles
* Stages
* Users
* Deal Products

### Configure using environment variables

This Singer tap will automatically import any environment variables within the working directory's
`.env` if the `--config=ENV` is provided, such that config values will be considered if a matching
environment variable is set either in the terminal context or in the `.env` file.

### Source Authentication and Authorization

This tap requires an API token for authentication. You can obtain your API token from your Pipedrive account settings.

## Usage

You can run `tap-pipedrive` by itself, or in a pipeline with a target.

### Executing the Tap Directly

To run the tap directly and output the data to standard output, use the following command:

```bash
tap-pipedrive --config CONFIG --discover > ./catalog.json
tap-pipedrive --config CONFIG --catalog ./catalog.json > ./state.json
```

### Running with a Target

To run the tap with a target, such as `target-jsonl`, you can pipe the output of the tap to the target:

```bash
tap-pipedrive --config CONFIG --catalog ./catalog.json | target-jsonl > ./state.json
```

```bash
tap-pipedrive --version
tap-pipedrive --help
tap-pipedrive --config CONFIG --discover > ./catalog.json
```

## Developer Resources

Follow these instructions to contribute to this project.

### Initialize your Development Environment

Prerequisites:

- Python 3.9+
- [uv](https://docs.astral.sh/uv/)

```bash
uv sync
```

### Create and Run Tests

Create tests within the `tests` subfolder and
then run:

```bash
uv run pytest
```

You can also test the `tap-pipedrive` CLI interface directly using `uv run`:

```bash
uv run tap-pipedrive --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-pipedrive
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-pipedrive --version

# OR run a test ELT pipeline:
meltano run tap-pipedrive target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to
develop your own taps and targets.
