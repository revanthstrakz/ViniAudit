from ViniAudit.providers.aws.facade.base import AWSFacade
from ViniAudit.providers.aws.resources.base import AWSResources
from ViniAudit.providers.utils import get_non_provider_id


class MetricFilters(AWSResources):
    def __init__(self, facade: AWSFacade, region: str):
        super(MetricFilters, self).__init__(facade)
        self.region = region

    async def fetch_all(self):
        for raw_metric_filter in await self.facade.cloudwatch.get_metric_filters(self.region):
            name, resource = self._parse_metric_filter(raw_metric_filter)
            self[name] = resource

    def _parse_metric_filter(self, raw_metric_filter):
        metric_filter_dict = {}
        metric_filter_dict['id'] = get_non_provider_id('{}{}'.format(raw_metric_filter.get('filterName'),
                                                                     raw_metric_filter.get('creationTime')))
        metric_filter_dict['name'] = raw_metric_filter.get('filterName')
        metric_filter_dict['creation_time'] = raw_metric_filter.get('creationTime')
        metric_filter_dict['pattern'] = raw_metric_filter.get('filterPattern')
        metric_filter_dict['metric_transformations'] = raw_metric_filter.get('metricTransformations')
        metric_filter_dict['log_group_name'] = raw_metric_filter.get('logGroupName')
        return metric_filter_dict['id'], metric_filter_dict


