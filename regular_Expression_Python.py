import re

# Matching a literal string
pattern = r"hello"
text = "Say hello to everyone!"
match = re.search(pattern, text)
print(match.group())  # Output: hello

# Matching a character class
pattern = r"[aeiou]"
text = "Hello, World!"
matches = re.findall(pattern, text)
print(matches)  # Output: ['e', 'o', 'o']

# Using quantifiers
pattern = r"ab*c"
texts = ["ac", "abc", "abbc", "abbbbc"]
for text in texts:
    match = re.match(pattern, text)
    if match:
        print(f"Matched: {match.group()}")
    else:
        print("No match")

# Anchors
pattern = r"^Hello"
text = "Hello, World!"
match = re.match(pattern, text)
if match:
    print("Matched:")
else:
    print("No match")

# Escape sequences
pattern = r"\."
text = "www.example.com"
match = re.search(pattern, text)
print(match.group())  # Output: .
