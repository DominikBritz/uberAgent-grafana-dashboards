from grafana_foundation_sdk.builders import (
    timeseries,
    text,
    table,
    dashboard,
    common as common_builder,
    azuremonitor,
)
from grafana_foundation_sdk.models import common


def azuremonitor_logs_query(query: str) -> azuremonitor.AzureLogsQuery:
    return (
        azuremonitor.AzureLogsQuery()
        .query(query)
        .dashboard_time(False)
        .result_format("logs")
        .time_column("TimeGenerated")
    )



def default_timeseries() -> timeseries.Panel:
    return (
        timeseries.Panel()
        .height(7)
        .span(12)
        .line_width(1)
        .fill_opacity(0)
        .point_size(5)
        .min(0)
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


def text_panel(content: str, mode: str = "markdown") -> text.Panel:
    """Create a text panel with markdown or plaintext content."""
    return (
        text.Panel()
        .height(20)
        .span(24)
        .code(
            text.CodeOptions()
            .language("plaintext" if mode == "plaintext" else "markdown")
            .show_line_numbers(False)
            .show_mini_map(False)
        )
        .content(content)
        .mode(mode)
    )


def default_table() -> table.Panel:
    """Create a default table panel."""
    return (
        table.Panel()
        .height(10)
        .span(24)
        .options(
            table.TableOptions()
            .cell_height("sm")
            .show_header(True)
            .footer(
                table.TableFooterOptions()
                .count_rows(False)
                .show(False)
            )
        )
    )


def row_panel(title: str, collapsed: bool = True) -> dashboard.Row:
    """Create a row panel for grouping other panels."""
    return (
        dashboard.Row(title)
        .collapsed(collapsed)
    )