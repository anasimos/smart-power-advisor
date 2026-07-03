import re

KNOWN_DEVICES = [
    "desktop computer",
    "laptop",
    "printer",
    "router",
    "server",
    "monitor",
]


def extract_devices(text):
    devices = []

    for device in KNOWN_DEVICES:
        pattern = rf"(\d+)\s+{device}s?"
        matches = re.findall(pattern, text.lower())

        for quantity in matches:
            devices.append((device, int(quantity)))

    return devices