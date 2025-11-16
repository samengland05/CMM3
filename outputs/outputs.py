print("This plots a graph of displacement against k to guess the values for optimal k")

#This creates a range of k values to plot

k_values_plot = np.linspace(500, 10000, 100) 


# We use objective(k) which returns (deflection - 0.05)
objective_values = []
for k_val in k_values_plot:
    print(f"Plotting: Trying k={k_val:.0f}")
    objective_values.append(objective(k_val))

#Create the plot
plt.figure(figsize=(10, 6))
plt.plot(k_values_plot, objective_values, 'y-', label="c=3000")

# Add the target line (where objective = 0)
plt.axhline(y=0.0, color='r', linestyle='--', 
            label='Target = Maximum deflection is 0.025m ')

#Add labels and title
plt.xlabel('Spring Stiffness $k$ (N/m)')
plt.ylabel('Suspension deflection - 0.025 (m)')
plt.title('Suspension Deflection vs. Stiffness')
plt.legend()
plt.grid(True)
plt.savefig('rootfinding_plot.png')

print("Look at this plot to find where the blue line intersects the red line.")
print("Use k-values on either side of that crossing as your new k0 and k1.")
