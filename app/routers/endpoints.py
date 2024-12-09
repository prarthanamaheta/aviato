import os
from app.helpers.email_utils import send_email
from fastapi import APIRouter, HTTPException
from typing import  Optional, Dict
from app.helpers.firestore_utils import FirestoreService

router = APIRouter()
firestore_service = FirestoreService()


# Add User Endpoint
@router.post("/add_users")
def add_user(user_data: Dict):
    """
    Create a new user with arbitrary data.
    """
    if "project_id" not in user_data:
        raise HTTPException(status_code=400, detail="Project ID is required.")
    return firestore_service.create_user(user_data)

# Get All Users Endpoint
@router.get("/get_users")
def get_users(project_id: Optional[str] = None):
    """
    Retrieve all users or filter by project_id.
    """
    if project_id:
        return firestore_service.get_users_by_project(project_id)
    return firestore_service.get_users()

# Update User Endpoint
@router.patch("/update_users")
def update_user(user_id: str, user_data: Dict):
    """
    Update user details with arbitrary data.
    """
    if not user_id:
        raise HTTPException(status_code=400, detail="User ID is required for updating.")
    if "project_id" in user_data:
        raise HTTPException(
            status_code=400, detail="Project ID cannot be updated directly."
        )
    return firestore_service.update_user(user_id, user_data)

# Delete User Endpoint
@router.delete("/delete_users")
def delete_user(user_id: str, project_id: Optional[str] = None):
    """
    Delete a user by ID. Optionally ensure they belong to a specific project.
    """
    user = firestore_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")

    if project_id and user.get("project_id") != project_id:
        raise HTTPException(
            status_code=403, detail="User does not belong to the specified project."
        )

    return firestore_service.delete_user(user_id)

@router.get("/send-invite")
def send_invite():
    url = os.getenv('URL')
    github_link=os.getenv("GITHUB")
    subject = "Aviato Users Management API Documentation Invitation"
    body = f"""
    <html>
        <body style="font-family: Arial, sans-serif; background-color: #f9f9f9; padding: 20px;">
            <div style="max-width: 600px; margin: auto; background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
                <h1 style="text-align: center; color: #4A90E2;">Aviato Users Management API Documentation Invitation</h1>
                <p>Hello,</p>
                <p>We are excited to invite you to view our Aviato Users Management API documentation on <strong>ReDoc</strong>.</p>
                <p>You can access the documentation by clicking the button below:</p>
                <div style="text-align: center; margin: 20px 0;">
                    <a href="{url}" 
                       style="background-color: #4A90E2; color: white; text-decoration: none; padding: 10px 20px; border-radius: 5px;">
                       View API Documentation
                    </a>
                </div>
                <p>Additionally:</p>
                <ul>
                    <li>I have set up an AWS EC2 instance for the public IP</li>
                    <li>Used Reverse Proxy for port forwarding</li>
                    <li>GCP Firestore for the database</li>
                </ul>
                <p>We appreciate your time and look forward to your feedback.</p>
                <p>You can also check out the project on GitHub:</p>
                <div style="text-align: center; margin: 20px 0;">
                    <a href="{github_link}" 
                       style="background-color: #4A90E2; color: white; text-decoration: none; padding: 10px 20px; border-radius: 5px;">
                       View on GitHub
                    </a>
                </div>
                <p>Thank you,</p>
                <p style="text-align: center; font-size: 18px; font-weight: bold;">Prarthana Maheta</p>
                <p style="text-align: center; font-size: 14px; color: #888;">If you have any questions, feel free to reply to this email.</p>
            </div>
        </body>
    </html>
    """
    email_list = os.getenv("RECEIPT_LIST").split(",")
    attachment_path = os.getenv("IMG")  # Path to the uploaded image
    send_email(subject, body, email_list, attachment_path)
    return {"detail": "Invitation sent successfully"}
