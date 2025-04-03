import os
import re
import subprocess
import string

def extract_text_from_csv_files(folder_path):
    extracted_chars = set(string.printable)  # ASCII文字を追加
    
    # フォルダ内の全ファイルを走査
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".csv"):  # CSVファイルのみ対象
            file_path = os.path.join(folder_path, file_name)
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                    # 各文字をセットに追加（重複を排除）
                    extracted_chars.update(re.findall(r'.', content))
            except Exception as e:
                print(f"Error reading {file_name}: {e}")
    
    return "".join(sorted(extracted_chars))

# 使用例
folder_path = "PEXIntlJp"
text_data = extract_text_from_csv_files(folder_path)

# 結果を表示
print(text_data)

def run_pyftsubset(font, source, output_file):
    if source.endswith(".txt"):
        text_option = f"--text-file={source}"
    else:
        text_option = f"--text={source}"
    command = [
        "pyftsubset", font,
        text_option,
        f"--output-file={output_file}"
    ]
    try:
        subprocess.run(command, check=True)
        print("Font subset generated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running pyftsubset: {e}")

run_pyftsubset("./font/NotoSerifJP-Medium_150.ttf", "subset_chars.txt", "PEXIntlJp/Title.ttf")
run_pyftsubset("./font/NotoSerifJP-Medium_150.ttf", "subset_chars.txt", "PEXIntlJp/Macro.ttf")
run_pyftsubset("./font/NotoSansJP-SemiBold_200.ttf", "subset_chars.txt", "PEXIntlJp/OptionsLeft.ttf")
run_pyftsubset("./font/NotoSansJP-SemiBold_165y64.ttf", "subset_chars.txt", "PEXIntlJp/OptionsRight.ttf")
run_pyftsubset("./font/NotoSansJP-SemiBold_125.ttf", "subset_chars.txt", "PEXIntlJp/Trigger.ttf")

run_pyftsubset("./font/NotoSerifJP-Medium_150.ttf", text_data, "PEXIntlJp/軽量版/Title.ttf")
run_pyftsubset("./font/NotoSerifJP-Medium_150.ttf", text_data, "PEXIntlJp/軽量版/Macro.ttf")
run_pyftsubset("./font/NotoSansJP-SemiBold_200.ttf", text_data, "PEXIntlJp/軽量版/OptionsLeft.ttf")
run_pyftsubset("./font/NotoSansJP-SemiBold_165y64.ttf", text_data, "PEXIntlJp/軽量版/OptionsRight.ttf")
run_pyftsubset("./font/NotoSansJP-SemiBold_125.ttf", text_data, "PEXIntlJp/軽量版/Trigger.ttf")

