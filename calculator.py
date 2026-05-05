import math

def roller_speed(diameter_mm, rpm):
    diameter_m = diameter_mm / 1000
    speed = math.pi * diameter_m * rpm / 60
    return speed

def capacity(width_mm, speed):
    width_m = width_mm / 1000
    return width_m * speed * 60 * 0.6

def motor_power(capacity):
    return capacity * 0.75

if __name__ == "__main__":
    print("=== Crusher Tool ===")
    
    d = float(input("Diameter (mm): "))
    rpm = float(input("Speed (rpm): "))
    width = float(input("Width (mm): "))
    
    v = roller_speed(d, rpm)
    q = capacity(width, v)
    p = motor_power(q)
    
    print(f"Speed: {v:.2f} m/s")
    print(f"Capacity: {q:.2f} t/h")
    print(f"Power: {p:.2f} kW")
