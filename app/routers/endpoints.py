import os

from fastapi import APIRouter, HTTPException
from app.database.models import User, UpdateUser
from app.helpers.firestore_utils import FirestoreService
from app.helpers.email_utils import send_email

router = APIRouter()
firestore_service = FirestoreService()

# Create user
@router.post("/add_users", response_model=User)
def add_user(user: User):
    # Convert the Pydantic model to a dictionary for Firestore insertion
    user_data = user.dict()  # This converts the Pydantic model to a dictionary
    return firestore_service.create_user(user_data)

# Get all users
@router.get("/get_users")
def get_users():
    return firestore_service.get_users()

# Update user details
@router.patch("/update_users")
def update_user(user: UpdateUser):
    if not user.id:
        raise HTTPException(status_code=400, detail="User ID is required for updating.")
    return firestore_service.update_user(user.id, user.dict())

# Delete user by ID
@router.delete("/delete_users")
def delete_user(user_id: str):
    return firestore_service.delete_user(user_id)


@router.get("/send-invite")
def send_invite():
    subject = "API Documentation Invitation"
    body = """
    <html>
        <body style="font-family: Arial, sans-serif; background-color: #f9f9f9; padding: 20px;">
            <div style="max-width: 600px; margin: auto; background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
                <h1 style="text-align: center; color: #4A90E2;">API Documentation Invitation</h1>
                <p>Hello,</p>
                <p>We are excited to invite you to view our User Management API documentation on <strong>ReDoc</strong>.</p>
                <p>You can access the documentation by clicking the button below:</p>
                <div style="text-align: center; margin: 20px 0;">
                    <a href="http://localhost:8000/redoc" 
                       style="background-color: #4A90E2; color: white; text-decoration: none; padding: 10px 20px; border-radius: 5px;">
                       View API Documentation
                    </a>
                </div>
                <p>As per the requirements, I changed that 'Any' method because of Flutter. Additionally:</p>
                <ul>
                    <li>I have set up an AWS EC2 instance for the public IP</li>
                    <li>Used Reverse Proxy for port forwarding</li>
                    <li>GCP Firestore for the database</li>
                </ul>
                <p>We appreciate your time and look forward to your feedback.</p>
                <p>Thank you,</p>
                <p style="text-align: center; font-size: 18px; font-weight: bold;">Ulrich Bachmann</p>
                <p style="text-align: center; font-size: 14px; color: #888;">If you have any questions, feel free to reply to this email.</p>
            </div>
        </body>
    </html>
    """
    attachment_path = os.getenv("IMG")  # Path to the uploaded image
    send_email(subject, body, ["dhavalchaudhary2014@gmail.com"], attachment_path)
    return {"detail": "Invitation sent successfully"}
