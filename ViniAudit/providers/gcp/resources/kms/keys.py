from ViniAudit.providers.base.resources.base import Resources
from ViniAudit.providers.gcp.facade.base import GCPFacade


class Keys(Resources):
    def __init__(self, facade: GCPFacade, project_id: str, keyring_name: str, location: str):
        super().__init__(facade)
        self.project_id = project_id
        self.keyring_name = keyring_name
        self.location = location

    async def fetch_all(self):
        raw_keys = await self.facade.kms.list_keys(self.project_id, self.location, self.keyring_name)
        for raw_key in raw_keys:
            key_id, key = self._parse_key(raw_key)
            self[key_id] = key

    def _parse_key(self, raw_key):
        key_dict = {}

        key_dict['id'] = raw_key['name'].split('/')[-1]
        key_dict['state'] = raw_key.get('primary', {}).get('state', None)
        key_dict['creation_datetime'] = raw_key.get('primary', {}).get('createTime', None)
        key_dict['protection_level'] = raw_key.get('primary', {}).get('protectionLevel', None)
        key_dict['algorithm'] = raw_key.get('primary', {}).get('algorithm', None)
        key_dict['next_rotation_datetime'] = raw_key.get('nextRotationTime', None)
        key_dict['purpose'] = raw_key['purpose']
        key_dict['rotation_period'] = raw_key.get('rotationPeriod', None)

        return key_dict['id'], key_dict
