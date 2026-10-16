import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Download required packages (run once)
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt')

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Sample Input
text = "The children are running and flies were studying better"

# Tokenize
words = word_tokenize(text)
print("Original Words:", words)

print("\nLemmatized Words:")
for word in words:
    # pos='v' for verb, 'n' for noun, 'a' for adjective
    lemma = lemmatizer.lemmatize(word.lower(), pos='v')
    print(f"{word} -> {lemma}")

# Direct list example
print("\n--- Direct Word List ---")
sample_words = ["running", "flies", "studies", "better", "children", "went"]
for w in sample_words:
    print(f"{w} -> {lemmatizer.lemmatize(w, pos='n')} (noun), {lemmatizer.lemmatize(w, pos='v')} (verb)")
