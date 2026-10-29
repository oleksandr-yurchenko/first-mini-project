raw = "   пЕТРО   іВАНОВИЧ    шевченко  "
# треба: "Петро Іванович Шевченко"

clean = raw.title()
clean = clean.strip()
clean = clean.split()
clean = " ".join(clean)
print(clean)