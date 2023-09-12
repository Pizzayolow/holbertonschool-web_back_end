#!/usr/bin/env python3
"""show somes stats"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school

    db_name = "logs"
    col_name = "nginx"

    db = client[db_name]
    collection = db[col_name]

    document_count = collection.count_documents({})
    print(f"{document_count} logs")

    filter_get = {"method": "GET"}
    get_count = collection.count_documents(filter_get)

    filter_put = {"method": "PUT"}
    put_count = collection.count_documents(filter_put)

    filter_post = {"method": "POST"}
    post_count = collection.count_documents(filter_post)

    filter_patch = {"method": "PATCH"}
    patch_count = collection.count_documents(filter_patch)

    filter_delete = {"method": "DELETE"}
    delete_count = collection.count_documents(filter_delete)

    filter_status = {"path": "/status", "method": "GET"}
    status_count = collection.count_documents(filter_status)

    print("Methods:")
    print(f"\tmethod GET: {get_count}")
    print(f"\tmethod POST: {post_count}")
    print(f"\tmethod PUT: {put_count}")
    print(f"\tmethod PATCH: {patch_count}")
    print(f"\tmethod DELETE: {delete_count}")
    print(f"{status_count} status check")

