# -*- coding: utf-8 -*-

from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers

# import spacy

# print("loading spacy")
# nlp = spacy.load('en_core_web_lg')

# file = open("/Users/skylerilenstine/Library/Mobile Documents/com~apple~TextEdit/Documents/Wizard_of_OZ.rtf")

# my_file_contents = file.read()

# doc = nlp(my_file_contents)

# sents = list(doc.sents)

#print('Downloading text...')
#text = strip_headers(load_etext(14040)).strip()

#print('Analyzing text...')
#doc = nlp(text)

#sents = list(doc.sents)
#my_sent = nlp('My friend is always telling me that nothing I say is real. How do I convince him that nothing at ALL is real?!')
# my_sent = nlp('He told himself that he was glad she was away and he did not care to have her return.')

# print('Finding best match...')
#best_match = None
# best_similarity = 0
# for sent in sents:
#   similarity = sent.similarity(my_sent)
#   if similarity > best_similarity:
#     best_similarity = similarity
#     best_match = sent

# def get_reply(question):
#   question = nlp(question)
#   similarities = [
#     (sent.similarity(question), sent)
#     for sent in sents
#   ]
#   similarities = sorted(similarities, reverse=True)
#   return similarities[0]

# while True:
#   next_question = input("> ")
#   next_reply = get_reply(next_question)
#   print(str(next_reply[1]).replace('\n', ' '))
#   print(next_reply[0])
#   print()

# print(my_sent)

# for i in range(10):
#   similarity, match = similarities[i]
#   print()
#   print(similarity)
#   print(match)
#   print()
