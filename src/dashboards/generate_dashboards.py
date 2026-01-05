import os
import json
from grafana_foundation_sdk.builders import dashboard
from grafana_foundation_sdk.cog.encoder import JSONEncoder
from grafana_foundation_sdk.models.dashboard import (
    DataSourceRef,
    DashboardCursorSync,
    DashboardLinkType,
    VariableOption,
    VariableRefresh,
    VariableSort,
)

# Import all dashboards
from templates.poor_user_experience.poor_user_experience import build_dashboard_poor_user_experience

OUTPUT_DIR = "../output"
DATA_SOURCES_FILE = "../config/config.json"

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Load the data source configuration
    with open(DATA_SOURCES_FILE) as f:
        configs = json.load(f)

    # Run through each data source configuration
    # and build the dashboard
    for config in configs:
        ds_name = config["ds_name"]
        ds_queries = config["ds_queries"]

        dashboard = build_dashboard_poor_user_experience(ds_name, ds_queries)
        dashboard_name = "Troubleshooting Poor User Experience 2"
        print(f"Dashboard name: {dashboard_name}")
        print(f"Building dashboards for data source {ds_name}")
        filename = f"{dashboard_name.replace(' ', '_').lower()}_{ds_name.replace(' ', '_').lower()}.json"
        with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as file:
            file.write(JSONEncoder(sort_keys=True, indent=2).encode(dashboard.build()))

if __name__ == "__main__":
    main()

