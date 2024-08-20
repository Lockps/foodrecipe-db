import os
from dotenv import load_dotenv


class Parameter:
    load_dotenv()
    website = os.getenv('test')
