import requests
from collections import Counter
import csv
import re

author_id = "3Aa5006262715"
target_name = "Mitchel Berger"
coauthors = Counter()
page = 1

while True:
    url = (
        f"https://api.openalex.org/works?"
        f"filter=author.id:{author_id},to_publication_date:2015-01-01"
        f"&per-page=200&page={page}"
    )
    res = requests.get(url).json()
    results = res.get("results", [])

    if not results:
        break

    for work in results:
        for author in work["authorships"]:
            name = author["author"]["display_name"]
            if not name or name.lower() == target_name.lower():
                continue

            first_name = name.split()[0]
            # Skip if first name is a single letter or letter with a dot (e.g., "J" or "J.")
            if re.fullmatch(r"[A-Za-z]\.?", first_name):
                continue

            coauthors[name] += 1

    page += 1

# Save to CSV
with open("coauthors_with_counts.csv", "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Co-author", "Count"])  # header
    for name, count in coauthors.most_common():
        writer.writerow([name, count])

print(f"CSV file 'coauthors_with_counts.csv' created with {len(coauthors)} unique co-authors from 2015 and earlier.")
