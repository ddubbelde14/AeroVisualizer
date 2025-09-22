import numpy as np
import matplotlib.pyplot as plt
import io
import base64

def simulate_ballistics(v0, angle_deg, h0, g=9.81):
    """
    Simulates projectile motion with initial velocity, angle, and height.
    Returns a base64-encoded PNG of the trajectory.
    """
    # Convert angle to radians
    angle = np.radians(angle_deg)
    
    # Initial velocity components
    vx = v0 * np.cos(angle)
    vy = v0 * np.sin(angle)
    
    # Time of flight (solve quadratic: y = h0 + vy*t - 0.5*g*t^2 = 0)
    t_flight = (vy + np.sqrt(vy**2 + 2*g*h0)) / g
    
    # Time points
    t = np.linspace(0, t_flight, 200)
    
    # Position over time
    x = vx * t
    y = h0 + vy * t - 0.5 * g * t ** 2
    
    # Set totalDistance
    totalDistance = x[-1]
    
    # Plot
    plt.figure()
    plt.plot(x, y)
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.title("Projectile Motion")
    plt.grid(True)
    plt.xlim(0,200)
    plt.ylim(0,100)
    
    # Save to a PNG in memory
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    buf.seek(0)
    
    # Encode PNG as base64 string
    img_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    return img_base64, totalDistance