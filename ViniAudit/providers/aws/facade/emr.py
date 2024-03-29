from ViniAudit.core.console import print_exception
from ViniAudit.providers.aws.facade.basefacade import AWSBaseFacade
from ViniAudit.providers.aws.facade.utils import AWSFacadeUtils
from ViniAudit.providers.utils import map_concurrently, run_concurrently


class EMRFacade(AWSBaseFacade):
    async def get_clusters(self, region):

        try:
            cluster_list = await AWSFacadeUtils.get_all_pages('emr', region, self.session, 'list_clusters', 'Clusters')
            cluster_ids = [cluster['Id'] for cluster in cluster_list]
        except Exception as e:
            print_exception(f'Failed to get EMR clusterss: {e}')
            return []
        else:
            return await map_concurrently(self._get_cluster, cluster_ids, region=region)

    async def _get_cluster(self, cluster_id: str, region: str):
        client = AWSFacadeUtils.get_client('emr', self.session, region)
        try:
            return await run_concurrently(lambda: client.describe_cluster(ClusterId=cluster_id)['Cluster'])
        except Exception as e:
            print_exception(f'Failed to describe EMR cluster: {e}')
            raise
