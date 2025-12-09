# FastAPI Notes API

**📖 概要**  
FastAPI と Python で構築した、メモ管理用のシンプル CRUD API。  
個人の学習およびポートフォリオ提出用に作成。

---

## ✅ 機能一覧（Features）

| メソッド | エンドポイント | 動作概要     |
| -------- | -------------- | ------------ |
| GET      | `/notes`       | メモ一覧取得 |
| POST     | `/notes`       | メモ作成     |
| GET      | `/notes/{id}`  | 特定メモ取得 |
| PUT      | `/notes/{id}`  | メモ更新     |
| DELETE   | `/notes/{id}`  | メモ削除     |

Swagger UI によるドキュメント生成対応。  
→ 起動後 `http://localhost:8000/docs` で確認可能。

---

## 🛠 技術スタック (Tech Stack)

-   Python 3.x
-   :contentReference[oaicite:0]{index=0}
-   :contentReference[oaicite:1]{index=1}
-   データストア: メモリ上のリストによる簡易実装
-   （今後の拡張例：SQLite／Docker／認証機能など）

---

## 🚀 ローカルでの動作方法

```bash
git clone https://github.com/ishida-gh-dev/fastapi-notes.git
cd fastapi-notes
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

-   ブラウザで以下へアクセス → Swagger UI が立ち上がる - http://localhost:8000/docs - 画面イメージ
    <img width="1854" height="2377" alt="image" src="https://github.com/user-attachments/assets/ac33303a-a6c1-4c77-ad45-d56318def1de" />

## 📄 コード構成 (Project Structure)

```
fastapi-notes/
├─ app/
│   ├─ main.py
│   ├─ schemas.py
│   └─ routers/
│       └─ notes.py
├─ requirements.txt
├─ README.md
└─ .gitignore
```

## ⚠️ 注意点 / 補足 (Caveats & Notes)

-   現状、データはメモリ上で保持。サーバ再起動で消える仕様。
-   デプロイ設定・DB 永続化・認証機能などは未実装。
