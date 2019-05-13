# import nltk
# from nltk.corpus import state_union
# from nltk.tokenize import PunktSentenceTokenizer
# t_t=state_union.raw("2005-GWBush.txt")
# s_t=state_union.raw("2006-GWBush.txt")
# custom=PunktSentenceTokenizer(t_t)
# tokenized=custom.tokenize(s_t)
# def process_content():
#      try:
#              for i in tokenized:
#                      words=nltk.word_tokenize(i)
#                      tagged=nltk.pos_tag(words)
#                      # chunkGram=r"""chunk: {<RB.?>*<VB.?>*<NNP><NN>?} """
#                      # chunkParser=nltk.RegexpParser(chunkGram)
#                      # chunked=chunkParser.parse(tagged)
#                      # chunked.draw()
#                      namedEnt=nltk.ne_chunk(tagged,binary=True)
#                      namedEnt.draw()
#      except Exception as e:
#              print(str(e))

# process_content()
# from nltk.stem import WordNetLemmatizer
# l=WordNetLemmatizer()
# print(l.lemmatize("went"))
# from nltk import word_tokenize, pos_tag
 
# print (pos_tag(word_tokenize("Photosynthesis is the process used by plants, algae and certain bacteria to harness energy from sunlight and turn it into chemical energy.")))
# [('I', 'PRP'), ("'m", 'VBP'), ('learning', 'VBG'), ('NLP', 'NNP')]

