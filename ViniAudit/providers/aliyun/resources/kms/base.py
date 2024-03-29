from ViniAudit.providers.aliyun.resources.regions import Regions
from ViniAudit.providers.aliyun.facade.base import AliyunFacade
from ViniAudit.providers.aliyun.resources.kms.keys import Keys


class KMS(Regions):
    _children = [
        (Keys, 'keys')
    ]

    def __init__(self, facade: AliyunFacade):
        super().__init__('kms', facade)
