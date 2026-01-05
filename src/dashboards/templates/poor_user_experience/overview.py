from grafana_foundation_sdk.builders import timeseries, table, azuremonitor
from grafana_foundation_sdk.models.dashboard import DataSourceRef
from grafana_foundation_sdk.models import common
from templates.panel_factory import (
    azuremonitor_logs_query,
    azuredataindexplorer_query,
    default_timeseries,
    default_table,
)

def overview_session_delay_timeseries(query: str, datasource: str) -> timeseries.Panel:
   if datasource == "azuremonitor":
      target = azuremonitor_logs_query(query=query)
   elif datasource == "azuredataindexplorer":
      target = azuredataindexplorer_query(query=query)
   else:
      raise ValueError(f"Unsupported data source: {datasource}")

   return (
      default_timeseries()
      .title("Session delay overview")
      .description("The 80th percentile of protocol latency + input delay for all sessions. Gauges the overall user experience.")
      .datasource(DataSourceRef(uid="$dashboard_datasource"))
      .with_target(target)
      .unit("ms")
   )

def overview_session_count_timeseries(query: str, datasource: str) -> timeseries.Panel:
   if datasource == "azuremonitor":
      target = azuremonitor_logs_query(query=query)
   elif datasource == "azuredataindexplorer":
      target = azuredataindexplorer_query(query=query)
   else:
      raise ValueError(f"Unsupported data source: {datasource}")

   return (
      default_timeseries()
      .title("Session count")
      .height(7)
      .span(7)
      .datasource(DataSourceRef(uid="$dashboard_datasource"))
      .with_target(target)
      .draw_style("bars")
      .fill_opacity(100)
   )

def overview_session_table(query: str, datasource: str) -> table.Panel:
   """Create a session table panel showing all sessions with details."""
   if datasource == "azuremonitor":
      target = azuremonitor_logs_query(query=query)
   elif datasource == "azuredataindexplorer":
      target = azuredataindexplorer_query(query=query)
   else:
      raise ValueError(f"Unsupported data source: {datasource}")

   return (
      default_table()
      .title("Session table")
      .description("The table lists all sessions in the selected timeframe, sorted by session delay. Click on a session to filter the dashboard.")
      .height(10)
      .datasource(DataSourceRef(uid="$dashboard_datasource"))
      .with_target(target)
   )