# User Accounts

- A `ModelForm` is a helper class that creates a form automatically from a model, handling field generation, validation, and saving data to the database.

    ```python
    from django import forms.ModelForm
    from .models import User
    
    class UserForm(ModelForm):
        class Meta:
            model = User
            fields = ['username', 'email', 'password']
    ```

    A `ModelForm` Uses `Meta` class to specify the `model` and fields.

    key methods

    1. `save(commit=True)` – saves form data to the database (via the model instance)\
    `commit=False` – creates/updates model instance (without saving to database).
    2. `is_valid()` – Checks if submitted data is valid.
    3. `errors` – Returns validation errors.

- Django’s default authentication system provides a built-in way to handle user accounts, permissions, and sessions.

- In Django’s authentication system, every template has a `user` object available that always has an `is_authenticated` attribute set and a `username` attribute for authenticated users.