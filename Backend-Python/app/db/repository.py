from typing import List, Optional

from app.core.config import get_settings
from app.db.in_memory_store import store


class BaseRepository:
    def __init__(self, container_name: str) -> None:
        self.container_name = container_name
        self.settings = get_settings()

    def _container(self):
        from app.db.cosmos_client import get_cosmos_client
        return get_cosmos_client().get_container(self.container_name)

    def list_items(self) -> List[dict]:
        if self.settings.use_in_memory_db:
            return store.list(self.container_name)

        query = "SELECT * FROM c"
        return list(self._container().query_items(query=query, enable_cross_partition_query=True))

    def get_item(self, item_id: str) -> Optional[dict]:
        if self.settings.use_in_memory_db:
            return store.get(self.container_name, item_id)

        query = "SELECT * FROM c WHERE c.id = @id"
        parameters = [{"name": "@id", "value": item_id}]
        result = list(self._container().query_items(query=query, parameters=parameters, enable_cross_partition_query=True))
        return result[0] if result else None

    def upsert_item(self, item: dict) -> dict:
        item.setdefault("partitionKey", item.get("id"))
        if self.settings.use_in_memory_db:
            return store.upsert(self.container_name, item)
        return self._container().upsert_item(item)

    def delete_item(self, item_id: str) -> bool:
        existing = self.get_item(item_id)
        if not existing:
            return False

        if self.settings.use_in_memory_db:
            return store.delete(self.container_name, item_id)

        self._container().delete_item(item=item_id, partition_key=existing.get("partitionKey", item_id))
        return True
