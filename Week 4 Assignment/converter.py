month_names = ["Baisakh", "Jestha", "Ashadh", "Shrawan", "Bhadra", "Ashwin",
               "Kartik", "Mangsir", "Poush", "Magh", "Falgun", "Chaitra"]

records = [
    {"name": "Ramesh Thapa", "date": "1985-06-24", "cal": "AD", "need": "BS", "style": "full"},
    {"name": "Sunita Karki", "date": "2055-09-10", "cal": "BS", "need": "AD", "style": "iso"},
    {"name": "Bikash Rai", "date": "1998-11-30", "cal": "AD", "need": "BS", "style": "nepali"},
    {"name": "Anjali Gurung", "date": "2040-01-05", "cal": "BS", "need": "AD", "style": "full"},
]
def convert_date(date_str, from_cal, to_cal):
    yy, mm, dd = date_str.split("-")
    yy = int(yy)

    if from_cal == to_cal:
        return date_str
    elif from_cal == "AD" and to_cal == "BS":
        yy += 56
    elif from_cal == "BS" and to_cal == "AD":
        yy -= 56
    else:
        return "invalid"

    return f"{yy}-{mm}-{dd}"
for entry in records:
    output = convert_date(entry["date"], entry["cal"], entry["need"])
    yy, mm, dd = output.split("-")

    if entry["style"] == "iso":
        print(
            f"{entry['name']} | Original: {entry['date']} {entry['cal']} | Converted: {output} {entry['need']}"
        )

    elif entry["style"] == "full":
        print(
            f"{entry['name']} | Original: {entry['date']} {entry['cal']} | Converted: {dd}-{mm}-{yy} {entry['need']}"
        )

    elif entry["style"] == "nepali":
        month_label = month_names[int(mm) - 1]
        print(
            f"{entry['name']} | Original: {entry['date']} {entry['cal']} | Converted: {dd} {month_label}, {yy} {entry['need']}"
        )