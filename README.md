# Lumineer Cognito Admin CLI

Used for admin related corrections relating specifically to the Cognito User Pool.  Ideally we get this functionally into the Lumineer User Management API.

This is MVP stuff.  Need to run Python functions interactively at this time.


## Setup Environment

Requirements:

- Python 3.6+
- Pipenv

1. Create `.env` file in project root and add USER_POOL_ID.  No quotes around value.

    ```shell
    USER_POOL_ID=<cognito_user_pool_id>
    ```

1. Install dependencies

    ```shell
    pipenv install
    ```

1. Start interactive shell

    ```shell
    ./start_shell.sh
    ```

## Usage

```Python
import user_management
```

### Create user pool record

```Python
user_management.create_user('user-email-here')
```

### Delete user pool record

```Python
username=user_management.find_username_by_email('user-email-here')
user_management.disable_user(username)
user_management.delete_user(username)
```

### Exit interactive shell

```Python
quit()
```