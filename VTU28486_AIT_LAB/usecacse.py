# Simple Lemmatization without NLTK - 100% works anywhere

def simple_lemmatizer(word):
    # Simple rule-based lemmatization
    word = word.lower()
    rules = {
        'running': 'run',
        'flies': 'fly',
        'studies': 'study',
        'studying': 'study',
        'better': 'good',
        'children': 'child',
        'went': 'go',
        'are': 'be',
        'were': 'be',
        'is': 'be'
    }
    if word in rules:
        return rules[word]
    # General suffix rules
    if word.endswith('ies'):
        return word[:-3] + 'y'
    if word.endswith('ing'):
        return word[:-3]
    if word.endswith('es'):
        return word[:-2]
    if word.endswith('s'):
        return word[:-1]
    return word

text = "The children are running and flies were studying better"
words = text.split()

print("Original:", words)
print("\nLemmatized:")
for w in words:
    print(f"{w} -> {simple_lemmatizer(w)}")
