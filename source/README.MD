# The source Folder

- Contains the source files for the dashboards. The `am` folder contains the Azure Monitor JSON files, and the `adx` folder contains the Azure Data Explorer JSON files.
- Only the Azure Monitor JSON files in `source/am` must be modified. The Azure Data Explorer JSON files in `source/adx` are generated from the Azure Monitor JSON files with a GitHub Workflow and should not be modified directly. The workflow also creates the `dist` folder with the final JSON files.
- The dashboards in the `source/am` and `source/adx` folders **cannot** be imported into Grafana directly. They must be converted to the Grafana JSON format first. The conversion is done with a GitHub Workflow that runs on every push to the `main` branch when files in `source/am` change.
