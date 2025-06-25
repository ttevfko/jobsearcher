from serpapi import GoogleSearch

# 🔑  SerpApi anahtarın
SERPAPI_KEY = "c6f8c2eac0b0d1ac6e3065450f6bbb82b9826f59fa138a22f0fd22a719df352d"

def search_jobs(keywords, location="Türkiye", max_results=5):
    """
    keywords : ["CNC", "operatörü", ...]
    location  : "Türkiye", "İstanbul" vb.
    Dönen değer: kariyer.net linklerinden oluşan liste
    """
    query = f'{" ".join(keywords)} {location} site:kariyer.net'

    params = {
        "engine":  "google",
        "api_key": SERPAPI_KEY,
        "q":       query,
        "hl":      "tr",   # arayüz dili
        "gl":      "tr"    # coğrafya
    }

    search  = GoogleSearch(params)
    results = search.get_dict()

    job_links = []
    if "organic_results" in results:
        for result in results["organic_results"][:max_results]:
            link = result.get("link")
            if link and "kariyer.net" in link:
                job_links.append(link)

    # --- DEBUG ÇIKTISI ---
    if not job_links:
        print("SerpApi TAM dönüş:", results)   # Boş gelirse burayı incele
    # ---------------------
    return job_links
