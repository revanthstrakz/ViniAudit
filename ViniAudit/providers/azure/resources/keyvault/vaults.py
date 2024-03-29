from ViniAudit.providers.azure.facade.base import AzureFacade
from ViniAudit.providers.azure.resources.base import AzureResources
from ViniAudit.providers.utils import get_non_provider_id
from ViniAudit.providers.azure.utils import get_resource_group_name


class Vaults(AzureResources):

    def __init__(self, facade: AzureFacade, subscription_id: str):
        super().__init__(facade)
        self.subscription_id = subscription_id

    async def fetch_all(self):
        for raw_vault in await self.facade.keyvault.get_key_vaults(self.subscription_id):
            id, vault = self._parse_key_vault(raw_vault)
            self[id] = vault

    def _parse_key_vault(self, raw_vault):
        vault = {}
        vault['id'] = get_non_provider_id(raw_vault.id)
        vault['name'] = raw_vault.name
        vault['type'] = raw_vault.type
        vault['location'] = raw_vault.location
        vault['additional_properties'] = raw_vault.additional_properties
        if raw_vault.tags is not None:
            vault['tags'] = ["{}:{}".format(key, value) for key, value in  raw_vault.tags.items()]
        else:
            vault['tags'] = []
        vault['resource_group_name'] = get_resource_group_name(raw_vault.id)
        vault['properties'] = raw_vault.properties
        vault['public_access_allowed'] = self._is_public_access_allowed(raw_vault)
        return vault['id'], vault

    def _is_public_access_allowed(self, raw_vault):
        return raw_vault.properties.network_acls is None
