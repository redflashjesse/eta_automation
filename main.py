# import the necessary parts from the other files
import eta_data_collection
import eta_visualizer

def main():
# defiine what to do
datacollection = True # True or False
dataanalysis = False # True or False
# starting the loop funktion for the data collection
if datacollection == True:
    if __name__ == '__main__':
        eta_data_collection.main()
else:
    pass
# starting the visualizer for plotly diagrams
if dataanalysis == True:
    eta_visualizer.app.run(debug=True)
else:
    pass

    # starting the loop funktion for the data collection
    eta_data_collection.loop_longtime_writing_csv()


if __name__ == "__main__":
    # Call main() function
    main()
