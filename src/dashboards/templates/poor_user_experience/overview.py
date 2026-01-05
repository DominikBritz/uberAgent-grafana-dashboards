from grafana_foundation_sdk.builders import timeseries, azuremonitor
from grafana_foundation_sdk.models.dashboard import DataSourceRef
from grafana_foundation_sdk.models import units
from templates.panel_factory import azuremonitor_logs_query, default_timeseries

def overview_session_delay_timeseries(query: str, datasource: str) -> timeseries.Panel:
   
   if datasource == "azuremonitor":
      target = (azuremonitor_logs_query(query=query))
   else:
      raise ValueError(f"Unsupported data source: {datasource}") 

   return (
      default_timeseries()
      .title("Session Delay")
      .description("Session Delay")
      .datasource(DataSourceRef(uid="$dashboard_datasource"))
      .with_target(
         azuremonitor.AzureLogsQuery()
         .query(query)
         .dashboard_time(False)
         .result_format("logs")
         .time_column("TimeGenerated")
      )
   )