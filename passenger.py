import paho.mqtt.client as mqtt
import keyboard
import time

from pynput.keyboard import Listener

# MQTT Broker details
broker_address = "192.168.1.5"
port = 1883

# Flag to control the loop
exit_flag = False

def on_message(client, userdata, message):
    print(f"Received schedule for {message.topic}: {message.payload.decode()}")

def subscribe_to_station(station_topic):
    client = mqtt.Client()

    try:
        client.connect(broker_address, port)
        client.on_message = on_message
        client.subscribe(station_topic)
        client.loop_start()

        while not exit_flag:
            time.sleep(1)

    except Exception as e:
        print(f"MQTT Error: {e}")

    finally:
        client.loop_stop()

def passenger_ui():
    print("Welcome, Passenger!")
    print("Available stations: station1, station2, station3")

    station_choice = input("Enter station code to view schedule: ")
    station_topic = f"stations/{station_choice}"

    print("Press ctrl+c if you want to exit")
    print(f"Subscribed to {station_choice} station schedule...")

    try:
        subscribe_to_station(station_topic)
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    try:
        passenger_ui()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        exit_flag = True
