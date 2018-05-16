#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function

import json

from watson_developer_cloud import DiscoveryV1

import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')


discovery = DiscoveryV1(

    version='2017-10-16',

    username='username goes here',

    password='password goes here')



environments = discovery.list_environments()

print(json.dumps(environments, indent=2))



news_environment_id = '84c8fd9f-8dbe-4c00-9d55-806e950f36e9'

print(json.dumps(news_environment_id, indent=2))



collections = discovery.list_collections(news_environment_id)

news_collections = [x for x in collections['collections']]

#print(json.dumps(collections, indent=2))



#
environment_id=news_environment_id
#
#print(json.dumps(configurations, indent=2))



query_results = discovery.query(news_environment_id,

                                news_collections[0]['collection_id'],

                                filter='enriched_text.entities.text:"ICO"',

                                return_fields='text')

#print(json.dumps(query_results, indent=1))

#json_object = json.loads(json.dumps(query_results))
json_object = json.loads(json.dumps(query_results))
#print (json_object)

#print (json_object['results'][0]['text'])
startmessage = "starting here"

print (startmessage)

#print (json_object['results'][0]['text'])

for answer in json_object['results']:
        answer_to_display = answer['text'].replace('\n', '<br />')
        print (answer_to_display)


#extracted_text = json.loads(query_results)



# new_environment = discovery.create_environment(name="new env", description="bogus env")

# print(new_environment)



#if (discovery.get_environment(environment_id=new_environment['environment_id'])['status'] == 'active'):

#    writable_environment_id = new_environment['environment_id']

#    new_collection = discovery.create_collection(environment_id=writable_environment_id,

#                                                name='Example Collection',

#                                                description="just a test")

#

#    print(new_collection)

    #print(discovery.get_collections(environment_id=writable_environment_id))

    #res = discovery.delete_collection(environment_id='10b733d0-1232-4924-a670-e6ffaed2e641',

    #                                  collection_id=new_collection['collection_id'])

#    print(res)



# collections = discovery.list_collections(environment_id=writable_environment_id)

# print(collections)



#with open(os.path.join(os.getcwd(),'..','resources','simple.html')) as fileinfo:

#    print(discovery.test_document(environment_id=writable_environment_id, fileinfo=fileinfo))





# In[25]:



# with open(os.path.join(os.getcwd(),'..','resources','simple.html')) as fileinfo:

#     res = discovery.add_document(environment_id=writable_environment_id,

#                                 collection_id=collections['collections'][0]['collection_id'],

#                                 fileinfo=fileinfo)

#    print(res)





#res = discovery.get_collection(environment_id=writable_environment_id,

#                               collection_id=collections['collections'][0]['collection_id'])

#print(res['document_counts'])





#res = discovery.delete_environment(environment_id=writable_environment_id)

#print(res)
