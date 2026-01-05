from grafana_foundation_sdk.builders import timeseries, azuremonitor
from grafana_foundation_sdk.models.dashboard import DataSourceRef
from templates.panel_factory import azuremonitor_logs_query, default_timeseries

def app_input_delay_per_app_timeseries(query: str, datasource: str) -> timeseries.Panel:
    if datasource == "azuremonitor":
        target = azuremonitor_logs_query(query=query)
    else:
        raise ValueError(f"Unsupported data source: {datasource}")
    
    return (
        default_timeseries()
        .title("Input delay per app (p80)")
        .datasource(DataSourceRef(uid="$dashboard_datasource"))
        .with_target(target)
        .unit("ms")
    )

def app_cpu_usage_timeseries(query: str, datasource: str) -> timeseries.Panel:
    if datasource == "azuremonitor":
        target = azuremonitor_logs_query(query=query)
    else:
        raise ValueError(f"Unsupported data source: {datasource}")
    
    return (
        default_timeseries()
        .title("CPU usage (p80)")
        .datasource(DataSourceRef(uid="$dashboard_datasource"))
        .with_target(target)
        .unit("percent")
    )

def app_memory_usage_timeseries(query: str, datasource: str) -> timeseries.Panel:
    if datasource == "azuremonitor":
        target = azuremonitor_logs_query(query=query)
    else:
        raise ValueError(f"Unsupported data source: {datasource}")
    
    return (
        default_timeseries()
        .title("Memory usage (p80)")
        .datasource(DataSourceRef(uid="$dashboard_datasource"))
        .with_target(target)
        .unit("MB")
    )

def app_disk_ios_timeseries(query: str, datasource: str) -> timeseries.Panel:
    if datasource == "azuremonitor":
        target = azuremonitor_logs_query(query=query)
    else:
        raise ValueError(f"Unsupported data source: {datasource}")
    
    return (
        default_timeseries()
        .title("Disk IOs (sum)")
        .datasource(DataSourceRef(uid="$dashboard_datasource"))
        .with_target(target)
    )

def app_network_throughput_timeseries(query: str, datasource: str) -> timeseries.Panel:
    if datasource == "azuremonitor":
        target = azuremonitor_logs_query(query=query)
    else:
        raise ValueError(f"Unsupported data source: {datasource}")
    
    return (
        default_timeseries()
        .title("Network thruput (p80)")
        .datasource(DataSourceRef(uid="$dashboard_datasource"))
        .with_target(target)
        .unit("MBs")
    )

def app_gpu_usage_timeseries(query: str, datasource: str) -> timeseries.Panel:
    if datasource == "azuremonitor":
        target = azuremonitor_logs_query(query=query)
    else:
        raise ValueError(f"Unsupported data source: {datasource}")
    
    return (
        default_timeseries()
        .title("GPU usage (p80)")
        .datasource(DataSourceRef(uid="$dashboard_datasource"))
        .with_target(target)
        .unit("percent")
    )

def app_gpu_memory_timeseries(query: str, datasource: str) -> timeseries.Panel:
    if datasource == "azuremonitor":
        target = azuremonitor_logs_query(query=query)
    else:
        raise ValueError(f"Unsupported data source: {datasource}")
    
    return (
        default_timeseries()
        .title("GPU memory (p80)")
        .datasource(DataSourceRef(uid="$dashboard_datasource"))
        .with_target(target)
        .unit("MB")
    )

def app_handle_count_timeseries(query: str, datasource: str) -> timeseries.Panel:
    if datasource == "azuremonitor":
        target = azuremonitor_logs_query(query=query)
    else:
        raise ValueError(f"Unsupported data source: {datasource}")
    
    return (
        default_timeseries()
        .title("Handle count (sum)")
        .datasource(DataSourceRef(uid="$dashboard_datasource"))
        .with_target(target)
    )

def app_thread_count_timeseries(query: str, datasource: str) -> timeseries.Panel:
    if datasource == "azuremonitor":
        target = azuremonitor_logs_query(query=query)
    else:
        raise ValueError(f"Unsupported data source: {datasource}")
    
    return (
        default_timeseries()
        .title("Thread count (sum)")
        .datasource(DataSourceRef(uid="$dashboard_datasource"))
        .with_target(target)
    )

def app_errors_hangs_timeseries(query: str, datasource: str) -> timeseries.Panel:
    if datasource == "azuremonitor":
        target = azuremonitor_logs_query(query=query)
    else:
        raise ValueError(f"Unsupported data source: {datasource}")
    
    return (
        default_timeseries()
        .title("Errors & Hangs over time (sum)")
        .draw_style("bars")
        .fill_opacity(50)
        .datasource(DataSourceRef(uid="$dashboard_datasource"))
        .with_target(target)
    )
