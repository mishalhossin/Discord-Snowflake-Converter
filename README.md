# Discord Snowflake to Timestamp Converter

This Python script provides a simple and efficient way to convert Discord Snowflake IDs into human-readable timestamps. Discord Snowflakes are unique identifiers used by Discord to track and identify various entities such as users, channels, and messages. Converting Snowflakes to timestamps can be helpful for analyzing time-related information within the Discord ecosystem.

## Features

- Converts Discord Snowflake IDs to timestamps using Discord's epoch (or a custom epoch if provided).
- Validates the Snowflake ID format and size before conversion.
- Returns a `datetime.datetime` object representing the corresponding timestamp.

## Usage

```bash
python converter.py
```

The script will prompt you to enter a Snowflake ID. After entering the ID, it will validate the input and display the corresponding timestamp if the Snowflake ID is valid. If the Snowflake ID is invalid, it will provide an error message indicating the reason for the validation failure.

## Acknowledgments

The script is inspired by the Discord Snowflake specification and the original JavaScript implementation by [vegeta897](https://github.com/vegeta897/snow-stamp)

## References

- Discord API Documentation: [Snowflakes](https://discord.com/developers/docs/reference#snowflakes)
- Discord API Documentation: [Epoch and Timestamps](https://discord.com/developers/docs/reference#snowflake-ids-in-pagination)
