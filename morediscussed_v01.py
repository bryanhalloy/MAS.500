#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 11:30:27 2016

@author: bryanhalloy
"""

"""
This program intends to answer the question: 
 Did US Mainstream Media sources talk about Trump 
 or Clinton more in September 2016?
"""
 
import mediacloud, datetime
mediacloudcall = mediacloud.api.MediaCloud('MY KEY')

# perform a call to the api to collect sentence information
sentencecount_trump = mediacloudcall.sentenceCount('(Trump)', solr_filter=[mediacloudcall.publish_date_query( datetime.date( 2016, 9, 1), datetime.date( 2016, 9, 30) ), 'tags_id_media:1' ])
sentencecount_clinton = mediacloudcall.sentenceCount('(Clinton)', solr_filter=[mediacloudcall.publish_date_query( datetime.date( 2016, 9, 1), datetime.date( 2016, 9, 30) ), 'tags_id_media:1' ])

#Determine who was talked about more
if sentencecount_trump > sentencecount_clinton:
    winner = "Trump"
elif sentencecount_clinton > sentencecount_trump:
    winner = "Clinton"
else:
    winner = "No winner; they were discussed equally"


# print the results of the queries
print "\n%s was discussed the most." % (winner)
print "\nNumber of sentences that talked about Trump:" + str(sentencecount_trump['count'])
print "\nNumber of sentences that talked about Clinton:" + str(sentencecount_clinton['count'])


