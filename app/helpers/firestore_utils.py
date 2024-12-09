from app.database.database import db
from typing import  Dict

class FirestoreService:
    def create_user(self, user_data: Dict):
        """
        Create a user in the Firestore 'users' collection.
        """
        user_ref = db.collection("users").add(user_data)
        return {"id": user_ref[1].id, **user_data}

    def get_users(self):
        """
        Retrieve all users from the Firestore 'users' collection.
        """
        users_ref = db.collection("users")
        docs = users_ref.stream()
        return [{"id": doc.id, **doc.to_dict()} for doc in docs]

    def get_users_by_project(self, project_id: str):
        """
        Retrieve all users associated with a specific project.
        """
        users_ref = db.collection("users").where("project_id", "==", project_id)
        docs = users_ref.stream()
        return [{"id": doc.id, **doc.to_dict()} for doc in docs]

    def get_user_by_id(self, user_id: str):
        """
        Retrieve a single user by their unique Firestore document ID.
        """
        user_ref = db.collection("users").document(user_id)
        doc = user_ref.get()
        if doc.exists:
            return {"id": doc.id, **doc.to_dict()}
        return None

    def update_user(self, user_id: str, user_data: Dict):
        """
        Update a user's details in Firestore.
        """
        user_ref = db.collection("users").document(user_id)
        user_ref.update(user_data)
        updated_user = user_ref.get()
        return {"id": user_id, **updated_user.to_dict()}

    def delete_user(self, user_id: str):
        """
        Delete a user by their Firestore document ID.
        """
        user_ref = db.collection("users").document(user_id)
        user_ref.delete()
        return {"message": f"User with ID {user_id} deleted successfully."}