import requests
from bs4 import BeautifulSoup
import csv
import sys
import time

def scraper(url, output="emails.csv"):
    """Extrae emails de una página web y los guarda en CSV."""
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"Error bajando la página: {e}")
        return

    soup = BeautifulSoup(resp.text, "html.parser")
    emails = set()

    # Busca en mailto:
    for link in soup.find_all("a", href=True):
        if link["href"].startswith("mailto:"):
            emails.add(link["href"][7:].strip())

    # Busca en texto plano (patrón básico)
    import re
    texto = soup.get_text()
    emails.update(re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", texto))

    with open(output, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["email"])
        writer.writerows(sorted(emails))

    print(f"Se encontraron {len(emails)} emails → {output}")

if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else "https://ejemplo.com"
    scraper(url)   