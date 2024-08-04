def is_running_in_databricks():
    try:
        # Check if the Databricks-specific library is available
        import databricks.koalas
        return True
    except ImportError:
        return False

# Example usage
if is_running_in_databricks():
    print("Running in Databricks environment")
else:
    print("Not running in Databricks environment")
