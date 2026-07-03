from .device_power import DEVICE_POWER


class LoadCalculator:

    @staticmethod
    def calculate(devices):
        total = 0
        details = []

        for name, quantity in devices:
            watts = DEVICE_POWER.get(name.lower())

            if watts:
                subtotal = watts * quantity
                total += subtotal

                details.append({
                    "device": name,
                    "quantity": quantity,
                    "watts_each": watts,
                    "subtotal": subtotal,
                })

        return {
            "total_watts": total,
            "details": details,
        }