# Coauthor Gender Analysis 

This project analyzes the gender distribution of coauthors for a given researcher using publication data from the OpenAlex API. It uses name-based inference powered by the `gender-guesser` library to estimate whether each coauthor is male, female, or unknown.

The final output is a CSV file listing each coauthor’s name, number of publications, and inferred gender, as well as a printed summary of total estimated male and female coauthors (weighted by co-authorship count).

---

## Purpose

The project was designed to explore gender representation trends among coauthors in medical and academic publications. By analyzing coauthor data from before and after 2015, we aim to understand how collaborative networks may reflect broader diversity patterns.

---

## Features

- Fetches coauthor data from [OpenAlex](https://openalex.org/) using their public API
- Counts the number of publications shared with each coauthor
- Applies gender inference using the first name of each coauthor
- Outputs:
  - `coauthors_with_counts.csv` — raw coauthor names + counts
  - `authors_with_gender.csv` — cleaned data with gender labels
- Provides weighted totals of male and female coauthors

---

## Technologies Used

- Python
- `requests` – API calls
- `csv` – file I/O
- `gender-guesser` – name-based gender classification
- `collections.Counter` – frequency counting
- `re` – basic name pattern filtering

---

## How It Works

1. **Fetch Coauthors**  
   Pulls works authored by a target author from OpenAlex (before 2015), extracts coauthors, filters out initials-only names, and counts occurrences.

2. **Infer Gender**  
   Uses the `gender-guesser` library to infer the gender of each coauthor using their first name.

3. **Save Results**  
   Two CSV files are created:
   - `coauthors_with_counts.csv`
   - `authors_with_gender.csv` (includes gender labels)

4. **Output Totals**  
   Prints the total weighted number of male and female coauthors to the console.

---

## Files

| File | Description |
|------|-------------|
| `coauthor_gender_analysis.py` | Main script for fetching, counting, and classifying coauthors |
| `coauthors_with_counts.csv` | Generated intermediate file with coauthor names and counts |
| `authors_with_gender.csv` | Final output with coauthor gender labels and counts |

