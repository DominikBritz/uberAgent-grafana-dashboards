from grafana_foundation_sdk.builders import dashboard
from grafana_foundation_sdk.models.dashboard import VariableOption

def textbox_variable(name: str, label: str, description: str = "", default: str = "") -> dashboard.TextBoxVariable:
    """Create a textbox variable for filtering."""
    return (
        dashboard.TextBoxVariable(name)
        .label(label)
        .description(description)
        .default_value(default)
    )

def custom_variable(name: str, label: str, options: list[str], default: str = "") -> dashboard.CustomVariable:
    """Create a custom variable with predefined options."""
    var = (
        dashboard.CustomVariable(name)
        .label(label)
        .multi(False)
        .values(",".join(options))
    )
    # Set current value if default is provided
    if default:
        var = var.current(VariableOption(text=default, value=default, selected=True))
    return var

def datasource_variable(name: str, label: str, datasource_type: str) -> dashboard.DatasourceVariable:
    """Create a datasource variable."""
    return (
        dashboard.DatasourceVariable(name)
        .label(label)
        .type(datasource_type)
        .multi(False)
    )

