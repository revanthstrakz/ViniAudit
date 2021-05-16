from ViniAudit.providers.aws.facade.base import AWSFacade
from ViniAudit.providers.aws.resources.regions import Regions

from .keys import Keys


class KMS(Regions):
    _children = [
        (Keys, 'keys'),
    ]

    def __init__(self, facade: AWSFacade):
        super().__init__('kms', facade)
