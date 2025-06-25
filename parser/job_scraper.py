from serpapi import GoogleSearch

SERPAPI_KEY = "c6f8c2eac0b0d1ac6e3065450f6bbb82b9826f59fa138a22f0fd22a719df352d"

def search_jobs(keywords, location, max_results=5):
    query = f"{' '.join(keywords)} {location} site:kariyer.net"

    search = GoogleSearch({
        "q": query,
        "api_key": SERPAPI_KEY,
        "hl": "tr"
    })

    results = search.get_dict()
    job_links = []

    if "organic_results" in results:
        for result in results["organic_results"][:max_results]:
            link = result.get("link")
            if link:
                job_links.append(link)

    return job_links
