import pymongo

from bson import ObjectId
import json


class MiniMongo:
    '''
        This class builds the connection to the Mini Mongo database, used for short lived sotrage of data from Retrobiocat

    '''

    def mongo_connection(self):
        '''
            This function builds the the connection to the MongoDB instance
        '''

        pw = "Minimongo333!!!"
        UN = "MiniMongoAccessor"

        client = pymongo.MongoClient('mongodb+srv://MiniMongoAccessor:Minimongo333!!!@cluster0.cgs1w.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&authSource=admin')

        return client

    def get_collection(self):

        client = self.mongo_connection()
        db = client["Minimongo"]
        collection = db["retrobiohub"]
        payload = collection.find()
        for i in payload:
            print(i)

    def get_collection_by_id(self, id):
        ''' 
            extract entries from the MiniMongo database based on a submitted id 
            ---
            args:
                id: String; MiniMongo id to be queried
            returns:
                payload: dict; database entry
        '''

        newId = ObjectId(id)
        print("die id ist:", newId)

        client = self.mongo_connection()
        db = client["Minimongo"]
        collection = db["retrobiohub"]
        extract = collection.find_one({'_id':newId})
        print("der extract ist", extract)

        return extract

    def push_document(self, payload):
        '''
            mappes the retrobiocat model to the BioCatHub model and writes it to the MoniMongo Database
            ---
            args:
            payload: dict; Retrobiocat object to be mapped to a BioCatHub enzyme object.
            ---
            returns:
            id: json; object containing the database entry id of the previously stored object
        '''

        client = self.mongo_connection()
        db = client["Minimongo"]
        collection = db["retrobiohub"]

        post = {"experiment":payload}
        upload = collection.insert_one(post)
        id = upload.inserted_id
        return id
