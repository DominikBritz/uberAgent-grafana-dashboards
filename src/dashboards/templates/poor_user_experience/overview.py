from grafana_foundation_sdk.builders import timeseries
from grafana_foundation_sdk.models.dashboard import DataSourceRef
from grafana_foundation_sdk.models import units
from templates.panel_factory import azuremonitor_logs_query, default_timeseries

def overview_session_delay_timeseries(query: str, datasource: str) -> timeseries.Panel:
   
   if datasource == "azuremonitor":
        target = azuremonitor_logs_query(query=query)
   
   return (
      default_timeseries()
      .title("Session Delay")
      .description("Session Delay")
      .with_target(target)
   )