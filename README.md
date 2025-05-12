# uberAgent Grafana Dashboards

Collection of Grafana dashboards for uberAgent for Azure Monitor and Azure Data Explorer data sources. Aims to provide quick and easy access to select uberAgent use-cases without the need for Splunk.

> This project is not maintained by Citrix. It is a community-driven effort to provide useful dashboards for non-Splunk backends for uberAgent.
>
> DO NOT CONTACT Citrix SUPPORT FOR REQUESTS OR ISSUES RELATED TO THIS PROJECT.

## 🏆 Project goal

The goal of this project is to provide a set of Grafana dashboards for uberAgent that are easy to use and serve select use-cases. The dashboards are not meant to replace the existing Splunk dashboards, but rather to provide an alternative for users who do not want to use Splunk as a backend.

While the Splunk dashboards visualize every metric uberAgent collects, the Grafana dashboards focus on select use-cases. They are a good starting point to get started with uberAgent, Azure and Grafana, but they are not a replacement for the full uberAgent experience.

The dashboards are designed to be used with Azure Monitor or Azure Data Explorer as data sources. The dashboards have the exact same structure and features, but the queries and inputs are different. GitHub automation keeps the dashboards in sync. You can choose the one for your preferred backend.

## 💡 Use-cases

The Grafana dashboards in this repository are designed to address the following use-cases.

### 🎯 Troubleshooting poor user experience

Diagnosing poor user experience in virtual sessions is complex — it requires analyzing multiple layers such as input responsiveness, protocol performance, system load, and network conditions. This dashboard helps simplify that process.

It introduces **Session Delay** as leading metric. Session delay consists of **User Input Delay** and **Protocol Latency**. It enables you to quickly identify users with poor experience and lets you drill down into the details to understand the root cause.

- **Protocol Latency**: Measures network-related delay in remoting protocols like ICA or RDP.
- **User Input Delay**: Captures the time between user input (e.g. keypress) and the moment it is picked up by the application — a direct indicator of system/app responsiveness.

<img src="/screenshots/session_delay.png" width="400"/> <img src="/screenshots/machine_compute.png" width="400"/> <img src="/screenshots/app_compute.png" width="400"/> <img src="/screenshots/app_networking.png" width="400"/>

*Click a screenshot to enlarge.*

### 🚀 Desktop Transformation - Persona Mapping

This dashboard provides a comprehensive overview of application inventory, usage, and performance — essential data for planning and executing desktop transformation initiatives.

Instead of assigning all users full personal virtual machines, we can use this data to:

- Identify which apps are actually used
- Understand the performance impact of those apps
- Group users with similar needs
- Deliver more cost-effective, tailored desktop experiences
- Shows which users can be equipped with a browser, only

> This dashboard helps you match application needs to user personas, and transition from "one size fits all" desktops to right-sized solutions.

<img src="/screenshots/app_inventory.png" width="400"/> <img src="/screenshots/app_usage.png" width="400"/> <img src="/screenshots/browser_usage.png" width="400"/>

*Click a screenshot to enlarge.*

## ⚙️ Installation

### Requirements

<details>
   <summary>Click to expand</summary>

