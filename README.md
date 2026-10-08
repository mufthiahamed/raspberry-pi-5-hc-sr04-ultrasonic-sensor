# HC-SR04 Ultrasonic Sensor with Raspberry Pi 5

This project measures distance using an HC-SR04 ultrasonic sensor connected to a Raspberry Pi 5.

## Wiring

| HC-SR04 | Raspberry Pi |
|---|---|
| VCC | 5V |
| TRIG | GPIO16 |
| ECHO | GPIO21 through voltage divider |
| GND | GND |

## Voltage Divider

The HC-SR04 ECHO pin outputs approximately 5V.

The Raspberry Pi GPIO accepts 3.3V, so a voltage divider is used:

- 1 kΩ resistor between ECHO and GPIO21
- 2.2 kΩ resistor between GPIO21 and GND

## Breadboard Layout

- SENSOR CONNECTION ON BREADBOARD
- A1 = VCC
- A2 = ECHO
- A3 = TRIG
- A4 = GND

- RESISTOR CONNECTION ON BREADBAORD
- B2 to B7 = 1 kΩ resistor
- C7 to C11 = 2.2 kΩ resistor

- WIRING
- A7 = GPIO21
- A11 = GND
- E1 = 5V
- E3 = GPIO16
- E4 = GND

## Run

```bash
python3 ultrasonic_sensor.py
