# data plot against polynomial
# dnese time axis to smoothen curve 
t_plot = np.linspace(time_values.min(), time_values.max(), 800)

plt.figure(figsize=(8,4))
plt.scatter(time_values, height_values, s=12, color="black", label="Recorded data")
plt.plot(t_plot, z_r(t_plot), "r-", lw=1.8, label=f"Polynomial line (deg={poly_order})")
plt.xlabel("Time [s]")
plt.ylabel("Height [m]")
plt.title("Polynomial Curve of Mars Terrain z_r(t)")
plt.grid(True, ls="--", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()
