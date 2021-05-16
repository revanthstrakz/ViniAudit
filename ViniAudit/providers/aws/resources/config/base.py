from ViniAudit.providers.aws.facade.base import AWSFacade
from ViniAudit.providers.aws.resources.config.recorders import Recorders
from ViniAudit.providers.aws.resources.config.rules import Rules
from ViniAudit.providers.aws.resources.regions import Regions


class Config(Regions):
    _children = [
        (Recorders, 'recorders'),
        (Rules, 'rules')
    ]

    def __init__(self, facade: AWSFacade):
        super().__init__('config', facade)
