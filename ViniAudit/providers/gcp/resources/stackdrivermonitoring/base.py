from ViniAudit.providers.gcp.resources.projects import Projects
from ViniAudit.providers.gcp.resources.stackdrivermonitoring.uptime_checks import UptimeChecks
from ViniAudit.providers.gcp.resources.stackdrivermonitoring.alert_policies import AlertPolicies


class StackdriverMonitoring(Projects):
    _children = [ 
        (UptimeChecks, 'uptime_checks'),
        (AlertPolicies, 'alert_policies')
    ]
