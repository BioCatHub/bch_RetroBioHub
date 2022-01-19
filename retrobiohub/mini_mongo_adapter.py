import pymongo



class MiniMongo:
    '''
        This class builds the connection to the Mini Mongo database, used for short lived sotrage of data from Retrobiocat

    '''

    def __init__(self, payload):
        self.payload = payload

    def mongo_connection(self):
        '''
            This function builds the the connection to the MongoDB instance
        '''

        pw = "Minimongo333!!!"
        UN = "MiniMongoAccessor"

        client = pymongo.MongoClient('mongodb+srv://MiniMongoAccessor:Minimongo333!!!@cluster0.cgs1w.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

        return client

    def get_collection(self):

        client = self.mongo_connection()
        db = client["Minimongo"]
        collection = db["retrobiohub"]
        payload = collection.find()
        for i in payload:
            print(i)

    def push_document(self):
        '''
            writes the created biocathub_model to the MoniMongo Database
        '''

        client = self.mongo_connection()
        db = client["Minimongo"]
        collection = db["retrobiohub"]

        post = {"experiment":self.payload}
        upload = collection.insert_one(post)
        id = upload.inserted_id
        return id
