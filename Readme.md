PraciceEXIntlで使われる日本語用データ

メモ：
```
python -m venv venv
./venv/Scripts/activate
pip install -r requirements.txt
```

```
pyftsubset ./font/NotoSerifJP-Medium_150.ttf --text-file=subset_chars.txt --output-file=PEXIntlJp/Title.ttf
pyftsubset ./font/NotoSerifJP-Medium_150.ttf --text-file=subset_chars.txt --output-file=PEXIntlJp/Macro.ttf
pyftsubset ./font/NotoSansJP-SemiBold_200.ttf --text-file=subset_chars.txt --output-file=PEXIntlJp/OptionsLeft.ttf
pyftsubset ./font/NotoSansJP-SemiBold_165y50.ttf --text-file=subset_chars.txt --output-file=PEXIntlJp/OptionsRight.ttf
pyftsubset ./font/NotoSansJP-SemiBold_125.ttf --text-file=subset_chars.txt --output-file=PEXIntlJp/Trigger.ttf
```
