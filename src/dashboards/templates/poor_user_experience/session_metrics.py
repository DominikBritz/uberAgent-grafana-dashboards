from grafana_foundation_sdk.builders import timeseries, azuremonitor
from grafana_foundation_sdk.models.dashboard import DataSourceRef
from templates.panel_factory import azuremonitor_logs_query, default_timeseries

def session_delay_per_session_timeseries(query: str, datasource: str) -> timeseries.Panel:
    if datasource == "azuremonitor":
        target = azuremonitor_logs_query(query=query)
    else:
        raise ValueError(f"Unsupported data source: {datasource}")
    
    return (
        default_timeseries()
        .title("Delay per session over time")
        .description("The 80th percentile of protocol latency + input delay per session")
        .height(8)
        .span(24)
        .datasource(DataSourceRef(uid="$dashboard_datasource"))
        .with_target(target)
        .unit("ms")
    )

def session_protocol_latency_timeseries(query: str, datasource: str) -> timeseries.Panel:
    if datasource == "azuremonitor":
        target = azuremonitor_logs_query(query=query)
    else:
        raise ValueError(f"Unsupported data source: {datasource}")
    
    return (
        default_timeseries()
        .title("Protocol latency")
        .datasource(DataSourceRef(uid="$dashboard_datasource"))
        .with_target(target)
        .unit("ms")
    )

def session_ica_rtt_timeseries(query: str, datasource: str) -> timeseries.Panel:
    if datasource == "azuremonitor":
        target = azuremonitor_logs_query(query=query)
    else:
        raise ValueError(f"Unsupported data source: {datasource}")
    
    return (
        default_timeseries()
        .title("ICA RTT")
        .datasource(DataSourceRef(uid="$dashboard_datasource"))
        .with_target(target)
        .unit("ms")
    )

def session_input_delay_timeseries(query: str, datasource: str) -> timeseries.Panel:
    if datasource == "azuremonitor":
        target = azuremonitor_logs_query(query=query)
    else:
        raise ValueError(f"Unsupported data source: {datasource}")
    
    return (
        default_timeseries()
        .title("Input delay")
        .datasource(DataSourceRef(uid="$dashboard_datasource"))
        .with_target(target)
        .unit("ms")
    )
