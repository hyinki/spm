from werkzeug.security import check_password_hash
from .Employees import Employees  # Import the Employees model

class Login:
    def check_user_password(self, user_id, input_password):
        # Get the password hash for the user by their ID
        pword = Employees.check_pword(user_id)
        
        if not pword:  # If the user does not exist
            return "User not found"
        
        # Check if the input password matches the stored hash
        if not check_password_hash(pword, input_password):
            return "Incorrect password"
        
        return "Login successful"
