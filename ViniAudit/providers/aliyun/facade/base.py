from collections import Counter

from aliyunsdkcore.endpoint.local_config_regional_endpoint_resolver import LocalConfigRegionalEndpointResolver

from ViniAudit.providers.aliyun.authentication_strategy import AliyunCredentials
from ViniAudit.providers.aliyun.facade.actiontrail import ActiontrailFacade
from ViniAudit.providers.aliyun.facade.ecs import ECSFacade
from ViniAudit.providers.aliyun.facade.kms import KMSFacade
from ViniAudit.providers.aliyun.facade.ram import RAMFacade
from ViniAudit.providers.aliyun.facade.rds import RDSFacade
from ViniAudit.providers.aliyun.facade.vpc import VPCFacade
from ViniAudit.providers.aliyun.facade.oss import OSSFacade
from ViniAudit.providers.utils import run_concurrently


class AliyunFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials
        self._instantiate_facades()
        self._resolver = LocalConfigRegionalEndpointResolver()

    def _instantiate_facades(self):
        self.actiontrail = ActiontrailFacade(self._credentials)
        self.ram = RAMFacade(self._credentials)
        self.ecs = ECSFacade(self._credentials)
        self.rds = RDSFacade(self._credentials)
        self.vpc = VPCFacade(self._credentials)
        self.kms = KMSFacade(self._credentials)
        self.oss = OSSFacade(self._credentials)

    async def build_region_list(self, service: str, chosen_regions=None):

        # TODO could need this for service ids
        # service = 'ec2containerservice' if service == 'ecs' else service

        # TODO does a similar endpoint exist?
        # available_services = await run_concurrently(lambda: Session().get_available_services())
        # if service not in available_services:
        #     raise Exception('Service ' + service + ' is not available.')

        regions = await run_concurrently(
            lambda: self._resolver.get_valid_region_ids_by_product(product_code=service))

        if chosen_regions:
            return list((Counter(regions) & Counter(chosen_regions)).elements())
        else:
            return regions
