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
    print(f"Menerima topic {message.topic}: {message.payload.decode()}")


def subscribe_to_station(jadwal_topic, posisi_topic):
    client = mqtt.Client()

    try:
        client.connect(broker_address, port)
        client.on_message = on_message
        client.subscribe([(jadwal_topic, 1), (posisi_topic, 1)])
        client.loop_start()

        while not exit_flag:
            time.sleep(1)

    except Exception as e:
        print(f"MQTT Error: {e}")

    finally:
        client.loop_stop()


def passenger_ui():
    print("Selamat datang, penumpang!")
    print("Jadwal kereta apa yang mau kamu lihat?")

    train_choice = input("Masukkan nama kereta: ")
    jadwal_topic = f"jadwal_kereta/{train_choice}"
    posisi_topic = f"posisi_kereta/{train_choice}"

    print("\nTekan CTRL + C untuk keluar\n")

    try:
        subscribe_to_station(jadwal_topic, posisi_topic)
    except KeyboardInterrupt:
        print("\nExiting...")


if __name__ == "__main__":
    try:
        passenger_ui()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        exit_flag = True
