import numpy as np
import matplotlib.pyplot as plt

def create_sinusoidal_plot():
    # Generate x values from 0 to 4π
    x = np.linspace(0, 4 * np.pi, 1000)
    
    # Calculate y values for sin(x)
    y = np.sin(x)
    
    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-', linewidth=2, label='sin(x)')
    
    # Add grid and labels
    plt.grid(True, alpha=0.3)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.title('Sinusoidal Function: y = sin(x)', fontsize=14)
    plt.legend()
    
    # Set x-axis ticks to show multiples of π
    pi_ticks = np.arange(0, 4.5 * np.pi, np.pi/2)
    pi_labels = ['0', 'π/2', 'π', '3π/2', '2π', '5π/2', '3π', '7π/2', '4π']
    plt.xticks(pi_ticks, pi_labels)
    
    # Save the plot
    plt.savefig('sinusoidal_plot.png', dpi=100, bbox_inches='tight')
    print("Plot saved as 'sinusoidal_plot.png'")
    
    # Display the plot
    plt.show()

if __name__ == "__main__":
    create_sinusoidal_plot()