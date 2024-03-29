from azure.mgmt.keyvault import KeyVaultManagementClient

from ViniAudit.core.console import print_exception
from ViniAudit.providers.utils import run_concurrently
from ViniAudit.utils import get_user_agent


class KeyVaultFacade:

    def __init__(self, credentials):
        self.credentials = credentials

    def get_client(self, subscription_id: str):
        client = KeyVaultManagementClient(self.credentials.get_credentials('arm'),
                                        subscription_id=subscription_id)
        client._client.config.add_user_agent(get_user_agent())
        return client

    async def get_key_vaults(self, subscription_id: str):
        try:
            client = self.get_client(subscription_id)
            return await run_concurrently(
                lambda: list(client.vaults.list_by_subscription()))
        except Exception as e:
            print_exception(f'Failed to retrieve key vaults: {e}')
            return []
