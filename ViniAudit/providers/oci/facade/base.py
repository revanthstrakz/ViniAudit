from ViniAudit.providers.oci.facade.identity import IdentityFacade
from ViniAudit.providers.oci.facade.kms import KMSFacade
from ViniAudit.providers.oci.facade.objectstorage import ObjectStorageFacade
from ViniAudit.providers.oci.authentication_strategy import OracleCredentials


class OracleFacade:
    def __init__(self, credentials: OracleCredentials):
        self._credentials = credentials
        self._instantiate_facades()

    def _instantiate_facades(self):
        self.identity = IdentityFacade(self._credentials)
        self.kms = KMSFacade(self._credentials)
        self.objectstorage = ObjectStorageFacade(self._credentials)
