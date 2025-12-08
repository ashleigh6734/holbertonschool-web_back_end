#!/usr/bin/env python3
"""Log Stats"""
from pymongo import MongoClient


def log_stats(mongo_collection):
    """Prints some stats about Nginx logs stored in MongoDB"""
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")
    
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        method_count = mongo_collection.count_documents({'method': method})
        print(f"method {method}: {method_count}")
    
    status_check = mongo_collection.count_documents({'path': '/status'})
    print(f"{status_check} status check")
