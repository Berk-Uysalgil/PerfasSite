import os
import glob

public_dir = r"c:\Users\user\OneDrive\Masaüstü\perfassite\public"
html_files = glob.glob(os.path.join(public_dir, "*.html"))

replacements = {
    'href="index.html"': 'href="/"',
    'href="hakkimizda.html"': 'href="/hakkimizda"',
    'href="iletisim.html"': 'href="/iletisim"',
    'href="cozumler.html"': 'href="/cozumler"',
    'href="guvenlik-kvkk.html"': 'href="/guvenlik-kvkk"',
    'href="kullanim-senaryolari.html"': 'href="/kullanim-senaryolari"',
    'href="nasil-calisir.html"': 'href="/nasil-calisir"',
    'href="ozellikler.html"': 'href="/ozellikler"',
    'href="sss.html"': 'href="/sss"'
}

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for old_text, new_text in replacements.items():
        content = content.replace(old_text, new_text)
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Reverted {len(html_files)} HTML files to clean URLs.")
