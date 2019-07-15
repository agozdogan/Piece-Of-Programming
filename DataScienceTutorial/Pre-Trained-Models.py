from pprint import pprint
from nltk import word_tokenize,pos_tag,ne_chunk

sentence = "Mark is working at the South Africa offices at Google"
ne_tree = ne_chunk(pos_tag(word_tokenize(sentence)))
print(ne_tree)