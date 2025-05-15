# How to Contribute to the Project

Thank you in advance for wanting to contribute to this project! We appreciate your help in making this project better. Please follow the guidelines below to ensure a smooth contribution process.

## Found a Bug?

- Before creating a new issue, please check if the issue already exists.
- Provide a clear and descriptive title for the issue.

## Want to Contribute a Dashboard?

### ⚠️ Security Notice

This repository uses **GitHub Actions** with sensitive secrets.  
To prevent misuse, **we do not allow contributors to push branches directly** to the main repository.

---

### Requirements

Create an account at [Grafana](https://grafana.com/) which gives you a Grafana Cloud instance for free. This is mandatory.

### Step-by-Step Guide

#### 1. Fork the Repository

Click the **"Fork"** button in the top-right corner of the [main repository](https://github.com/DominikBritz/uberAgent-grafana-dashboards).

This will create your own copy of the repository under your GitHub account.

---

#### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/REPO_NAME.git
cd REPO_NAME
```

---

#### 3. Add the Original Repo as Upstream

```bash
git remote add upstream https://github.com/DominikBritz/uberAgent-grafana-dashboards.git
```

---

#### 4. Create a Feature Branch

```bash
git checkout -b feature/your-topic
```

---

#### 5. Set Up Your Own GitHub Actions Variables and Secrets

> GitHub does not expose secrets to workflows in forked repositories.

The GitHub workflow needs secrets (e.g., Grafana Cloud Stack ID), hence you must:

- Go to your fork → Settings → Secrets and variables → Actions
- Add the required variables and secrets to your repository
  - Variables
    - `GRAFANACTL_VERSION`: The version of `grafanactl` to use (e.g., `v0.1.0`)
    - `GRAFANA_SERVER`: The URL of your Grafana instance (e.g., `https://your-instance.grafana.net`)
    - `GRAFANA_STACK_ID`: The Stack ID of your Grafana instance (e.g., `12345678`). You can see all stacks in your Grafana Cloud account.
  - Secrets
    - `GRAFANA_TOKEN`: The API token for your Grafana instance. Go to `https://your-instance.grafana.net/org/serviceaccounts` and create a new service account with the `Admin` role. Generate a new service account token and copy it here.

---

#### 6. Make Your Changes

Write, test, and commit your changes:

```bash
git add .
git commit -m "Describe your change"
git push origin feature/your-topic
```
---

#### 7. Open a Pull Request

- Go to your fork on GitHub.
- Click "Compare & pull request".
- Choose the main repository as the base.
- Add a clear title and description.

#### 8. Keeping Your Fork Up to Date

To sync with the latest changes from upstream:

```bash
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

Rebase your feature branch if necessary.

---

#### 9. Code Reviews & Merge

Once your PR is approved by a maintainer and passes CI, it will be merged.

Thank you for contributing!
