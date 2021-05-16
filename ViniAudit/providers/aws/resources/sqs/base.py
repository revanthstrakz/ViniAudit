from ViniAudit.providers.aws.facade.base import AWSFacade
from ViniAudit.providers.aws.resources.regions import Regions

from .queues import Queues


class SQS(Regions):
    _children = [
        (Queues, 'queues')
    ]

    def __init__(self, facade: AWSFacade):
        super().__init__('sqs', facade)
