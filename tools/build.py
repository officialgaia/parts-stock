"""src/app.html（claude.ai 版と同じ本文）を GitHub Pages 用の index.html に包む。"""
from pathlib import Path

root = Path(__file__).resolve().parent.parent
body = (root / "src" / "app.html").read_text(encoding="utf-8")
head = (
    '<!doctype html><html lang="ja"><head><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
    "<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);"
    "padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0;font:14px/1.5 system-ui,sans-serif}"
    "img{max-width:100%}[hidden]{display:none!important}</style></head><body>\n"
)
(root / "index.html").write_text(head + body + "\n</body></html>\n", encoding="utf-8")
print("index.html を更新しました")
