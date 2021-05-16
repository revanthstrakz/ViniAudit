from ViniAudit.providers.oci.facade.base import OracleFacade
from ViniAudit.providers.oci.resources.base import OracleCompositeResources
from ViniAudit.providers.oci.resources.kms.keyvaults import KeyVaults


class KMS(OracleCompositeResources):
    _children = [
        (KeyVaults, 'keyvaults')
    ]

    def __init__(self, facade: OracleFacade):
        super().__init__(facade)
        self.service = 'kms'

    async def fetch_all(self, **kwargs):
        await self._fetch_children(resource_parent=self)
