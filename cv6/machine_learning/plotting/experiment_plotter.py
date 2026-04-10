import os
import seaborn as sns
from matplotlib import pyplot as plt
from plotting.base_plotter import BasePlotter


class ExperimentPlotter(BasePlotter):
    """A class for plotting the results of machine learning experiments."""

    def __init__(self):
        os.makedirs("outputs", exist_ok=True)

    def plot_metric_density(self, results, metrics=('accuracy', 'f1_score', 'roc_auc', 'precision')):
        """
        Plot density plots for specified metrics.

        Parameters:
        - results: DataFrame containing the results.
        - metrics: List of metrics to plot.
        """
        for metric in metrics:
            self._BasePlotter__generic_plot(
                sns.kdeplot,
                data=results,
                x=metric,
                hue="model",
                fill=True,
                common_norm=False,
                alpha=0.5,
                title=f'Density Plot of {metric}',
                xlabel=metric,
                ylabel='Density',
                figsize=(10, 6)
            )

    def plot_evaluation_metric_over_replications(self, all_metric_results, title, metric_name):
        """
        Plot metric values for each model over all replications and display the average value.

        Parameters:
        - all_metric_results: Dict containing metric values for each model.
        - title: str, title of the plot.
        - metric_name: str, name of the metric to display on the y-axis.
        """
        def plot_func():
            for model_name, values in all_metric_results.items():
                plt.plot(values, label=model_name)
                avg_value = sum(values) / len(values)
                plt.axhline(y=avg_value, linestyle='--', label=f"{model_name} avg = {avg_value:.2f}")
            plt.legend()

        self._BasePlotter__generic_plot(
            plot_func,
            title=title,
            xlabel='Replication',
            ylabel=metric_name,
            figsize=(10, 5)
        )

    def plot_confusion_matrices(self, confusion_matrices):
        """
        Plot the average confusion matrix for each model.

        Parameters:
        - confusion_matrices: Dict containing the average confusion matrix for each model.
        """
        for model_name, matrix in confusion_matrices.items():
            self._BasePlotter__generic_plot(
                sns.heatmap,
                matrix,
                annot=True,
                fmt='.2f',
                cmap='Blues',
                cbar=False,
                title=f'Average Confusion Matrix: {model_name}',
                xlabel='Predicted label',
                ylabel='True label',
                figsize=(6, 5)
            )

    def print_best_parameters(self, results):
        """
        Print the most frequently chosen best parameters for each model.

        Parameters:
        - results: DataFrame containing the results.
        """
        for model_name in results['model'].unique():
            model_results = results[results['model'] == model_name]
            best_params_list = model_results['best_params'].value_counts().index[0]
            print(f"Most frequently chosen best parameters for {model_name}: {best_params_list}")