# Created by Acas Saleem
# Git: https://github.com/Acassaleem
# Educational Purposes Only
import string
import secrets
import pyperclip

alphabet = string.ascii_letters + string.digits + string.punctuation

# Generates a random 20 character password
password = ''.join(secrets.choice(alphabet) for x in range(20))
print("Generated Password:", password)
pyperclip.copy(password)  # Copies to the clipboard
