# 🎬 IMDb Top 1000 Film Öneri Sistemi

Bu projede, kullanıcının girdiği bir film OMDb API üzerinden sorgulanarak IMDb Top 1000 listesiyle karşılaştırılır.
Tür, IMDb puanı ve oy sayısı bilgileri kullanılarak cosine similarity ile benzerlik hesabı yapılır ve tematik olarak en yakın 5 film önerilir.


**Özellikler**
- **Tür bazlı öneri:** Film türlerine ağırlık verilerek temaya yakın öneriler sunar.
- **OMDb API entegrasyonu:** Kullanıcının girdiği film verisi API kullanılarak web sitesinden alınır.
- **Ağırlıklı cosine similarity:** Tür bilgisi %70, IMDb puanı ve oy sayısı %30 etkilidir.
- **Masaüstü uyumlu:** Kod `.exe` dosyası ile çalıştırılabilir.

.exe link: https://drive.google.com/drive/folders/1JR2ag73A46Xm3nAEsH5eYb8kiY3yy4aZ?usp=drive_link


**Kullanılanlar**

- Python
- Pandas, Numpy
- Scikit-learn
- OMDb API
- PyInstaller


**Örnek Çıktı**

Film Adını Giriniz: you

🎬 Film Bilgisi
----------------------------
🎞️ Film Adı     : You
🎭 Türü         : Suç, Dram, Romantik
⭐ IMDb Puanı   : 7.7
👥 Oy Sayısı    : 324857

🎯 'You' filmine en çok benzeyen 5 öneri:
1. True Romance - IMDb: 7.9, Oy: 252218
2. Slumdog Millionaire - IMDb: 8.0, Oy: 894851
3. 3-Iron - IMDb: 7.9, Oy: 59910
4. A Brighter Summer Day - IMDb: 8.2, Oy: 13968
5. Marriage Story - IMDb: 7.9, Oy: 360468
------------------------------------------------


.exe link: https://drive.google.com/drive/folders/1JR2ag73A46Xm3nAEsH5eYb8kiY3yy4aZ?usp=drive_link
