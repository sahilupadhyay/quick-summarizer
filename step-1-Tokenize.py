import nltk
from nltk.stem.porter import *


hash_table = {}
def	feature_1(sentence_index):	# Relative position of sentence
	hash_table[0] = 1
	hash_table[para_lenght-1] = 1

def feature_2():	

def uniq(input):
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  return output

tokenize_file = open("text.txt", "r+")
paragraph = tokenize_file.read()

# Find out current index(s) of paragraph
fetch_sentences = nltk.sent_tokenize(paragraph)
sentence_index = {}
for x in range(0, len(fetch_sentences)):
	sentence_index[x] = fetch_sentences[x]

para_lenght=len(fetch_sentences)
print "\nsentence_index : ", sentence_index

# Tokenize the paragraph
tokens = nltk.word_tokenize(paragraph)
print "\nTokens: ", tokens

#Stemming the words
stemmer = PorterStemmer()
stemmed_content = [ stemmer.stem(token) for token in tokens ]

print "\nstemmed_content:", stemmed_content

stemmed_content_file = open("stemmed-content.txt", "wb")
stemmed_content_file.writelines(["%s\n" % item  for item in stemmed_content])


uniqe_keywords = uniq(stemmed_content)

print "\nuniqe_keywords:", uniqe_keywords

feature_1(fetch_sentences)
print hash_table[0]
print hash_table[para_lenght-1]

tokenize_file.close()
stemmed_content_file.close()