"""Foundry Local modellerini yükleyen ortak yardımcılar."""
import math

from foundry_local_sdk import Configuration, FoundryLocalManager

import config

_manager = None


def _get_manager():
    global _manager
    if _manager is None:
        FoundryLocalManager.initialize(Configuration(app_name=config.APP_NAME))
        _manager = FoundryLocalManager.instance
    return _manager


def load_model(alias):
    """Modeli (gerekirse indirip) belleğe yükler."""
    model = _get_manager().catalog.get_model(alias)
    if not model.is_cached:
        model.download(lambda p: print(f"\r{alias} indiriliyor: {p:.1f}%", end="", flush=True))
        print()
    model.load()
    return model


def normalize(vec):
    """Vektörü birim uzunluğa getirir; böylece kosinüs benzerliği = iç çarpım."""
    norm = math.sqrt(sum(x * x for x in vec))
    return [x / norm for x in vec] if norm else vec


class Embedder:
    def __init__(self):
        self.model = load_model(config.EMBED_MODEL)
        self.client = self.model.get_embedding_client()

    def embed(self, texts):
        response = self.client.generate_embeddings(texts)
        return [normalize(item.embedding) for item in response.data]
