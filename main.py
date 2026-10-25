from dotenv import load_dotenv
load_dotenv()

import os

if __name__ == '__main__':
    print(os.getenv("LANGSMITH_PROJECT"))
