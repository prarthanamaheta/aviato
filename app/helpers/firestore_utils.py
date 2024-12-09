from app.database.database import db
from app.database.models import User

class FirestoreService:
    def create_user(self, user_data):
        user_ref = db.collection("users").add(user_data)
        return {"id": user_ref[1].id, **user_data}  # Returning the generated ID

    def get_users(self):
        users_ref = db.collection("users")
        docs = users_ref.stream()
        return [{"id": doc.id, **doc.to_dict()} for doc in docs]

    def update_user(self, user_id, user_data):
        user_ref = db.collection("users").document(user_id)
        user_ref.update(user_data)
        return {"id": user_id, **user_data}

    def delete_user(self, user_id):
        user_ref = db.collection("users").document(user_id)
        user_ref.delete()
        return {"message": f"User with id {user_id} deleted successfully."}
