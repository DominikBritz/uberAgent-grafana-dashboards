from grafana_foundation_sdk.builders import dashboard
from grafana_foundation_sdk.models.dashboard import (
    DataSourceRef,
    DashboardCursorSync,
    DashboardLinkType,
    VariableOption,
    VariableRefresh,
    VariableSort,
)
from templates.panel_factory import text_panel, row_panel
from templates.variable_factory import (
    textbox_variable,
    custom_variable,
    datasource_variable,
)

import templates.poor_user_experience.overview as overview
import templates.poor_user_experience.session_metrics as session_metrics
import templates.poor_user_experience.machine_compute as machine_compute
import templates.poor_user_experience.app_compute as app_compute

# Instructions markdown content
INSTRUCTIONS_CONTENT = """## 🎯 Troubleshooting Poor User Experience

Diagnosing poor user experience in virtual sessions is complex — it requires analyzing multiple layers such as input responsiveness, protocol performance, system load, and network conditions. This dashboard helps simplify that process.

Start by identifying sessions with **high session delay** (input delay + protocol latency), then use the lower panels to investigate **root causes** like app or network performance issues.

> 💡 **Tip:** Click on a username in any data table to **filter the entire dashboard** to that specific user's session.

---

## 🧮 Why Percentiles Matter

Most metrics in this dashboard (e.g. input delay, protocol latency, CPU, RAM, Disk) are calculated using the **80th percentile**, rather than the average or maximum.

- The **80th percentile** means: "80% of the time, values were below this number."
- It helps **ignore brief spikes**, while still highlighting **consistently poor performance**.
- It's more realistic for assessing **typical user experience** than using averages.

---

## 🧪 What Is Session Delay?

**Session Delay** = **User Input Delay** + **Protocol Latency**

- **Protocol Latency**: Measures network-related delay in remoting protocols like ICA or RDP.
- **User Input Delay**: Captures the time between user input (e.g. keypress) and the moment it is picked up by the application — a direct indicator of system/app responsiveness.

---

## 📊 How To Interpret Session Delay

Session delay categories used in this dashboard:

- 🟢 **Excellent**: consistently **below 40 ms**
- 🔵 **Good**: mostly below 40 ms, always **below 200 ms**
- 🟡 **Mediocre**: consistently **below 400 ms**
- 🔴 **Poor**: frequently **above 400 ms**

> ℹ️ [More info on user input delay](https://uberagent.com/blog/uberagent-7-1-preview-user-input-delay-application-responsiveness/)"""


def build_dashboard_poor_user_experience(data_source_name: str, queries: dict) -> dashboard:
    builder = (
        dashboard.Dashboard("Troubleshooting Poor User Experience")
        .uid("poor-user-experience")
        .tags(["generated", "uberAgent"])
        .editable()
        .tooltip(DashboardCursorSync.CROSSHAIR)
        .time("now-3h", "now")
        .timezone("browser")

        # Variables
        .with_variable(
            datasource_variable("dashboard_datasource", "Data source", "grafana-azure-monitor-datasource")
        )
        .with_variable(
            textbox_variable(
                "User",
                "User",
                "Filter the dashboard to usernames or parts of username. I.e. \"jo\" would include the users \"joe\" and \"john\".",
                ""
            )
        )
        .with_variable(
            textbox_variable(
                "Computer",
                "Machine",
                "Filter the dashboard to computer names or parts of computer names. I.e. \"pc\" would include the computers \"pc1\" and \"pc-test\".",
                ""
            )
        )
        .with_variable(
            textbox_variable(
                "App",
                "App",
                "Filter the dashboard to an app or parts of app names. I.e. \"my\" would include the apps \"my-dev-app\" and \"my-hr-app\".",
                ""
            )
        )
        .with_variable(
            custom_variable(
                "time_agg",
                "Time aggregation",
                ["1m", "5m", "10m", "15m", "30m", "1h", "1d"],
                "10m"
            )
            .description("Time series charts aggregate metrics over a time frame. You can change the time frame here.")
        )

        # Panels
        # Instructions panel
        .with_panel(text_panel(INSTRUCTIONS_CONTENT))

        # Overview row
        .with_panel(row_panel("Overview", collapsed=True))
        .with_panel(overview.overview_session_delay_timeseries(queries["overview"]["session_delay"], data_source_name))
        .with_panel(overview.overview_session_count_timeseries(queries["overview"]["session_count"], data_source_name))
        .with_panel(overview.overview_session_table(queries["overview"]["session_table"], data_source_name))

        # Session metrics row
        .with_panel(row_panel("Session metrics", collapsed=True))
        .with_panel(session_metrics.session_delay_per_session_timeseries(queries["session_metrics"]["delay_per_session"], data_source_name))
        .with_panel(session_metrics.session_protocol_latency_timeseries(queries["session_metrics"]["protocol_latency"], data_source_name))
        .with_panel(session_metrics.session_ica_rtt_timeseries(queries["session_metrics"]["ica_rtt"], data_source_name))
        .with_panel(session_metrics.session_input_delay_timeseries(queries["session_metrics"]["input_delay"], data_source_name))

        # Machine compute row
        .with_panel(row_panel("Machine compute", collapsed=True))
        .with_panel(machine_compute.machine_cpu_usage_timeseries(queries["machine_compute"]["cpu_usage"], data_source_name))
        .with_panel(machine_compute.machine_memory_usage_timeseries(queries["machine_compute"]["memory_usage"], data_source_name))
        .with_panel(machine_compute.machine_disk_utilization_timeseries(queries["machine_compute"]["disk_utilization"], data_source_name))
        .with_panel(machine_compute.machine_io_latency_timeseries(queries["machine_compute"]["io_latency"], data_source_name))
        .with_panel(machine_compute.machine_network_utilization_timeseries(queries["machine_compute"]["network_utilization"], data_source_name))
        .with_panel(machine_compute.machine_pagefile_usage_timeseries(queries["machine_compute"]["pagefile_usage"], data_source_name))
        .with_panel(machine_compute.machine_stop_errors_table(queries["machine_compute"]["stop_errors"], data_source_name))

        # App compute row
        .with_panel(row_panel("App compute", collapsed=True))
        .with_panel(app_compute.app_input_delay_per_app_timeseries(queries["app_compute"]["input_delay_per_app"], data_source_name))
        .with_panel(app_compute.app_cpu_usage_timeseries(queries["app_compute"]["cpu_usage"], data_source_name))
        .with_panel(app_compute.app_memory_usage_timeseries(queries["app_compute"]["memory_usage"], data_source_name))
        .with_panel(app_compute.app_disk_ios_timeseries(queries["app_compute"]["disk_ios"], data_source_name))
        .with_panel(app_compute.app_network_throughput_timeseries(queries["app_compute"]["network_throughput"], data_source_name))
        .with_panel(app_compute.app_gpu_usage_timeseries(queries["app_compute"]["gpu_usage"], data_source_name))
        .with_panel(app_compute.app_gpu_memory_timeseries(queries["app_compute"]["gpu_memory"], data_source_name))
        .with_panel(app_compute.app_handle_count_timeseries(queries["app_compute"]["handle_count"], data_source_name))
        .with_panel(app_compute.app_thread_count_timeseries(queries["app_compute"]["thread_count"], data_source_name))
        .with_panel(app_compute.app_errors_hangs_timeseries(queries["app_compute"]["errors_hangs"], data_source_name))
    )

    return builder

    