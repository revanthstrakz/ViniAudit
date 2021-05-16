from ViniAudit.providers.aws.facade.base import AWSFacade
from ViniAudit.providers.aws.resources.regions import Regions

from .functions import Functions


class Lambdas(Regions):
    _children = [
        (Functions, 'functions')
    ]

    def __init__(self, facade: AWSFacade):
        super().__init__('lambda', facade)
