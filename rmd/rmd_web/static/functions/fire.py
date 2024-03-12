
from google.cloud.firestore_v1 import SERVER_TIMESTAMP
from firebase_admin import firestore

db = firestore.client()

def add_user_profile(user_profile_data):
    doc_ref = db.collection('user_profiles').document(user_profile_data['email'])
    doc_ref.set({
        'full_name': user_profile_data['full_name'],
        'profile_picture': user_profile_data['profile_picture'],
        'professional_background': user_profile_data['professional_background'],
        'interests': user_profile_data['interests'],
        'privacy_settings': user_profile_data['privacy_settings'],
    })
    
