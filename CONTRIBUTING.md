# How to Contribute to the Project

Thank you in advance for wanting to contribute to this project! We appreciate your help in making this project better. Please follow the guidelines below to ensure a smooth contribution process.

## Found a Bug?

- Before creating a new issue, please check if the issue already exists.
- Provide a clear and descriptive title for the issue.

## Want to Contribute a Dashboard?

- Clone the repository and create a new branch for your changes.
- Only the Azure Monitor JSON files in `source/am` must be modified. The Azure Data Explorer JSON files in `source/adx` are generated from the Azure Monitor JSON files with a GitHub Workflow and should not be modified directly. The workflow also creates the `dist` folder with the final JSON files.
- Create a pull request with a clear description of your changes.
