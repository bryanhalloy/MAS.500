#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 11:30:27 2016

@author: bryanhalloy
"""

"""
This program intends to answer the question: 
 Did US Mainstream Media sources talk about Clinton 
 or ______ more in From June through Halloween 2016?
"""
 
import locale, datetime

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

key_mediacloud = "6f590e3ba161d1a86cb4e8ecd6c7ba67aba4a367abc948626602a5f0fb6c2d87"
logger.info('Mediacloud key set')

date_querystart = datetime.date( 2016, 6, 1)
logger.info('Start Date set')

date_queryend = datetime.date( 2016, 10, 31)
logger.info('End Date set')

term_userdefined = raw_input("Insert term to company to Clinton: \n")
logger.info('User-defined term set: ' + term_userdefined)



#define functions

def getsentencecount( inputstring, mediacloudkey, startdate, enddate ):
   "function that takes the query terms as an input, and outputs the number of sentences which contained it"
   import mediacloud
   mediacloudcall = mediacloud.api.MediaCloud(mediacloudkey)
   
   sentencecount_inputstring = mediacloudcall.sentenceCount(str(inputstring), solr_filter=[mediacloudcall.publish_date_query(startdate, enddate ), 'tags_id_media:1' ])
   sentencecount_inputstring_value = sentencecount_inputstring['count']
   logger.debug('Sentence Count determined for '+  inputstring)

   return sentencecount_inputstring_value

# perform a call to the api to collect sentence information

sentencecount_clinton = getsentencecount("clinton", key_mediacloud, date_querystart, date_queryend)
sentencecount_input = getsentencecount(term_userdefined, key_mediacloud, date_querystart, date_queryend)


#Determine who was talked about more
if sentencecount_clinton > sentencecount_input:
    winner = "Clinton"
    logger.info('Winner determined')
elif sentencecount_input > sentencecount_clinton:
    winner = term_userdefined
    logger.info('Winner determined')
else:
    winner = "No winner; they were discussed equally"
    logger.info('Winner determined')

    
ratio_sentencecount = float(sentencecount_clinton) / float(sentencecount_input)


# print the results of the queries
locale.setlocale(locale.LC_ALL, 'en_US')
'en_US'

print "\nWhat was discussed more?: %s." % (winner)
print "\nFor every time %s was discussed, Clinton was discussed %.3f times." % (term_userdefined, ratio_sentencecount)

print "\nNumber of sentences that talked about Clinton: " + str(locale.format("%d", sentencecount_clinton, grouping=True))
print "\nNumber of sentences that talked about "+term_userdefined+": " + str(locale.format("%d", sentencecount_input, grouping=True))






