# Mars Suspension System Simulation - README
Project files : 

- Coding script :
1. Loads and fits the raw terrain data using polynomial interpolation
2. Defines the suspension model
3. Solves the motion using RK4 method
4. Solves root-finding using the Secant method
5. Generates plots and outputs the optimal stiffness value

- gale_terrain_synthetic.csv
  A synthetic but realistic terrain profile representing the elevation patterns in Gale Crater, Mars. It follows the typical roughness and slopes patterns from NASA, MOLA and HiRISE terrain maps. The file was generated to be easier to use for numerical modelling.

How to run the code : 
1. Install python packages (external functions) :
   
   pip install numpy pandas matplotlib
3. Place files in the same folder:

   folder : Mars suspension system simulation, gale_terrain_synthetic.csv
5. Run the code

Where the three required numerical methods are implemented : 
1. Regression/Interpolation (polynomial approximation of terrain)

   Location : top of the coding script
   
   poly_coeff = np.polyfit(time_values, height_values, poly_order)

   z_r = np.poly1d(poly_coeff)

   Objective : Convert the raw terrain data into a smooth, differentiable function z(t) to be used as the suspension input. 
3. ODE-Solving (Runge-Kutta 4th Order)

   Location : mid of the coding script

   
5. Root-finding (Secant method)

   
