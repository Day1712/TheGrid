from code.classes import district as district_file
from code.visualisation import visualisation
from code.output import output
from code.algorithms import random, hill_climber, simulated_annealing
from code.experiments import experiment_random, experiment_sim_ann, experiment_hill_climb
import argparse

def main(district_number, algorithm, move_batteries, plot, experiment, runs, output):
    if experiment == "no":
        district = district_file.District(district_number)
        random.create_all_routes(district)

        if move_batteries == 'yes':
            move_batteries = True
        else:
            move_batteries = False

        if algorithm == "hill":
            if plot == "live":
                district = hill_climber.hill_climber_algorithm(district, plot = "y", move_batteries = move_batteries)
            elif plot == "static":
                district = hill_climber.hill_climber_algorithm(district, move_batteries = move_batteries)
                visualisation.basic_static_visualise(district)
            elif plot == "battery":
                district = hill_climber.hill_climber_algorithm(district, move_batteries = move_batteries)
                visualisation.plot_per_battery(district)
            else:
                print(f"Invalid input: {plot}")

            if output == "yes":
                output.generate_json(district)
            elif output == "no":
                pass
            else:
                print(f"Invalid input: {output}")

        elif algorithm == "sim_ann":
            if plot == "live":
                district = simulated_annealing.simulated_annealing_algorithm(district, plot = "y", move_batteries = move_batteries)
            elif plot == "static":
                district = simulated_annealing.simulated_annealing_algorithm(district, move_batteries = move_batteries)
                visualisation.basic_static_visualise(district)
            elif plot == "battery":
                district = simulated_annealing.simulated_annealing_algorithm(district, move_batteries = move_batteries)
                visualisation.plot_per_battery(district)
            else:
                print(f"Invalid input: {plot}")

            if output == "yes":
                output.generate_json(district)
            elif output == "no":
                pass
            else:
                print(f"Invalid input: {output}")

        elif algorithm == "random":
            if plot == "live":
                print("There is no live plot for random algorithm")
            elif plot == "static":
                visualisation.basic_static_visualise(district)
            elif plot == "battery":
                visualisation.plot_per_battery(district)
            else:
                print(f"Invalid input: {plot}")

            if output == "yes":
                output.generate_json(district)
            elif output == "no":
                pass
            else:
                print(f"Invalid input: {output}")
        else:
            print(f"Invalid input: {algorithm}")

    elif experiment == "yes":
        if algorithm == "hill":
            experiment_hill_climb.experiment_hill_climb(district_number, runs)
        elif algorithm == "sim_ann":
            experiment_sim_ann.experiment_sim_ann(district_number, runs)
        elif algorithm == "random":
            experiment_random.experiment_random(district_number, runs)
        else:
            print(f"Invalid input: {algorithm}")

    else:
        print(f"Invalid input: {experiment}")


# ----------------------------- Argument Parser ---------------------------------
if __name__ == "__main__":
    # Set-up parsing command line arguments
    parser = argparse.ArgumentParser(description = "Run SmartGrid")

    # Adding arguments
    parser.add_argument("-d", "--district_number", default = 1, help = "Choose district number")
    parser.add_argument("-a", "--algorithm", default = 'random', help = "Choose algorithm: hill, sim_ann, random or none")
    parser.add_argument("-m", "--move_batteries", default = False, help = "Choose if batteries may move: yes or no")
    parser.add_argument("-p", "--plot", default = "static", help = "Choose plot type: static, live or battery (for plot per battery)")
    parser.add_argument("-e", "--experiment", default = "no", help = "Choose yes or no for experiment")
    parser.add_argument("-r", "--runs", type=int, default = 18, help = "Choose amount of runs for experiment")
    parser.add_argument("-o", "--output", default = "no", help = "Choose yes or no for json output")

    # Read arguments from command line
    args = parser.parse_args()

    # Run main with provide arguments
    main(args.district_number, args.algorithm, args.move_batteries, args.plot, args.experiment, args.runs, args.output)
