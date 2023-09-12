#!/usr/bin/env python3
"""where can i learn python ?"""

def schools_by_topic(mongo_collection, topic):
    """return the list"""
    collection_list = []
    
    for documents in mongo_collection.find({"topics": topic}):
        collection_list.append(documents)
    return collection_list
