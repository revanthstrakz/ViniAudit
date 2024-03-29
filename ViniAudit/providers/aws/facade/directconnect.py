from ViniAudit.core.console import print_exception
from ViniAudit.providers.aws.facade.basefacade import AWSBaseFacade
from ViniAudit.providers.aws.facade.utils import AWSFacadeUtils
from ViniAudit.providers.utils import run_concurrently


class DirectConnectFacade(AWSBaseFacade):
    async def get_connections(self, region):
        client = AWSFacadeUtils.get_client('directconnect', self.session, region)
        try:
            return await run_concurrently(lambda: client.describe_connections()['connections'])
        except Exception as e:
            print_exception(f'Failed to describe Direct Connect connections: {e}')
            return []
