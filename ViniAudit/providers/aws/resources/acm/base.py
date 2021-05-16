from ViniAudit.providers.aws.facade.base import AWSFacade
from ViniAudit.providers.aws.resources.regions import Regions

from .certificates import Certificates


class Certificates(Regions):
    _children = [
        (Certificates, 'certificates')
    ]

    def __init__(self, facade: AWSFacade):
        super().__init__('acm', facade)
