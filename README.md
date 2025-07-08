# NoShiPasswords
imagine a no AI, no telemetry, no ads, free, open-source, no BS password manager. that is what this is.

**you're welcome.**

---

# How To Use
## First
Go to the [latest release](https://github.com/averagebagelenjoyer/NoShiPasswords/releases/latest) and download `Source code (zip)`. Unzip the folder, and then go inside.

Make sure the latest version of Python is installed, view the source code so that you yourself can be assured it is safe, and run `SETUP.py`.

## Creating your first database
Run `create_db.py` and follow the steps it says to create a database. **DO NOT FORGET YOUR MASTER PASSWORD. THERE IS NO WAY TO RESET OR MODIFY YOUR PASSWORD AFTER INITALLY SETTING IT.**

## Viewing your database
Run `retrieve_db.py` and follow the steps it says to retrieve the passwords from your database. *Please note that it will copy the passwords to your clipboard and not visually display them.*

## Editing your database
Run `edit_db.py` and follow the steps it says to edit the passwords from your database.

## Generating passwords
Run `generate_passwd.py`. You will now be using a RegEx based password generator. It is suggested that use check out [regular expression 101](https://regex101.com/), and possibly look up some YouTube videos if you do not know how RegEx works.

This allows you to generate extremely specific passwords exactly to your needs. For example `![A-Za-z ]{100}` will copy a one-hundred character long passwords that supports spaces, uppercase letters, and lowercase letters.

---

## features
> *Note: The text in the parentheses is the current status of said feature.*

- cross-system *(windows, linux, and mac)*
- configurable one-way encryption *(not very configurable at the moment)*
- master password based decryption
- open-source
- fully offline *(any online features are opt-in)*
- RegEx based password generation
- *by a fellow paranoid computer nerd*

### it's *your* password manager. everything after this is opt-in
- on login [HIBP](https://haveibeenpwned.com/) detection *(i haven't even started this yet)*

### not quite finished features
- multiple master passwords *(nor have i started this)*

# Our Focus
1. privacy. anything even semi-instrusive is opt in.
2. security. we actively encourage that you go into the config.ini and modify the settings.
3. user friendliness. this is the least of our concerns. we want it to be easy to use, but if that means sacrificing security or privacy, we won't do it.

when i say *we* i mean *me* because atm it's an indie project.

## we got everything you need — even a link to buy a bagel
[here](https://www.hero.co/products/everything-bagel/)
