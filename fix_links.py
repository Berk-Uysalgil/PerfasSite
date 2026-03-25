import os
import glob

public_dir = r"c:\Users\user\OneDrive\Masaüstü\perfassite\public"
html_files = glob.glob(os.path.join(public_dir, "*.html"))

replacements = {
    'href="/"': 'href="index.html"',
    'href="/hakkimizda"': 'href="hakkimizda.html"',
    'href="/iletisim"': 'href="iletisim.html"',
    'href="/cozumler"': 'href="cozumler.html"',
    'href="/guvenlik-kvkk"': 'href="guvenlik-kvkk.html"',
    'href="/kullanim-senaryolari"': 'href="kullanim-senaryolari.html"',
    'href="/nasil-calisir"': 'href="nasil-calisir.html"',
    'href="/ozellikler"': 'href="ozellikler.html"',
    'href="/sss"': 'href="sss.html"'
}

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for old_text, new_text in replacements.items():
        content = content.replace(old_text, new_text)
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Processed {len(html_files)} HTML files.")
