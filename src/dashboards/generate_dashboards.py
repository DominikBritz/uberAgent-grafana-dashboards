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
from templates.poor_user_experience.poor_user_experience import build_dashboard


OUTPUT_DIR = "../output"
DATA_SOURCES_FILE = "../datasources/config.json"

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(DATA_SOURCES_FILE) as f:
        configs = json.load(f)

    for config in configs:
        name = config["name"]
        queries = config["queries"]

        dashboard = build_dashboard(name, queries)
        print(f"Building dashboard for {name}...")
        print(dashboard)
        filename = f"{name.replace(' ', '_').lower()}_dashboard.json"
        with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as file:
            file.write(JSONEncoder(sort_keys=True, indent=2).encode(dashboard.build()))

if __name__ == "__main__":
    main()

