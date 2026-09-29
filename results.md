# Değerlendirme sonuçları: `qwen3.5-4b`

- Embedding: `qwen3-embedding-0.6b`, TOP_K = 3, MIN_SCORE = 0.65, sıcaklık = 0.2
- Soru sayısı: 10 (7 cevaplı, 3 tuzak)
- Toplam çalışma süresi: 7.0 dk

## Özet

| Ölçüm | Çeviri kapalı |
|---|---|
| Doğru kaynak getirildi (cevaplı sorular) | 7/7 (%100) |
| Beklenen komut cevapta var | 5/6 (%83) |
| Tuzak: ret cümlesi birebir | 3/3 (%100) |
| Tuzak: ret cümlesi geçiyor (gevşek) | 3/3 (%100) |
| Cevaplı soruda yanlışlıkla ret | 0/7 (%0) |
| Cevapta Çince/CJK karakter | 0/10 (%0) |
| Ortalama cevap süresi | 42.1 sn |
| Ortalama ilk token süresi | 36.5 sn |

## Soru bazında

Sütunlarda K: çeviri kapalı. Kaynak = beklenen dosya ilk TOP_K parça içinde mi; Komut = beklenen komut cevapta mı; Ret = ret cümlesi geçiyor mu (tuzakta ✅, cevaplı soruda ❌ iyidir); Skor = en iyi parçanın benzerliği.

| # | Tür | Soru | Kaynak (K) | Komut (K) | Ret (K) | Skor (K) | Süre sn (K) |
|---|---|---|---|---|---|---|---|
| 1 | cevaplı | Bir volume nasıl oluştururum? | ✅ | ✅ | ❌ | 0.85 | 31.4 |
| 2 | cevaplı | Container'ın 80 portunu host'taki 8080 portuna nasıl yayınlarım? | ✅ | ❌ | ❌ | 0.77 | 177.0 |
| 3 | cevaplı | Bir container'ın loglarını canlı olarak nasıl takip ederim? | ✅ | ✅ | ❌ | 0.81 | 27.1 |
| 4 | cevaplı | Dockerfile'dan bir image build edip ona nasıl etiket (tag) veririm? | ✅ | ✅ | ❌ | 0.79 | 50.6 |
| 5 | cevaplı | Bind mount ile volume arasındaki fark nedir? | ✅ | - | ❌ | 0.81 | 50.1 |
| 6 | cevaplı | Kullanıcı tanımlı bir bridge network nasıl oluştururum? | ✅ | ✅ | ❌ | 0.84 | 35.9 |
| 7 | cevaplı | Docker Compose ile tanımlı uygulamayı nasıl başlatırım? | ✅ | ✅ | ❌ | 0.81 | 46.8 |
| 8 | tuzak | Docker Swarm'da bir servisi nasıl ölçeklendiririm? | - | - | ✅ | 0.62 | 0.6 |
| 9 | tuzak | Kubernetes'te bir pod nasıl oluşturulur? | - | - | ✅ | 0.52 | 0.6 |
| 10 | tuzak | Podman ile Docker arasındaki farklar nelerdir? | - | - | ✅ | 0.60 | 0.6 |
