import os
import warnings

# Suppress specific FutureWarnings from scikit-learn
warnings.filterwarnings("ignore", category=FutureWarning)

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from data.data_handling_refactored import DatasetRefactored
from experiment.experiment import Experiment
from plotting.experiment_plotter import ExperimentPlotter
from utils.logger import Logger


def initialize_models_and_params():
    models = {
        "Logistic Regression": LogisticRegression(solver='liblinear'),
        "KNN": KNeighborsClassifier()
    }

    param_grids = {
        "Logistic Regression": {"C": [0.1, 1, 10], "max_iter": [10000]},
        "KNN": {
            "n_neighbors": [3, 5, 7, 9],
            "weights": ["uniform", "distance"],
            "metric": ["euclidean", "manhattan"]
        }
    }

    return models, param_grids


def run_experiment(dataset, models, param_grids, logger):
    logger.info("Starting the experiment...")
    experiment = Experiment(models, param_grids, n_replications=30, logger=logger)
    results = experiment.run(dataset.data, dataset.target)
    logger.info("Experiment completed successfully.")
    return experiment, results


def plot_results(experiment, results, logger):
    logger.info("Generating plots for the experiment results...")
    plotter = ExperimentPlotter()

    plotter.plot_metric_density(results, metrics=('accuracy',))

    plotter.plot_evaluation_metric_over_replications(
        experiment.results.groupby('model')['accuracy'].apply(list).to_dict(),
        'Accuracy per Replication and Average Accuracy',
        'Accuracy'
    )

    plotter.plot_evaluation_metric_over_replications(
        experiment.results.groupby('model')['precision'].apply(list).to_dict(),
        'Precision per Replication and Average Precision',
        'Precision'
    )

    plotter.plot_confusion_matrices(experiment.mean_conf_matrices)
    plotter.print_best_parameters(results)

    logger.info("Plots generated successfully.")


def main():
    os.makedirs("outputs", exist_ok=True)

    logger = Logger(log_file="outputs/application.log")
    logger.info("Application started.")

    dataset = DatasetRefactored()
    models, param_grids = initialize_models_and_params()
    experiment, results = run_experiment(dataset, models, param_grids, logger)
    plot_results(experiment, results, logger)

    logger.info("Application finished successfully.")


if __name__ == "__main__":
    main()