from ViniAudit.providers.gcp.resources.projects import Projects
from ViniAudit.providers.gcp.resources.cloudsql.database_instances import DatabaseInstances


class CloudSQL(Projects):
    _children = [ 
        (DatabaseInstances, 'instances')
     ]
