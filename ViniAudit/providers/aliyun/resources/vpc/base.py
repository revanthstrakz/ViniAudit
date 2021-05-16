from ViniAudit.providers.aliyun.resources.regions import Regions
from ViniAudit.providers.aliyun.resources.vpc.vpcs import VPCs
from ViniAudit.providers.aliyun.facade.base import AliyunFacade


class VPC(Regions):
    _children = [
        (VPCs, 'vpcs')
    ]

    def __init__(self, facade: AliyunFacade):
        super().__init__('vpc', facade)
