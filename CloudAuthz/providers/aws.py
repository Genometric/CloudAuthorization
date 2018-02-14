"""
Implements means of exchanging user ID token with temporary access and secret key.
"""
import requests


class Authorize:

    action = "AssumeRoleWithWebIdentity"
    version = "2011-06-15"

    def __init__(self):
        pass

    def authorize(self, identity_token, role_arn, duration, role_session_name):
        url = "https://sts.amazonaws.com/?" \
              "DurationSeconds={}&" \
              "Action={}&Version={}&" \
              "RoleSessionName={}&" \
              "RoleArn={}&" \
              "WebIdentityToken={}"\
            .format(duration, self.action, self.version, role_session_name,role_arn, identity_token)
        response = requests.get(url)
        return response.content
