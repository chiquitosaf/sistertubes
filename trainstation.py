import paho.mqtt.client as mqtt

# MQTT Broker details
broker_address = "192.168.1.5"
port = 1883

def publish_schedule(station_topic, schedule):
    client = mqtt.Client()
    client.connect(broker_address, port)
    client.publish(station_topic, schedule, qos=1, retain=True)
    client.disconnect()

def station_master_ui():
    station_master_credentials = {
        "station1": "password1",
        "station2": "password2",
        "station3": "password3"
    }

    print("Welcome, Train Station Master!")
    station_code = input("Enter your station code: ")

    if station_code in station_master_credentials:
        password = input("Enter your password: ")
        if password == station_master_credentials[station_code]:
            print("Login successful!")

            while True:
                choice = input("Do you want to publish a schedule? (Y/N): ").lower()
                if choice == 'y':
                    station_topic = f"stations/{station_code}"
                    schedule = input("Enter train schedule (train name, code, stop time, departure time): ")
                    publish_schedule(station_topic, schedule)
                elif choice == 'n':
                    print("Exiting the application. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please enter Y or N.")
        else:
            print("Invalid password. Please try again.")
    else:
        print("Station code not found.")

if __name__ == "__main__":
    station_master_ui()
