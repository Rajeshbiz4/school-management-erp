from azure.cosmos import CosmosClient, PartitionKey

from app.core.config import get_settings


class CosmosDbClient:
    def __init__(self) -> None:
        settings = get_settings()
        if not settings.cosmos_endpoint or not settings.cosmos_key:
            raise RuntimeError("Cosmos DB endpoint/key missing. Check .env file.")

        self.client = CosmosClient(settings.cosmos_endpoint, credential=settings.cosmos_key)
        self.database = self.client.create_database_if_not_exists(settings.cosmos_database_name)

    def get_container(self, container_name: str):
        return self.database.create_container_if_not_exists(
            id=container_name,
            partition_key=PartitionKey(path="/partitionKey"),
            offer_throughput=400,
        )


_cosmos_client: CosmosDbClient | None = None


def get_cosmos_client() -> CosmosDbClient:
    global _cosmos_client
    if _cosmos_client is None:
        _cosmos_client = CosmosDbClient()
    return _cosmos_client
