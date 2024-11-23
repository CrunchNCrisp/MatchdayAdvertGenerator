import yaml

from calendar_service import fetch_calendar_data, get_next_event


def read_config(config_path='config.yml'):
    """Reads the configuration file."""
    try:
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)
    except Exception as e:
        print(f"Error reading config file: {e}")
        exit(1)


def main():
    # Load the API URL from the configuration file
    config = read_config()

    api_url = config.get("calendar_api_url")
    if not api_url:
        print("Calendar API URL not found in config file.")
        exit(1)

    print(api_url)

    # Fetch and process the calendar data
    calendar_data = fetch_calendar_data(api_url)
    print(calendar_data)
    next_event = get_next_event(calendar_data)

    if next_event:
        print("Next Event:")
        print(f"Summary: {next_event.name}")
        print(f"Start: {next_event.begin}")
        print(f"End: {next_event.end}")
        print(f"Description: {next_event.description}")
        print(f"Location: {next_event.location}")
    else:
        print("No upcoming events found.")


if __name__ == "__main__":
    main()
