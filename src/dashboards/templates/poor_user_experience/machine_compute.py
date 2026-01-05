from grafana_foundation_sdk.builders import timeseries, table, azuremonitor
from grafana_foundation_sdk.models.dashboard import DataSourceRef
from templates.panel_factory import azuremonitor_logs_query, default_timeseries, default_table

def machine_cpu_usage_timeseries(query: str, datasource: str) -> timeseries.Panel:
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

def machine_memory_usage_timeseries(query: str, datasource: str) -> timeseries.Panel:
    if datasource == "azuremonitor":
        target = azuremonitor_logs_query(query=query)
    else:
        raise ValueError(f"Unsupported data source: {datasource}")
    
    return (
        default_timeseries()
        .title("Memory usage (p80)")
        .datasource(DataSourceRef(uid="$dashboard_datasource"))
        .with_target(target)
        .unit("percent")
    )

def machine_disk_utilization_timeseries(query: str, datasource: str) -> timeseries.Panel:
    if datasource == "azuremonitor":
        target = azuremonitor_logs_query(query=query)
    else:
        raise ValueError(f"Unsupported data source: {datasource}")
    
    return (
        default_timeseries()
        .title("Disk utilization (p80)")
        .datasource(DataSourceRef(uid="$dashboard_datasource"))
        .with_target(target)
        .unit("percent")
    )

def machine_io_latency_timeseries(query: str, datasource: str) -> timeseries.Panel:
    if datasource == "azuremonitor":
        target = azuremonitor_logs_query(query=query)
    else:
        raise ValueError(f"Unsupported data source: {datasource}")
    
    return (
        default_timeseries()
        .title("IO latency (sum)")
        .datasource(DataSourceRef(uid="$dashboard_datasource"))
        .with_target(target)
        .unit("ms")
    )

def machine_network_utilization_timeseries(query: str, datasource: str) -> timeseries.Panel:
    if datasource == "azuremonitor":
        target = azuremonitor_logs_query(query=query)
    else:
        raise ValueError(f"Unsupported data source: {datasource}")
    
    return (
        default_timeseries()
        .title("Network utilization (p80)")
        .datasource(DataSourceRef(uid="$dashboard_datasource"))
        .with_target(target)
        .unit("percent")
    )

def machine_pagefile_usage_timeseries(query: str, datasource: str) -> timeseries.Panel:
    if datasource == "azuremonitor":
        target = azuremonitor_logs_query(query=query)
    else:
        raise ValueError(f"Unsupported data source: {datasource}")
    
    return (
        default_timeseries()
        .title("Pagefile usage (p80)")
        .datasource(DataSourceRef(uid="$dashboard_datasource"))
        .with_target(target)
        .unit("percent")
    )

def machine_stop_errors_table(query: str, datasource: str) -> table.Panel:
    if datasource == "azuremonitor":
        target = azuremonitor_logs_query(query=query)
    else:
        raise ValueError(f"Unsupported data source: {datasource}")
    
    return (
        default_table()
        .title("Stop errors")
        .datasource(DataSourceRef(uid="$dashboard_datasource"))
        .with_target(target)
    )
