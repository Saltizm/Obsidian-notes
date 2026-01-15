- Injecting malicious SQL code through inputs 
### Example
Consider a login form that checks credentials with:

```sql
SELECT * FROM users WHERE username = '$username' AND password = '$password';
```

If the application blindly inserts user input without validation, an attacker could input:
- **Username:** `admin' --`
- **Password:** (anything)    

The resulting query becomes:

```sql
SELECT * FROM users WHERE username = 'admin' --' AND password = 'anything';
```

- The attacker logs in as `admin` without knowing the password.