'''blocklist.py
this file just contains the blocklist of the jwt tokens. it will be imported by 
app and the logout resource so that tokens can be added to the blocklist when the user log out.'''

BLOCKLIST = set()