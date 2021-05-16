from ViniAudit.providers.aws.facade.base import AWSFacade
from ViniAudit.providers.aws.resources.regions import Regions

from .identities import Identities


class SES(Regions):
    _children = [
        (Identities, 'identities')
    ]

    def __init__(self, facade: AWSFacade):
        super().__init__('ses', facade)
