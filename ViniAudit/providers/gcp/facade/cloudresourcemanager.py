from ViniAudit.core.console import print_exception
from ViniAudit.providers.gcp.facade.basefacade import GCPBaseFacade
from ViniAudit.providers.utils import run_concurrently

class CloudResourceManagerFacade(GCPBaseFacade):
    def __init__(self):
        super().__init__('cloudresourcemanager', 'v1')

    async def get_member_bindings(self, project_id: str):
        try:
            cloudresourcemanager_client = self._get_client()
            response = await run_concurrently(
                    lambda: cloudresourcemanager_client.projects().getIamPolicy(resource=project_id).execute()
            )
            return response.get('bindings', [])
        except Exception as e:
            print_exception(f'Failed to retrieve project IAM policy bindings: {e}')
            return []
        


