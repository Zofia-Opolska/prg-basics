import csv

# Load province data from CSV
province_file = 'province.csv'
province_map = {}  # Maps first letter to province name

with open(province_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        letter = row['Letter'].strip()
        name = row['Name'].strip()
        province_map[letter] = name

# Initialize a counter dictionary for provinces
province_counts = {name: 0 for name in province_map.values()}

# Read vehicle registration numbers
vehicle_file = 'vehicle.txt'
with open(vehicle_file, 'r', encoding='utf-8') as f:
    for line in f:
        reg_number = line.strip()
        if reg_number:  # skip empty lines
            first_letter = reg_number[0].upper()
            if first_letter in province_map:
                province_name = province_map[first_letter]
                province_counts[province_name] += 1
            else:
                print(f"Unknown province code: {first_letter}")

# Print results
for province, count in sorted(province_counts.items()):
    print(f"{province}: {count}")
