import random
import time

def monitor_temperature():
    print("--- IoT Temperature Monitor System ---")
    
    # 1. Accept max and min limit temperature from user
    try:
        min_limit = float(input("Enter the MINIMUM temperature limit: "))
        max_limit = float(input("Enter the MAXIMUM temperature limit: "))
    except ValueError:
        print("Invalid input. Please enter numerical values.")
        return

    print(f"\nMonitoring started... (Limits: {min_limit}°C - {max_limit}°C)")
    print("Press Ctrl+C to stop.\n")

    try:
        while True:
            # 2. Generate random values for temperature
            # Simulating a range between 0 and 50 for variety
            current_temp = round(random.uniform(0.0, 50.0), 2)
            
            # 3. Compare with the limits to display appropriate value
            status = ""
            if current_temp > max_limit:
                status = "⚠️ ALERT: Temperature too high!"
            elif current_temp < min_limit:
                status = "❄️ ALERT: Temperature too low!"
            else:
                status = "✅ Temperature Normal"

            print(f"Current Temp: {current_temp}°C | {status}")

            # 4. 2-second interval
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user. Goodbye!")

if __name__ == "__main__":
    monitor_temperature()
