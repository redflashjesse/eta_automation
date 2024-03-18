# import the necessary parts from the other files
from eta_data_collection import loop_longtime_writing_csv
from eta_visualizer import plot_and_visualize


def main():
    # defiine what to do
    datacollection = True  # True or False
    dataanalysis = False  # True or False

    # starting the loop funktion for the data collection
    if datacollection:
        loop_longtime_writing_csv()

    # starting the visualizer for plotly diagrams
    if dataanalysis:
        plot_and_visualize()


if __name__ == "__main__":
    # Call main() function
    main()
