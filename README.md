# Aviato Users Management API

This FastAPI application provides endpoints for managing users, including creating, updating, retrieving, and deleting users. Additionally, it offers an endpoint for sending an email invitation with a link to the API documentation and a GitHub repository.

## Endpoints

### 1. **Create User**
- **URL**: `/add_users`
- **Method**: `POST`
- **Request Body**: `User` (Pydantic Model)

Creates a new user in the Firestore database.

#### Example Request Body:
```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "project_id": "project_123"
}
```

### 2. **Get All Users**
- **URL**: `/get_users`
- **Method**: `GET`

Fetches all users from the Firestore database.

#### Response:
- **Success**:
  - **Code**: `200 OK`
  - **Body**: List of users stored in the Firestore database.

Example response:
```json
[
  {
    "id": "1",
    "username": "john_doe",
    "email": "john@example.com",
    "project_id": "project_123"
  },
  {
    "id": "2",
    "username": "jane_smith",
    "email": "jane@example.com",
    "project_id": "project_456"
  }
]
```

### 3. **Update User Details**
- **URL**: `/update_users`
- **Method**: `PATCH`

Updates the details of an existing user in the Firestore database.

#### Request Body:
- **Content-Type**: `application/json`
- **Body**: A JSON object that contains the user ID and the fields to be updated.

Example request body:
```json
{
  "id": "1",
  "username": "john_doe_updated",
  "email": "john_updated@example.com",
  "project_id": "project_456"
}
```

### 4. **Delete User**
- **URL**: `/delete_users`
- **Method**: `DELETE`

Deletes a user by their `user_id`.

#### Query Parameter:
- `user_id` (string) - The ID of the user to be deleted.


#### Response:
- **Success**:
  - **Code**: `200 OK`
  - **Body**: A confirmation message indicating the deletion of the user.

Example response:
```json
{
  "detail": "User deleted successfully."
}
```

### 5. **Send API Documentation Invitation**
- **URL**: `/send-invite`
- **Method**: `GET`

Sends an email invitation to a list of recipients with a link to the API documentation and a GitHub project link. The email also includes information about the environment and setup.

#### Environment Variables Required:
- `URL`: The URL to access the API documentation (ReDoc).
- `GITHUB`: The GitHub repository link for the project.
- `RECEIPT_LIST`: A comma-separated list of email addresses to send the invitation to.
- `IMG`: The path to an image to be attached to the email.


#### Response:
- **Success**:
  - **Code**: `200 OK`
  - **Body**: A success message indicating the invitation was sent successfully.

Example response:
```json
{
  "detail": "Invitation sent successfully"
}
```

### Environment Variables

You will need to configure the following environment variables in a `.env` file for the application to work properly:

```makefile
GOOGLE_APPLICATION_CREDENTIALS=<path_to_your_google_credentials_json>
SENDER=<your_email_address>
PASSWORD=<your_email_password>
IMG=<path_to_image_to_attach>
RECEIPT_LIST=<comma_separated_list_of_email_addresses>
URL=<url_for_api_documentation>
GITHUB=<url_to_github_repo>
```


## Installation and Setup

### 1. Clone this repository:

```bash
git clone <repository_url>
```

### 2. Create a .env file in the root directory and configure your environment variables (as described above).
### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 4. Run the application:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### 5. Access the API documentation:
Open http://localhost:8000/redoc in your browser.

## Testing

You can test the API using a tool like Postman or `curl`.

### Create User:
```arduino
POST http://localhost:8000/add_users
```

### Get Users:
```arduino
GET http://localhost:8000/get_users
```

### Update User:
```arduino
PATCH http://localhost:8000/update_users
```

### DELETE User:
```arduino
DELETE http://localhost:8000/delete_users?user_id=<user_id>
```


### Send Invitation:
```arduino
GET http://localhost:8000/send-invite
```

## License

This project is licensed under the MIT License.

### Explanation:
- The `README.md` file provides descriptions for each of the endpoints in your FastAPI application.
- It also includes the setup instructions for configuring the environment variables and running the application.
- The environment variables are listed in a clear format with instructions to place them in a `.env` file.
- It includes instructions on how to run the application, access the API documentation, and test the endpoints.

Let me know if you need any further customizations!

