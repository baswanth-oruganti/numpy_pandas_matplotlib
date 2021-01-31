steps for plotting:
A. Install following python packages:

pip install pandas
pip install matplotlib
pip install seaborn

1. copy the output containing the "OWN BASIS SET" and "ALL BASIS SET" from the GAMES log file to a new file. Repeat this step for the second file
2. As an example, see data1.log and data2.log files in this folder containing results from different Functionals
3. To run the script: 
> python3 my_pie.py data1.log data2.log 
4. "fig1.tiff" will be saved to pwd, four new files will be saved to pwd:own_basis1.csv,own_basis2.csv,all_basis1.csv,all_basis2.csv
