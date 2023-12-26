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
        "stasiun1": "password1",
        "stasiun2": "password2",
        "stasiun3": "password3",
    }

    print("Selamat datang Admin!")
    station_code = input("Masukkan stasiun: ")

    if station_code in station_master_credentials:
        password = input("Masukkan password: ")
        if password == station_master_credentials[station_code]:
            print("Login berhasil!")

            while True:
                choice = input(
                    "\nMasukkan 1 untuk update jadwal kereta di stasiun anda dan\nMasukkan 2 untuk update posisi kereta?\nMasukkan lainnya untuk keluar\n"
                ).lower()
                if choice == "1":
                    train = input("\nMasukkan nama kereta: ")
                    train_topic = f"jadwal_kereta/{train}"
                    waktu_kedatangan = input("Masukkan waktu kedatangan: ")
                    waktu_keberangkatan = input("Masukkan waktu keberangkatan: ")
                    jadwal = f"Kereta : {train}\nStasiun : {station_code}\nWaktu Keberangkatan : {waktu_keberangkatan}\nWaktu Kedatangan : {waktu_kedatangan}\n "
                    publish_schedule(train_topic, jadwal)
                elif choice == "2":
                    train = input("\nMasukkan nama kereta : ")
                    posisi_topic = f"posisi_kereta/{train}"
                    posisi = input("Masukkan posisi kereta : ")
                    posisi_kereta = f"Kereta : {train}\nPosisi Terakhir : {posisi}\n"
                    publish_schedule(posisi_topic, posisi_kereta)
                else:
                    print("Sampai Jumpa!")
                    break
        else:
            print("Invalid password. Please try again.")
    else:
        print("Station code not found.")


if __name__ == "__main__":
    station_master_ui()
