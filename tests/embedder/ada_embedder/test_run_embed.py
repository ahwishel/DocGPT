from service.embedder.ada_embedder.ada_embedder import AdaEmbedder
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def test_init_openai_embedder():
    embedder = AdaEmbedder()
    assert embedder.embedder is not None
