import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db=client['ahaddb']
# collection=db.create_collection("student")
collection=db["student"]
def insert_ex():
    all_documents = [
        {
        "empid":105,
        "ename":"irfan",
        "email":"irfan@gmail.com"
        },
        {
        "empid":106,
        "ename":"muskaan",
        "email":"muskan@gmail.com"
        }
    ]
    resp = collection.insert_many(all_documents)
    print('inserted ',resp.inserted_ids)
def read_ex():
    documents = collection.find()
    for document in documents:
        print(document)
def update_ex():
    up_document_by={"empid":101}
    new_document={"$set":{"name":"b"}}
    resp=collection.update_one(up_document_by,new_document)
    print('updated many ',resp.upserted_id)
def delete_ex():
    document = {"empid":101}
    resp = collection.delete_one(document)
    print('reocrd deleted by ',resp.deleted_count)
# insert_ex()
read_ex()
# update_ex()
# delete_ex()
client.close()