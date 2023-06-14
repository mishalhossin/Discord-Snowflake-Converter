import datetime

DISCORD_EPOCH = 1420070400000

def convert_snowflake_to_date(snowflake, epoch=DISCORD_EPOCH):
    milliseconds = int(snowflake) >> 22
    return datetime.datetime.fromtimestamp((milliseconds + epoch) / 1000.0)

def validate_snowflake(snowflake, epoch=DISCORD_EPOCH):
    if not snowflake.isdigit():
        raise ValueError("That doesn't look like a snowflake. Snowflakes contain only numbers.")

    if int(snowflake) < 4194304:
        raise ValueError("That doesn't look like a snowflake. Snowflakes are much larger numbers.")

    try:
        timestamp = convert_snowflake_to_date(snowflake, epoch)
        return timestamp
    except ValueError:
        raise ValueError("That doesn't look like a snowflake. Snowflakes have fewer digits.")

snowflake = input("Enter a snowflake ID: ")

try:
    timestamp = validate_snowflake(snowflake)
    print("Timestamp:", timestamp)
except ValueError as e:
    print("Error:", str(e))
