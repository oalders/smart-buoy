# Get MQTT details and more from a secrets.py file
try:
    from secrets import secrets
except ImportError:
    print("MQTT secrets are kept in secrets.py, please add them there!")
    raise

# Import library and create instance of REST client.
from Adafruit_IO import Client
aio = Client(secrets["aio_username"], secrets["aio_key"])

# Send the value 100 to a feed called 'Foo'.
aio.send('welcome-feed', 100)

# Retrieve the most recent value from the feed 'Foo'.
# Access the value by reading the `value` property on the returned Data object.
# Note that all values retrieved from IO are strings so you might need to convert
# them to an int or numeric type if you expect a number.
data = aio.receive('welcome-feed')
print('Received value: {0}'.format(data.value))
