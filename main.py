import sys
import random
import nltk
import NER
from ngrammarkov import *
sInput = " "
prn_dict={}

from tokeninput import *
from response import resfunctions
from function import *

# from nltk.corpus import stopwords

stopwords = ['what', 'why', 'when', 'how', 'a', 'is', 'an', 'the', 'are', 'was', 'were', 'am']


# static working
from gen import *

matched_keys = []
res = resfunctions()
if __name__ == '__main__':
	while 1:
		markov = True
		if markov:
			response = markovresponse()
			sentence = " ".join(response)
			print("AnswerBot>>",sentence)

		nerlist = []
		print("YOU>> ", end='')
		sInput = input().lower()
# sInput = "who is the president of america"

		inputstring = sInput
		sInput += str(' ')
# Remove stop words
# can be done with nltk->stopwords
# sInput = ' '.join([word for word in sInput.split() if word not in stopwords.words("english")])
		for word in stopwords:
			if word in sInput.split():
				sInput = sInput.replace(word, "")
# wikilist = wiki_search(sInput)


        # nerlist = getNER(wikilist)
#tokenize input words
		input_tokens = nltk.word_tokenize(inputstring)
		wikiflag = False
		wiki_tokens = ['what', 'who', 'where']
#check if input tokens contains wh question
		for tokens in input_tokens:
			if tokens in wiki_tokens:
				wikiflag = True
				break
		if wikiflag==False:
			static_search(sInput)
			continue

		input_tokens = checkprn(nltk.pos_tag(input_tokens))
		sInput = ' '.join(input_tokens)

        #sInput = ' '.join(input_tokens)
		# print("After replacing PRN:", input_tokens)
#wiki search true
		if wikiflag:
			#con contains all the contents from wiki search
			con = wiki_search(sInput)
			# file = open('paragraph.txt', 'r')
			# fread = file.read()
			#sentences = nltk.sent_tokenize(fread)
#get ner list
			sentences = nltk.sent_tokenize(con)	
			nerlist = NER.getNER(sentences)
			# print(nerlist)
			tagged_input = nltk.pos_tag(input_tokens)
			get_input_nouns = getnouns(tagged_input)
			start_output = " ".join(input_tokens[2:])
			verbused = input_tokens[1]
#for who  questions
			if 'who' in input_tokens:
				person = NER.getpersonlist(nerlist)
				# print(person)
				if len(person) == 1:
					print(start_output,verbused, ''.join(person))
				else:
					#reqper = NER.gethighcountner(get_input_nouns, person,con)
					reqper=NER.getcorrect(get_input_nouns, person,con)
					prn_dict['he'] = reqper[0]
					prn_dict['she'] = reqper[0]
					print(start_output,verbused,"".join(reqper))
					# print("here is the dictionary")
					# print(prn_dict)
			elif 'where' in input_tokens:
				place = NER.getplacelist(nerlist)
				verbused = input_tokens[1]

				# print(place)
				if len(place) ==1:
					print(start_output,"at","".join(place))
				else:
					reqplace = NER.gethighcountner(get_input_nouns,place,con)
					print(start_output,verbused,"at",reqplace)



				


