"""Proje ayarları."""

APP_NAME = "docker_rag"

# Foundry Local model takma adları
CHAT_MODEL = "qwen3.5-4b"          # alternatif: "qwen2.5-7b"
EMBED_MODEL = "qwen3-embedding-0.6b"

# Cevap üretimi
TEMPERATURE = 0.2
MAX_TOKENS = 400          # cevap uzunluğu sınırı
THINKING_TOKENS = 1300    # reasoning modellerde cevaptan önceki düşünme metni için ek pay

# Arama
TOP_K = 3
MIN_SCORE = 0.65          # en iyi parçanın benzerliği bunun altındaysa model çağrılmaz (0 = kapalı)
# Qwen3-Embedding, sorguların (dokümanların değil) başına görev talimatı eklenmesini bekler
QUERY_INSTRUCTION = ("Instruct: Given a question about Docker, "
                     "retrieve documentation passages that answer it\nQuery: ")

# Aramadan önce Türkçe soruyu İngilizceye çevir.
# Varsayılan olarak kapalı: ölçülebilir fayda sağlamadı, reasoning modellerle çok yavaş.
TRANSLATE_QUERY = False

# Yollar
DOCS_DIR = "docs"
DB_PATH = "rag.db"

# Dokümanlarda cevap yoksa asistanın döndürdüğü cümle
NO_ANSWER = "Bu konuda dokümanlarda bilgi bulamadım."
