# The dist Folder

- Contains the final JSON files for the dashboards.
- The JSON files in this folder are not meant to be modified directly. If you want to make changes to the dashboards, modify the Azure Monitor JSON files in the `source/am` folder and let the GitHub Workflow generate the new JSON files in this folder.
- The dashboards in this folder can be imported into Grafana directly. The latest stable releases are available via GitHub Releases. The latest development releases are available  in this folder.
