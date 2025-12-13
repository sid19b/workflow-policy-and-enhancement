SecureFlow is an internal company system that manages approvals in a secure and trackable way.

1. User performs an action from frontend (clicks approve, create request, etc.)
2. Frontend sends API request with JWT token
3. Backend validates the token
4. Backend identifies the user from token
5. Backend checks if user has permission (RBAC)
6. Backend opens a DB session
7. Business logic is executed
8. Database is updated if needed
9. Response is sent back to frontend
10. DB session is closed


run with uvicorn
uvicorn main:app --reload
here file name is main.py and app is default