from ViniAudit.providers.gcp.resources.kms.keyrings import KeyRings
from ViniAudit.providers.gcp.resources.projects import Projects


class KMS(Projects):
    _children = [
        (KeyRings, 'keyrings')
    ]
