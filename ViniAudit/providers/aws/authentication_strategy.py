import boto3
import logging

from ViniAudit import __version__
from ViniAudit.providers.aws.utils import get_caller_identity
from ViniAudit.providers.base.authentication_strategy import AuthenticationStrategy, AuthenticationException


class AWSCredentials:

    def __init__(self, session):
        self.session = session


class AWSAuthenticationStrategy(AuthenticationStrategy):
    """
    Implements authentication for the AWS provider
    """

    def authenticate(self,
                     profile=None,
                     aws_access_key_id=None, aws_secret_access_key=None, aws_session_token=None,
                     **kwargs):

        try:

            # Set logging level to error for libraries as otherwise generates a lot of warnings
            logging.getLogger('botocore').setLevel(logging.ERROR)
            logging.getLogger('botocore.auth').setLevel(logging.ERROR)
            logging.getLogger('urllib3').setLevel(logging.ERROR)

            if profile:
                session = boto3.Session(profile_name=profile)
            elif aws_access_key_id and aws_secret_access_key:
                if aws_session_token:
                    session = boto3.Session(
                        aws_access_key_id=aws_access_key_id,
                        aws_secret_access_key=aws_secret_access_key,
                        aws_session_token=aws_session_token,
                    )
                else:
                    session = boto3.Session(
                        aws_access_key_id=aws_access_key_id,
                        aws_secret_access_key=aws_secret_access_key,
                    )
            else:
                session = boto3.Session()

            # Test querying for current user
            get_caller_identity(session)

            # Set custom user agent
            session._session.user_agent_name = 'Vini Audit'
            session._session.user_agent_extra = 'Vini Audit/{} (https://gitplaceholder.todo)'.format(__version__)
            session._session.user_agent_version = __version__

            return AWSCredentials(session=session)

        except Exception as e:
            raise AuthenticationException(e)
