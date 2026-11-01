# StellarMetrics: Astrophysics Data-Processor & H-R Graph Generator

# What is Stellarmetrics?
Stellarmetrics is a pipeline built in Python made in order to take in astronomical data from telescopes, clean them up, and graph the cleaned up data on a Hertzburg-Russell Diagram. Stellarmetrics utilizes a physics engine I've created to calculate stellar properties, such as a star's surface temperature, radius, absolute magnitude, and luminosity. This data is used to generate the H-R Graph. Currently, Gaia, Kepler, and HYG data are all used to create the graphs, although it would be relatively easy to incorporate data from other telescopes into this code (more on that later).



# Project Features
- Universal Catalog: Any data ingested into the program gets re-catagorized under universal headers, making calculations and graphing seamless.
- Astronomical Physics Engine: Physics Engine capable of running astronoomical equations using numpy
- Data Cleanser: Filters errors in data, such as missing values and calculation uncertainties, automatically. Essentially cleans up and fixes the data from its raw form.
- Plotter Function: Automatically plots the an H-R Diagram using matplotlib. Plots and saves data for each set of telescope data serperately.
- Function Testers: Project passes all testing functions that I've created. Tester functions primarily focused on the physics module and data inerpretation module, since those were the functions were mistakes could easily occur.

# Project Structure
Stellarmetrics/
    data/            #Telescope datasets (Gaia, Kepler, and HYG)
    stellarmetrics/  #Main file for all project functions and some documentation (notes and logs written during the coding process)
        main.py      # Main function pipeline. All created functions and coding passes through here to make the project run smoothly. User inputs are also collected in here.
        data_setup.py.  #Grabs a sample set of data from telescope data (Kepler, Gaia, and HYG respetively), saving them to their own respective data files used to perform calculations (using the entire data set via a url would be subject to a plethora of bugs and could easily break; this method makes the project simpler and more efficient).
        mapper.py.    #Changes the headers of all telescope data from the headers provided by their respective telescopes to a universal header. This way, calculations are seamless across each source of data.
        data_interpreter.py   #Cleans up all inputed data after the data is relabled under the universal header using pandas.
        physics.py.  # All physics functions and math are run through here. Gathers the cleaned up data (cleaned up by data_interpreter.py). Uses pandas and numpy for calculations.
        test_data_interpreter.py   # thoroughly tests the data_interpreter function to ensure all data is properly cleaned up and processed.
        test_physics.py.    #tests equations and calculations to ensure that data is being properly calculated and processed.
        notes.md    #Notes and logs taken throughout the coding process, detailing the entire journey of the project
    README.md       #General project information presentation and documentation


# Physics Equations
The pride of Stellarmetrics is by far the physics module. This project executes 3 primary equations in order to calculate astrophysical data:

1. Surface Temperature Calculation - calculates the surface temperature of a star with Ballesteros Formula using the B-V color index:
T = 4600((1/0.92(B-V) + 1.7) + (1/0.92(B-V) + 0.62))

2. Absolute Magnitude and Parallax Distance Calculations - first converts parallax archsecond to parsecs (d = 1/p), then evaluates absolute magnitude:
M = m - 5(log10(d) - 1)

3. Luminosity and Radius Calculations: Calculates the luminosty and radius of a star in order to first convert to solar units, then find a star's radius which can help determine the part of a star's lifecycle a star is in.
L = 10^0.4(Mx-M)

R = L^1/2 (Tx/T)^2

# Prerequisites
Ensure Python 3.9+ is installed, as well as the following python libraries: numpy, matplotlib, pytest, and pandas. To install, run:
pip install numpy matplotlib pytest pandas

# How to run
run the following in your terminal window:

cd stellarmetrics
python main.py

From their, select the telescope data you want to analyze (1 is Kepler, 2 is Gaia, 3 is HYG)
When the png file pops up under the stellarmetrics file, click on it to observe the H-R diagram.


# Important Notes
This project is not hardwired to only produce HYG, Gaia, and Kepler graphs. In fact, I've made it so that it can take the data from any telescope, clean it up, run calculations, and graph the data on an H-R diagram. To do so, the programmer would simply need to add their desired telescope data into data_setup.py, and create a sample file of it. From their, they would need to head into maper.py and create a small convertor dictionary for their respective data sets, as I have done for Kepler, Gaia, and HYG. I am a relatively beginner programmer, and thus it isn't perfect, but I tried to make it as easy to use and add onto as possible with my limited programming knowledge. From their, they would add their converted data set dictionary to the MAPS dictionary and name their data set as I have done for the three used in this project. 
I've had a great time creating Stellarmetrics, and I hope to create more complex and innovative projects in the future!

