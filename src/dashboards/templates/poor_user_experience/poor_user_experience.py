from grafana_foundation_sdk.builders import dashboard
from grafana_foundation_sdk.models.dashboard import (
    DataSourceRef,
    DashboardCursorSync,
    DashboardLinkType,
    VariableOption,
    VariableRefresh,
    VariableSort,
)
from templates.panel_factory import azuremonitor_logs_query, default_timeseries

import templates.poor_user_experience.overview as overview

def build_dashboard(data_source_name: str, queries: dict) -> dashboard:
    builder = (
        dashboard.Dashboard("Troubleshooting Poor User Experience 2")
        .uid("poor-user-experience")
        .tags(["generated", "uberAgent"])
        .editable()
        .tooltip(DashboardCursorSync.CROSSHAIR)
        .time("now-3h", "now")
        .timezone("browser")

        # Panels
        .with_panel(overview.overview_session_delay_timeseries(queries["overview_session_delay"], data_source_name))

        
    )

    return builder

    