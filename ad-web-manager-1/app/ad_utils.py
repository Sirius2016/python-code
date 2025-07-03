def add_user(username, password, first_name, last_name):
    # Function to add a user to Active Directory
    import ldap

    try:
        # Connect to the AD server
        conn = ldap.initialize('ldap://your_ad_server')
        conn.simple_bind_s('your_username', 'your_password')

        # Define the user attributes
        user_dn = f"CN={username},OU=Users,DC=your_domain,DC=com"
        attrs = {
            'objectClass': [b'top', b'person', b'organizationalPerson', b'user'],
            'sAMAccountName': [username.encode()],
            'userPrincipalName': [f"{username}@your_domain.com".encode()],
            'givenName': [first_name.encode()],
            'sn': [last_name.encode()],
            'userPassword': [password.encode()],
        }

        # Add the user
        conn.add_s(user_dn, [(key, value) for key, value in attrs.items()])

        # Set the user password
        conn.modify_s(user_dn, [(ldap.MOD_REPLACE, 'userPassword', [password.encode()])])
        conn.modify_s(user_dn, [(ldap.MOD_ADD, 'userAccountControl', [b'512'])])  # Enable the account

        conn.unbind_s()
        return True
    except Exception as e:
        print(f"Error adding user: {e}")
        return False


def delete_user(username):
    # Function to delete a user from Active Directory
    import ldap

    try:
        # Connect to the AD server
        conn = ldap.initialize('ldap://your_ad_server')
        conn.simple_bind_s('your_username', 'your_password')

        user_dn = f"CN={username},OU=Users,DC=your_domain,DC=com"
        conn.delete_s(user_dn)

        conn.unbind_s()
        return True
    except Exception as e:
        print(f"Error deleting user: {e}")
        return False


def batch_add_users(user_list):
    # Function to batch add users to Active Directory
    results = {}
    for user in user_list:
        username, password, first_name, last_name = user
        result = add_user(username, password, first_name, last_name)
        results[username] = result
    return results


def batch_delete_users(usernames):
    # Function to batch delete users from Active Directory
    results = {}
    for username in usernames:
        result = delete_user(username)
        results[username] = result
    return results