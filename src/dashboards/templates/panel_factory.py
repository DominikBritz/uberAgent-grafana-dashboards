from grafana_foundation_sdk.builders import (
    timeseries,
    common as common_builder,
    azuremonitor,
)
from grafana_foundation_sdk.models import common


def azuremonitor_logs_query(query: str) -> azuremonitor.AzureLogsQuery:
    return azuremonitor.AzureLogsQuery().query(query)


def default_timeseries() -> timeseries.Panel:
    return (
        timeseries.Panel()
        .height(7)
        .span(12)
        .line_width(1)
        .fill_opacity(0)
        .point_size(5)
        .show_points(common.VisibilityMode.AUTO)
        .draw_style(common.GraphDrawStyle.LINE)
        .gradient_mode(common.GraphGradientMode.NONE)
        .span_nulls(False)
        .axis_border_show(False)
        .legend(
            common_builder.VizLegendOptions()
            .display_mode(common.LegendDisplayMode.LIST)
            .placement(common.LegendPlacement.BOTTOM)
            .show_legend(True)
        )
        .tooltip(
            common_builder.VizTooltipOptions()
            .mode(common.TooltipDisplayMode.SINGLE)
            .sort(common.SortOrder.NONE)
        )
        .thresholds_style(
            common_builder.GraphThresholdsStyleConfig().mode(
                common.GraphThresholdsStyleMode.OFF
            )
        )
    )