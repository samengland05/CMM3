print("This plots a graph of displacement against k to guess the values for optimal k")

#This creates a range of k values to plot

k_values_plot = np.linspace(500, 40000, 100) 


# We use objective(k) which returns (deflection - 0.05)
objective_values = []
for k_val in k_values_plot:
    print(f"Plotting: Trying k={k_val:.0f}")
    objective_values.append(objective(k_val))

#Create the plot
plt.figure(figsize=(10, 6))
plt.plot(k_values_plot, objective_values, 'b-', label='objective(k) [Max Deflection - 0.05 m]')

# Add the target line (where objective = 0)
plt.axhline(y=0.0, color='r', linestyle='--', 
            label='Target (objective = 0)')

#Add labels and title
plt.xlabel('Spring Stiffness $k$ (N/m)')
plt.ylabel('Objective Function Output')
plt.title('Objective Function vs. Stiffness')
plt.legend()
plt.grid(True)
plt.savefig('objective_function_plot.png')

print("Plot 'objective_function_plot.png' saved.")
print("Look at this plot to find where the blue line crosses the red line.")
print("Use k-values on either side of that crossing as your new k0 and k1.")
