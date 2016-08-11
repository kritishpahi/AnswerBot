import sys
import random
import nltk
sInput = " "
import NER


from tokeninput import *
from wikisearch import *
from scraping import *
from response import resfunctions

import generator

#static working
from gen import *
matched_keys = []
res = resfunctions()

if __name__ == '__main__':
	# while 1:
		print("> ", end = '')
		# sInput = input()
		# sInput += str(' ')


#search in the static keywords list
		# search = generator.SelectResponse(sInput)
		# response_list = search.top_ten_resp()
		# print(response_list)


#currently select the 1st keywords
		# best = response_list[0][0]
		# print("Selected key word: ", best)
#Resonse of the 1st matched keywords
		# best_resp = generator.give_resp(best)
		# print(best_resp)



		# alltokens = tokenization(sInput)
		# print(alltokens)
		# nouns = grouping(alltokens)
		# print(nouns)

		# tokens = res.word_tokenize(sInput)
		# nostop_words = res.remove_stopwords(tokens)
#get the wiki link for corresponding nouns
		# link = getlink(nostop_words)
		# content = regetdes(link)
		# print(content)
		# del sInput
		# del search
		# del response_list
		# del best_resp
		# r = search.top_ten_resp()
		# print(response_list)
nerlist=[]
wiki = [['The President of the United States of America (POTUS)[7] is the elected head of state and head of government of the United States.', 'The president leads the executive branch of the federal government and is the commander-in-chief of the United States Armed Forces.'], ["The President of the United States is considered one of the world's most powerful people, leading the world's only contemporary superpower.", "[8][9][10][11] The role includes being the commander-in-chief of the world's most expensive military with the largest nuclear arsenal and leading the nation with the largest economy by real and nominal GDP.", 'The office of the president holds significant hard and soft power both in the United States and abroad.'], ['Article II of the U.S. Constitution vests the executive power of the United States in the president.', 'The power includes execution of federal law, alongside the responsibility of appointing federal executive, diplomatic, regulatory and judicial officers, and concluding treaties with foreign powers with the advice and consent of the Senate.', 'The president is further empowered to grant federal pardons and reprieves, and to convene and adjourn either or both houses of Congress under extraordinary circumstances.', '[12] The president is largely responsible for dictating the legislative agenda of the party to which the president is enrolled.', 'The president also directs the foreign and domestic policy of the United States.', '[13] Since the founding of the United States, the power of the president and the federal government has grown substantially.', '[14]'], ['The president is indirectly elected by the people through the Electoral College to a four-year term, and is one of only two nationally elected federal officers, the other being the Vice President of the United States.', '[15] The Twenty-second Amendment, adopted in 1951, prohibits anyone from ever being elected to the presidency for a third full term.', "It also prohibits a person from being elected to the presidency more than once if that person previously had served as president, or acting president, for more than two years of another person's term as president.", "In all, 43 individuals have served 44 presidencies (counting Cleveland's two non-consecutive terms separately) spanning 56 full four-year terms.", '[16] On January 20, 2009, Barack Obama became the 44th and current president.', 'On November 6, 2012, he was re-elected and is currently serving the 57th term.', 'The next presidential election is scheduled to take place on November 8, 2016; on January 20, 2017, the newly elected president will take office.'], []]

for text in wiki:
	obtainlist = NER.get_continuous_chunks(str(text))
	for data in obtainlist:
		if data not in nerlist:
			nerlist.append(data)

for text in nerlist:
	print(text)
