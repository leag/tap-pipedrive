import singer
from requests import RequestException
from tap_pipedrive.streams.recents import RecentsStream


logger = singer.get_logger()


class DynamicTypingRecentsStream(RecentsStream):
    schema_path = "schemas/recents/dynamic_typing/{}.json"
    static_fields = []
    fields_endpoint = ""

    def get_schema(self):
        if not self.schema_cache:
            schema = self.load_schema()
            self.schema_cache = schema
        return self.schema_cache
