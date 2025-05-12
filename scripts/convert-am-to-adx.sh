#!/usr/bin/env bash
set -euo pipefail

if [ $# -ne 2 ]; then
  echo "Usage: $0 <input_json> <output_json>"
  exit 1
fi

input="$1"
output="$2"


jq '
  # 1) Update the first __inputs entry
  (.["__inputs"][0].name       = "DS_GRAFANA-AZURE-DATA-EXPLORER-DATASOURCE") |
  (.["__inputs"][0].label      = "grafana-azure-data-explorer-datasource") |
  (.["__inputs"][0].pluginId   = "grafana-azure-data-explorer-datasource") |
  (.["__inputs"][0].pluginName = "Azure Data Explorer Datasource") |

  # 2) Update the __requires entry
  ( .["__requires"][]
    | select(.type=="datasource" and .id=="grafana-azure-monitor-datasource")
  ) |= (
    .id      = "grafana-azure-data-explorer-datasource" |
    .name    = "Azure Data Explorer Datasource"       |
    .version = "6.0.0"
  ) |

  # 3) Change every datasource.type across the JSON
  (.. | objects | select(.type=="grafana-azure-monitor-datasource") | .type)
    |= "grafana-azure-data-explorer-datasource" |

  # 3b) Change every datasource.uid across the JSON
  (.. | objects | select(.uid=="${DS_GRAFANA-AZURE-MONITOR-DATASOURCE}") | .uid)
    |= "${DS_GRAFANA-AZURE-DATA-EXPLORER-DATASOURCE}" |

  # 4) Rewrite all panels’ targets from AzureLogAnalytics → ADX-style
  (.. | objects | select(has("targets")) | .targets) |= (
    map(
      if has("azureLogAnalytics") then
        {
          OpenAI:      false,
          clusterUri:  "$cluster",
          database:    "$database",
          datasource: {
            type: "grafana-azure-data-explorer-datasource",
            uid:  "${DS_GRAFANA-AZURE-DATA-EXPLORER-DATASOURCE}"
          },
          expression: {
            groupBy: { expressions: [], type: "and" },
            reduce:  { expressions: [], type: "and" },
            where:   { expressions: [], type: "and" }
          },
          pluginVersion: "6.0.0",
          query:         .azureLogAnalytics.query,
          querySource:   "raw",
          queryType:     "KQL",
          rawMode:       true,
          refId:         .refId,
          resultFormat:  "table"
        }
      else
        .
      end
    )
  ) |

  # 5) Templating: replace any .query == old-datasource
  (.. | objects | select(.query=="grafana-azure-monitor-datasource") | .query)
    |= "grafana-azure-data-explorer-datasource" |

  # 6) Remove subscription, resource_group & workspace
  .templating.list |= map(
    select(.name!="subscription" and .name!="resource_group" and .name!="workspace")
  ) |

  # 7) Insert Cluster & Database entries after “datasource”
  .templating.list |= (
    . as $l
    | ($l|map(.name)|index("datasource")) as $i
    | $l[0:$i+1]
      + [
          {
            "allowCustomValue": false,
            "current": {},
            "datasource": {
              "type": "grafana-azure-data-explorer-datasource",
              "uid": "${datasource}"
            },
            "definition": "",
            "label": "Cluster",
            "name": "cluster",
            "options": [],
            "query": {
              "azureLogAnalytics": { "query": "", "resources": [] },
              "clusterUri": "",
              "database": "",
              "queryType": "Clusters",
              "refId": "A",
              "subscription": ""
            },
            "refresh": 1,
            "regex": "",
            "type": "query"
          },
          {
            "allowCustomValue": false,
            "current": {},
            "datasource": {
              "type": "grafana-azure-data-explorer-datasource",
              "uid": "${datasource}"
            },
            "definition": "",
            "label": "Database",
            "name": "database",
            "options": [],
            "query": {
              "azureLogAnalytics": { "query": "", "resources": [] },
              "clusterUri": "$cluster",
              "database": "",
              "queryType": "Databases",
              "refId": "A",
              "subscription": ""
            },
            "refresh": 1,
            "regex": "",
            "sort": 1,
            "type": "query"
          }
        ]
      + $l[$i+1:]
  ) |

  # 8) Clean up all query strings:
  #    • strip "uberAgent_", "_CL", trailing "_<letter>"
  #    • rename TimeGenerated→Timestamp
  #    • rename Computer→Host when not preceded by "$"
  (.. | objects | select(has("query") and (.query|type=="string")) | .query)
    |= (
      gsub("uberAgent_"; "")       |
      gsub("_CL"; "")              |
      gsub("_[A-Za-z]\\b"; "")     |
      gsub("TimeGenerated"; "Timestamp") |
      gsub("(?<!\\$)Computer"; "Host")
    ) |

  # 9) Update root-level tags:
  #     remove "Azure Monitor", then add "Azure Data Explorer"
  .tags |= (map(select(. != "Azure Monitor")) + ["Azure Data Explorer"])
' "$input" > "$output"
