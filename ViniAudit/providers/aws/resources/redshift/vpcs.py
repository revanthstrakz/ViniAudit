from ViniAudit.providers.aws.resources.vpcs import Vpcs

from .clusters import Clusters


class RedshiftVpcs(Vpcs):
    _children = [
        (Clusters, 'clusters'),
    ]
