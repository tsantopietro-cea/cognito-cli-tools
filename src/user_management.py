import boto3
import os
from src.passwords import generate_random_password

USER_POOL_ID = os.environ.get('USER_POOL_ID')

client = boto3.client('cognito-idp')

def find_user_by_email(email):
    return client.list_users(
        UserPoolId=USER_POOL_ID,
        AttributesToGet=['email'],
        Filter="=".join(["email", "'%s'" % email])
    )

def validate_user_response(response, expected_count):
    return len(response.get('Users')) == expected_count

def get_username_from_response(response, index=0):
    return response.get('Users')[index].get('Username') 

def find_username_by_email(email):
    response = find_user_by_email(email)
    if not validate_user_response(response, expected_count=1):
        return ''

    return get_username_from_response(response)

def disable_user(username):
    try:
        response = client.admin_disable_user(
            UserPoolId=USER_POOL_ID,
            Username=username
        )
    
    except client.exceptions.UserNotFoundException as e:
        return {
            "error": False, 
            "success": True, 
            "message": "User was not found", 
            "data": None
        }

    except Exception as e:
        return {
            "error": True, 
            "success": False, 
            "message": str(e), 
            "data": None
        }

    return {
        "error": False, 
        "success": True, 
        "message": "User was disabled as requested", 
        "data": response
    }

def enable_user(username):
    try:
        response = client.admin_enable_user(
            UserPoolId=USER_POOL_ID,
            Username=username
        )
    
    except client.exceptions.UserNotFoundException as e:
        return {
            "error": False, 
            "success": True, 
            "message": "User was not found", 
            "data": None
        }

    except Exception as e:
        return {
            "error": True, 
            "success": False, 
            "message": str(e), 
            "data": None
        }

    return {
        "error": False, 
        "success": True, 
        "message": "User was enabled as requested", 
        "data": response
    }   

def delete_user(username):
    try:
        response = client.admin_delete_user(
            UserPoolId=USER_POOL_ID,
            Username=username
        )

    except client.exceptions.UserNotFoundException as e:
        return {
            "error": False,
            "success": True,
            "message": "User was not found",
            "data": None
        }

    except Exception as e:
        return {
            "error": True, 
            "success": False, 
            "message": str(e), 
            "data": None
        }

    return {
        "error": False, 
        "success": True, 
        "message": "User was deleted as requested", 
        "data": response
    }

def create_user(email):
    password = generate_random_password(12)

    try:
        response = client.admin_create_user(
            UserPoolId=USER_POOL_ID,
            Username=email,
            UserAttributes=[
                {
                    'Name': 'email',
                    'Value': email
                },
                {
                    'Name': 'email_verified',
                    'Value': 'true'
                }
            ],
            TemporaryPassword=password,
            DesiredDeliveryMediums=['EMAIL']
        )
    
    except client.exceptions.UsernameExistsException as e:
        return {
            "error": False, 
            "success": True, 
            "message": "Username already exists", 
            "data": None            
        }

    except client.exceptions.InvalidPasswordException as e:
        return {
            "error": False, 
            "success": True, 
            "message": "Password should have Caps, Special chars, Numbers", 
            "data": None
        }

    except Exception as e:
        return {
            "error": True, 
            "success": False, 
            "message": str(e), 
            "data": None
        }
    
    return {
        "error": False, 
        "success": True, 
        "message": "Please confirm your signup, \
                    check Email for validation code", 
        "data": response
    }