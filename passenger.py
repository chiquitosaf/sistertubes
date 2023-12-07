import paho.mqtt.client as mqtt

# MQTT Broker details
broker_address = "127.0.0.1"
port = 9000

def subscribe_to_station(station_topic):
    def on_message(client, userdata, message):
        print(f"Received schedule for {station_topic}: {message.payload.decode()}")

    client = mqtt.Client()
    client.connect(broker_address, port)
    client.on_message = on_message
    client.subscribe(station_topic)
    client.loop_forever()

def passenger_ui():
    print("Welcome, Passenger!")
    print("Available stations: station1, station2, station3")

    station_choice = input("Enter station code to view schedule: ")
    station_topic = f"stations/{station_choice}"

    print(f"Subscribed to {station_choice} station schedule...")
    subscribe_to_station(station_topic)

if __name__ == "__main__":
    passenger_ui()
