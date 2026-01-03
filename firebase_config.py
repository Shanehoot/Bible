import firebase_admin
from firebase_admin import credentials, firestore

# Use your local Firebase service account key (for testing)
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
