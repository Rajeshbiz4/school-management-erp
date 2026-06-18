from typing import Dict, List, Optional


class InMemoryStore:
    def __init__(self) -> None:
        self._data: Dict[str, Dict[str, dict]] = {}

    def list(self, container: str) -> List[dict]:
        return list(self._data.get(container, {}).values())

    def get(self, container: str, item_id: str) -> Optional[dict]:
        return self._data.get(container, {}).get(item_id)

    def upsert(self, container: str, item: dict) -> dict:
        self._data.setdefault(container, {})[item["id"]] = item
        return item

    def delete(self, container: str, item_id: str) -> bool:
        bucket = self._data.get(container, {})
        if item_id in bucket:
            del bucket[item_id]
            return True
        return False


store = InMemoryStore()
