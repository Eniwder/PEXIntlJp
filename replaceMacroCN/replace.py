def replace_multiple_pngs_in_dll(dll_path, replacements, output_path):
    with open(dll_path, 'rb') as f:
        dll_data = f.read()

    for original_png_path, new_png_path in replacements:
        with open(original_png_path, 'rb') as f:
            original_png = f.read()
        with open(new_png_path, 'rb') as f:
            new_png = f.read()

        index = dll_data.find(original_png)
        if index == -1:
            print(f"⚠️ PNG未発見: {original_png_path}")
            continue

        if len(new_png) > len(original_png):
            print(f"❌ サイズ超過: {new_png_path} は大きすぎます。スキップします。")
            continue
        elif len(new_png) < len(original_png):
            padding_length = len(original_png) - len(new_png)
            new_png += b'\x00' * padding_length
            print(f"🔧 パディング追加: {new_png_path} に {padding_length} バイト追加")

        dll_data = (
            dll_data[:index] +
            new_png +
            dll_data[index + len(original_png):]
        )
        print(f"✅ 置換完了: {original_png_path} → {new_png_path}")

    with open(output_path, 'wb') as f:
        f.write(dll_data)
    print(f"\n💾 出力完了: {output_path}")

# 使用例: 置換リストを指定
replace_multiple_pngs_in_dll(
    dll_path="replaceMacroCN/PracticeEx-original.dll",
    replacements=[
        ("replaceMacroCN/copy.png", "replaceMacroCN/copy2.png"),
        ("replaceMacroCN/paste.png", "replaceMacroCN/paste2.png"),
        ("replaceMacroCN/opt.png", "replaceMacroCN/opt2.png"),
        ("replaceMacroCN/del.png", "replaceMacroCN/del2.png"),
    ],
    output_path="replaceMacroCN/PracticeEx-patched.dll"
)