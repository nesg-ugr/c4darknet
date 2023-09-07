import re

class SiteData:
    def __init__(self, id, name, error_tries, discovering_tries, pages, uuid, type, current_status, source, timestamp, timestamp_s):
        self.id = id
        self.name = name
        self.error_tries = error_tries
        self.discovering_tries = discovering_tries
        self.pages = pages
        self.uuid = uuid
        self.type = type
        self.current_status = current_status
        self.source = source
        self.timestamp = timestamp
        self.timestamp_s = timestamp_s

    def extract_id_from_string(self, string):
        # Función para extraer el número de una cadena como "SiteType[5]", "SiteStatus[2]" o "SiteSource[1]"
        match = re.search(r"\[(\d+)\]", string)
        if match:
            return int(match.group(1))
        return None

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "error_tries": self.error_tries,
            "discovering_tries": self.discovering_tries,
            "pages": self.pages,
            "uuid": self.uuid,
            "type": self.extract_id_from_string(self.type),  # Extraer el número del campo type
            "current_status": self.extract_id_from_string(self.current_status),  # Extraer el número del campo current_status
            "source": self.extract_id_from_string(self.source),  # Extraer el número del campo source
            "timestamp": self.timestamp,
            "timestamp_s": self.timestamp_s
        }