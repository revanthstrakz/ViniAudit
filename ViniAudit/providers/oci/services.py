from ViniAudit.providers.oci.authentication_strategy import OracleCredentials
from ViniAudit.providers.oci.facade.base import OracleFacade
from ViniAudit.providers.oci.resources.identity.base import Identity
from ViniAudit.providers.oci.resources.kms.base import KMS
from ViniAudit.providers.oci.resources.objectstorage.base import ObjectStorage
from ViniAudit.providers.base.services import BaseServicesConfig


class OracleServicesConfig(BaseServicesConfig):
    def __init__(self, credentials: OracleCredentials = None, **kwargs):
        super().__init__(credentials)

        facade = OracleFacade(credentials)

        self.identity = Identity(facade)
        self.objectstorage = ObjectStorage(facade)
        self.kms = KMS(facade)

    def _is_provider(self, provider_name):
        return provider_name == 'oci'
