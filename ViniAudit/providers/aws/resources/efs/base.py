from ViniAudit.providers.aws.facade.base import AWSFacade
from ViniAudit.providers.aws.resources.regions import Regions

from .filesystems import FileSystems


class EFS(Regions):
    _children = [
        (FileSystems, 'filesystems')
    ]

    def __init__(self, facade: AWSFacade):
        super().__init__('efs', facade)
