"""This module provides implementations for Resources and CompositeResources for Azure."""

import abc

from ViniAudit.providers.base.resources.base import Resources, CompositeResources


class AzureResources(Resources, metaclass=abc.ABCMeta):
    """This is the base class for Azure resources."""

    pass


class AzureCompositeResources(AzureResources, CompositeResources, metaclass=abc.ABCMeta):
    """This class represents a collection of composite Resources (resources that include nested resources referred as
    their children). Classes extending AzureCompositeResources have to define a '_children' attribute which consists of
    a list of tuples describing the children. The tuples are expected to respect the following format:
    (<child_class>, <child_name>). 'child_name' is used to indicate the name under which the child resources will be
    stored in the parent object.
    """

    pass
