from functools import wraps

def require_login(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access Denied.")
            return None #explicit for safety
        else:
            return func(user_role)
    return wrapper

@require_login
def access(user):
    print("Access granted to inventory.")

access("user")
access("admin")

