name = "олена"
name.capitalize()
print(name)
name = name.capitalize()
print(name)

text = "    hello  "
text.strip()
text = text.strip()
print(text)

full = "taras shevchenko"
first, last = full.split()
result = last.title() + " " + first[0].upper() + "."
print(result)

phrase = "Козак з казок"
clean = phrase.replace(" ", "").lower()
print(clean == clean[::-1])

email = "ivan.petrenko@gmail.com"

# ↓↓↓ ТВІЙ КОД НИЖЧЕ ↓↓↓
parts = email.split("@")
print(parts)

print("ZADACHA EZHEDNEVNA")
