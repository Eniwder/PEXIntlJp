# PraciceEXIntlで使われる日本語用データ

## 文字がうまく表示されない場合は同梱の軽量版をお試しください

自分用メモ：

```python -m venv venv
./venv/Scripts/activate
pip install -r requirements.txt
python ./extractchar.py
```

```pyftsubset ./font/NotoSerifJP-Medium_150.ttf --text-file=subset_chars.txt --output-file=PEXIntlJp/Title.ttf
pyftsubset ./font/NotoSerifJP-Medium_150.ttf --text=ABCDE --output-file=PEXIntlJp/Title.ttf
```
