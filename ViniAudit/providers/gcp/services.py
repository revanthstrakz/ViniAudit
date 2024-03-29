from ViniAudit.providers.base.services import BaseServicesConfig
from ViniAudit.providers.gcp.facade.base import GCPFacade
from ViniAudit.providers.gcp.resources.cloudsql.base import CloudSQL
from ViniAudit.providers.gcp.resources.cloudstorage.base import CloudStorage
from ViniAudit.providers.gcp.resources.gce.base import ComputeEngine
from ViniAudit.providers.gcp.resources.iam.base import IAM
from ViniAudit.providers.gcp.resources.kms.base import KMS
from ViniAudit.providers.gcp.resources.stackdriverlogging.base import StackdriverLogging
from ViniAudit.providers.gcp.resources.stackdrivermonitoring.base import StackdriverMonitoring
from ViniAudit.providers.gcp.resources.gke.base import KubernetesEngine


class GCPServicesConfig(BaseServicesConfig):

    def __init__(self, credentials=None, default_project_id=None,
                 project_id=None, folder_id=None, organization_id=None, all_projects=None,
                 **kwargs):

        super().__init__(credentials)

        facade = GCPFacade(default_project_id, project_id, folder_id, organization_id, all_projects)

        self.cloudsql = CloudSQL(facade)
        self.cloudstorage = CloudStorage(facade)
        self.computeengine = ComputeEngine(facade)
        self.iam = IAM(facade)
        self.kms = KMS(facade)
        self.stackdriverlogging = StackdriverLogging(facade)
        self.stackdrivermonitoring = StackdriverMonitoring(facade)
        self.kubernetesengine = KubernetesEngine(facade)

    def _is_provider(self, provider_name):
        return provider_name == 'gcp'