- An Azure subscription
- A valid uberAgent license. See the [uberAgent licensing page](https://docs.citrix.com/en-us/licensing/uberagent-licensing-guide) for more information.
- uberAgent endpoint version 7.4.0 or later. Earlier versions do not have the `AppNameIsAppId` config flag to force sending full app names.
- Grafana
  - Version 11.6.0 or later
  - [Azure Data Explorer Datasource](https://grafana.com/grafana/plugins/grafana-azure-data-explorer-datasource/) 6.0.0 or later
- Tested with
  - Grafana OSS deployed with Docker
    - 11.6.0 ✅
    - 11.6.1 ✅
  - Grafana OSS native install ❌
  - Grafana Cloud ✅
  - Azure Managed Grafana ❌

</details>

### uberAgent

<details>
   <summary>Click to expand</summary>

- Install the endpoint agent according to the [uberAgent installation guide](https://docs.citrix.com/en-us/uberagent/current-release/installation/installing-uberagent).
- Install the browser extensions according to the [uberAgent Browser extension installation guide](https://docs.citrix.com/en-us/uberagent/current-release/installation/installing-uberagent). This is required for Browser usage data to be sent to Azure.
- Set up [Azure Monitor](https://docs.citrix.com/en-us/uberagent/current-release/installation/backend/configuring-microsoft-azure-oms-log-analytics) or [Azure Data Explorer](https://docs.citrix.com/en-us/uberagent/current-release/installation/backend/configuring-microsoft-azure-data-explorer-adx-event-hubs) as described in the respective docs.

In the ``uberAgent.conf`` file, set the config flag `AppNameIsAppId` to force sending full app names.

```ini
[Miscellaneous]
ConfigFlags = AppNameIsAppId
```

</details>

### Grafana

<details>
   <summary>Click to expand</summary>

Grafana comes in three different flavors: open-source (OSS), Enterprise, and Cloud. Or, you can use an [Azure managed Grafana](https://learn.microsoft.com/en-us/azure/managed-grafana/overview) instance. The dashboards in this repository should work with all flavors, but not all are tested, yet.

#### Grafana Cloud

The fastest way to get started is with the [Grafana Cloud free tier](https://grafana.com/auth/sign-up/create-user).

#### Grafana self-hosted

<details>
   <summary>Click to expand</summary>

To set up Grafana OSS with Docker, check the [Grafana Docker documentation](https://grafana.com/docs/grafana/latest/setup-grafana/installation/docker/) or follow the steps below.

Create the following directory structure:

```bash
mkdir -p /opt/compose/grafana/data
mkdir -p /opt/compose/grafana/config
touch /opt/compose/grafana/config/grafana.ini
chown -Rfv 472:472 /opt/compose/grafana/data/
chown 472:472 /opt/compose/grafana/config/grafana.ini
```

Create the `compose.yml` file in `/opt/compose/grafana`:

```yaml
# /opt/compose/grafana/compose.yml
services:
  grafana:
    image: grafana/grafana-oss:latest
    container_name: grafana
    restart: unless-stopped
    ports:
     - '3000:3000'
    environment:
      - GF_PLUGINS_PREINSTALL=grafana-azure-data-explorer-datasource
    volumes:
      - /etc/localtime:/etc/localtime:ro
      - ./config/grafana.ini:/etc/grafana/grafana.ini:ro
      - ./data:/var/lib/grafana
```

> The above YAML file references the open-source (OSS) image of Grafana. To use the enterprise image instead, replace grafana/grafana-oss:latest with grafana/grafana-enterprise:latest

Start the container:

```bash
cd /opt/compose/grafana
docker compose up -d
```

Your Grafana instance should now be running on port ``3000``. You can access it by navigating to `http://<your-server-ip>:3000` in your web browser. Login with the default credentials ``admin:admin`` and change the password when prompted.

</details>

#### Azure connection

Both Azure Monitor and Azure Data Explorer can be used as data sources for these dashboards. Here's a quick comparison to help you choose:

| Feature              | Azure Monitor                      | Azure Data Explorer                 |
|----------------------|------------------------------------|-------------------------------------|
| **Primary Use Case** | Monitoring and alerting            | Advanced analytics and querying     |
| **Data Retention**   | Limited (default 30 days)          | Long-term storage                   |
| **Query Language**   | KQL                                | KQL                                 |
| **Performance**      | Optimized for real-time monitoring | Optimized for large-scale analytics |
| **Integration**      | Built-in with Azure services       | Requires Azure Event Hub            |

Go to `Configuration > Data Sources` and add a new data source. Select either **Azure Monitor** or **Azure Data Explorer** as the data source type.

- For **Azure Monitor**, follow the [Azure Monitor data source documentation](https://grafana.com/docs/grafana/latest/datasources/azure-monitor/).
- For **Azure Data Explorer**, follow the [Azure Data Explorer plugin documentation](https://grafana.com/grafana/plugins/grafana-azure-data-explorer-datasource/).

#### Dashboard installation

- Download the JSON files for your preferred backend (Azure Monitor or Azure Data Explorer) from the releases page.
- Go to `Dashboards > Manage` and click on `Import`.
- For each JSON file
  - Copy the downloaded JSON files and paste it into the import dialog. Alternatively, you can upload the JSON file directly.
  - Select the data source you created earlier (Azure Monitor or Azure Data Explorer) and click `Import`.

</details>

## 🚧 Limitations

- The dashboards are designed to provide a quick and easy way to visualize select use-cases without the need for Splunk. Not all metrics that uberAgent collects are included in the dashboards.
- The only available dashboard filters are `User`, `Machine`, and `App`. Filtering in Splunk is much more advanced. This is a limitation of the Azure Monitor and Azure Data Explorer data sources, not Grafana.
- Input delay is provided by the Windows operating system and is not available for Linux or macOS machines. Other metrics like protocol latency, CPU load, and memory usage are available for all platforms.

## 🗺️ Roadmap

- Test more Grafana flavors (Azure Managed Grafana, etc.)
- Add more use-cases and dashboards
- Create dashboards as code with the [grafana-foundation-sdk](https://github.com/grafana/grafana-foundation-sdk) introduced in Grafana 12, instead of editing in the browser. This paves the way to support Elasticsearch as data source, too.
- Package as app for easier installation and updates

## 🤝 Contributing

- Please check the `CONTRIBUTING.md` file for guidelines on how to contribute to this project.
