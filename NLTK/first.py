corpus = """Hello how are you, I am Aneesh Ahuja. You are are? I am fine and what about you? I am good."""
#TOKENIZE
#Sentence -> paragraphs
from nltk.tokenize import sent_tokenize
import nltk
nltk.download('punkt')
print(sent_tokenize(corpus))