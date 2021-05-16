from ViniAudit.providers.gcp.resources.projects import Projects
from ViniAudit.providers.gcp.resources.stackdriverlogging.sinks import Sinks
from ViniAudit.providers.gcp.resources.stackdriverlogging.metrics import Metrics


class StackdriverLogging(Projects):
    _children = [ 
        (Sinks, 'sinks'),
        (Metrics, 'metrics')
    ]
