from data_handling import Dataset

if __name__ == "__main__":
    dataset = Dataset()

    # plot class distribution
    dataset.plot_class_distribution()

    # plot correlation matrix
    dataset.plot_correlation_matrix()

    # plot feature importance
    dataset.feature_importance()

    # plot feature distributions
    dataset.plot_feature_distributions()

    # plot box plots
    dataset.plot_box_plots()

    # plot pair plot for the first 5 features
    selected_features = dataset.feature_names[:5]
    dataset.plot_pair_plot(selected_features)

    stats = dataset.calculate_statistics()
    print("Stats:")
    print(stats)

    summary_all = dataset.summarize_features()
    print("Summary all:")
    print(summary_all)

    selected = ["mean radius", "mean texture", "mean area"]
    summary_selected = dataset.summarize_features(feature_names=selected)
    print("Summary selected:")
    print(summary_selected)