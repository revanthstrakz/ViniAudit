from ViniAudit.providers.gcp.resources.gce.instances import Instances
from ViniAudit.providers.gcp.resources.zones import Zones


class GCEZones(Zones):
    _children = [
        (Instances, 'instances'),
    ]
