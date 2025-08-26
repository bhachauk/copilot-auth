import os
import copilot_auth as ca


def github_token_handler(token: str):
    print("GitHub Access Token:", token)


def copilot_token_handler(token: str):
    print("Copilot Token:", token)


if __name__ == '__main__':
    # os.environ['GITHUB_ACCESS_TOKEN'] = 'your_github_access_token_here'
    ca.authenticate_github_access_token(handlers=[github_token_handler])
    ca.authenticate_copilot_token(handlers=[copilot_token_handler])