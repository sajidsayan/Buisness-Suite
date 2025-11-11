"""
Business Suite Modules Package
"""

from .crm import CRMModule
from .accounting import AccountingModule
from .inventory import InventoryModule
from .hr import HRModule
from .projects import ProjectModule
from .analytics import AnalyticsModule

__all__ = [
    'CRMModule',
    'AccountingModule', 
    'InventoryModule',
    'HRModule',
    'ProjectModule',
    'AnalyticsModule'
]