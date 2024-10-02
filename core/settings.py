from decouple import config

base_url: str = 'http://localhost:8000/api/v1/'
username: str = config('USERNAME_SGE')
password: str = config('PASSWORD_SGE')