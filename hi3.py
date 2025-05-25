import csv
import gender_guesser.detector as gender

# Initialize gender detector
d = gender.Detector()

# Counters
male_total = 0
female_total = 0

# Open original CSV and new CSV for writing
with open('coauthors_with_counts.csv', newline='', encoding='utf-8') as infile, \
        open('authors_with_gender.csv', 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Write header for new file
    writer.writerow(['Name', 'Count', 'Gender'])

    for row in reader:
        if len(row) < 2:
            continue
        name = row[0].strip()
        first_name = name.split()[0]
        try:
            count = int(row[1])
        except ValueError:
            continue

        gender_guess = d.get_gender(first_name)

        if gender_guess in ['male', 'mostly_male']:
            gender_label = 'male'
            male_total += count
        elif gender_guess in ['female', 'mostly_female']:
            gender_label = 'female'
            female_total += count
        else:
            gender_label = 'unknown'

        writer.writerow([name, count, gender_label])

# Print totals
print(f"Estimated Male Authors (weighted): {male_total}")
print(f"Estimated Female Authors (weighted): {female_total}")
