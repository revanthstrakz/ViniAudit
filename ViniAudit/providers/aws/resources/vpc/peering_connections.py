from ViniAudit.providers.aws.facade.base import AWSFacade
from ViniAudit.providers.aws.resources.base import AWSResources


class PeeringConnections(AWSResources):
    def __init__(self, facade: AWSFacade, region: str):
        super().__init__(facade)
        self.facade = facade
        self.region = region

    async def fetch_all(self):
        raw_peering_connections = await self.facade.ec2.get_peering_connections(self.region)

        for raw_peering_connection in raw_peering_connections:
            id, peering_connection = self._parse_peering_connections(raw_peering_connection)
            self[id] = peering_connection

    def _parse_peering_connections(self, raw_peering_connection):
        raw_peering_connection['id'] = raw_peering_connection['name'] = raw_peering_connection['VpcPeeringConnectionId']
        return raw_peering_connection['id'], raw_peering_connection
