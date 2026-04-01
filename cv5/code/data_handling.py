import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from typing import Tuple, List, Optional, Callable


class Dataset:
    def __init__(self):
        data = load_breast_cancer()
        self.data = data.data
        self.target = data.target
        self.feature_names = data.feature_names
        self.target_names = data.target_names
        self.__load_and_clean_data()

    def __load_and_clean_data(self):
        df = pd.DataFrame(self.data, columns=self.feature_names)
        df["target"] = self.target

        df.drop_duplicates(inplace=True)
        df.dropna(inplace=True)

        self.target = df["target"].values
        self.data = df.drop("target", axis=1).values

    def __generic_plot(self, plot_func: Callable, *args, **kwargs):
        general_kwargs = {
            key: kwargs.pop(key, None)
            for key in ["title", "xlabel", "ylabel", "xticks_rotation", "yticks", "yticklabels", "xticks"]
        }

        plt.figure(figsize=kwargs.pop("figsize", (10, 6)))
        plot_func(*args, **kwargs)

        if general_kwargs["title"]:
            plt.title(general_kwargs["title"])
        if general_kwargs["xlabel"]:
            plt.xlabel(general_kwargs["xlabel"])
        if general_kwargs["ylabel"]:
            plt.ylabel(general_kwargs["ylabel"])
        if general_kwargs["xticks_rotation"]:
            plt.xticks(rotation=general_kwargs["xticks_rotation"])
        if general_kwargs["xticks"] is not None:
            plt.xticks(ticks=general_kwargs["xticks"])
        if general_kwargs["yticks"] is not None and general_kwargs["yticklabels"] is not None:
            plt.yticks(ticks=general_kwargs["yticks"], labels=general_kwargs["yticklabels"])

        plt.tight_layout()
        plt.show()

    def split_data(
        self,
        test_size: float = 0.2,
        stratify: bool = True,
        random_state: int = 42
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:

        stratify_param = self.target if stratify else None
        return train_test_split(
            self.data,
            self.target,
            test_size=test_size,
            stratify=stratify_param,
            random_state=random_state
        )

    def scale_data(
        self,
        X_train: np.ndarray,
        X_test: np.ndarray,
        scale_type: str = "standard"
    ) -> Tuple[np.ndarray, np.ndarray]:

        scalers = {
            "standard": StandardScaler(),
            "normalize": MinMaxScaler(),
            "robust": RobustScaler()
        }

        scaler = scalers.get(scale_type)

        if scaler is None:
            raise ValueError("Zly scale_type. Pouzi 'standard', 'normalize' alebo 'robust'.")

        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        return X_train_scaled, X_test_scaled

    def calculate_statistics(self):
        df = pd.DataFrame(self.data, columns=self.feature_names)

        stats = pd.DataFrame()
        stats["mean"] = df.mean()
        stats["median"] = df.median()
        stats["std"] = df.std()

        return stats

    def summarize_features(self, feature_names=None):
        df = pd.DataFrame(self.data, columns=self.feature_names)

        if feature_names != None:
            df = df[feature_names]

        result = []

        for col in df.columns:
            amountUniques = df[col].nunique()
            mostCommon = df[col].mode()[0]
            amount = df[col].value_counts().iloc[0]

            result.append({
                "feature": col,
                "unique": amountUniques,
                "top": mostCommon,
                "count": amount
            })

        return pd.DataFrame(result)

    def visualize_feature_distribution(self, feature_index: int, scaled_data: Optional[np.ndarray] = None, title_suffix: str = ""):
        if feature_index < 0 or feature_index >= len(self.feature_names):
            raise IndexError("Zly index vlastnosti.")

        feature_name = self.feature_names[feature_index]
        original_feature = self.data[:, feature_index]

        self.__generic_plot(
            sns.boxplot,
            data=original_feature,
            color="blue",
            width=0.3,
            title=f"Boxplot of Feature: {feature_name} {title_suffix}",
            xlabel=feature_name,
            ylabel="Value"
        )

        if scaled_data is not None:
            scaled_feature = scaled_data[:, feature_index]
            self.__generic_plot(
                sns.boxplot,
                data=scaled_feature,
                color="orange",
                width=0.3,
                title=f"Boxplot of Scaled Feature: {feature_name} {title_suffix}",
                xlabel=feature_name,
                ylabel="Value"
            )

    def plot_class_distribution(self):
        df = pd.DataFrame({"target": self.target})
        self.__generic_plot(sns.countplot, x="target", data=df, title="Class Distribution")

    def plot_correlation_matrix(self):
        df = pd.DataFrame(self.data, columns=self.feature_names)
        self.__generic_plot(
            sns.heatmap,
            df.corr(),
            annot=True,
            fmt=".2f",
            cmap="coolwarm",
            figsize=(20, 15),
            title="Feature Correlation Matrix"
        )

    def feature_importance(self):
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(self.data, self.target)

        importances = model.feature_importances_
        indices = np.argsort(importances)[::-1]

        sorted_names = [self.feature_names[i] for i in indices]

        self.__generic_plot(
            plt.bar,
            range(self.data.shape[1]),
            importances[indices],
            align="center",
            title="Feature Importances",
            xlabel="Features",
            ylabel="Importance",
            xticks=range(self.data.shape[1]),
            xticks_rotation=90,
            figsize=(12, 6)
        )

        plt.xticks(range(self.data.shape[1]), sorted_names, rotation=90)
        plt.tight_layout()
        plt.show()

    def plot_feature_distributions(self):
        df = pd.DataFrame(self.data, columns=self.feature_names)
        df.hist(bins=20, figsize=(20, 15))
        plt.tight_layout()
        plt.show()

    def plot_box_plots(self, scaled_data: Optional[np.ndarray] = None, target: Optional[np.ndarray] = None):
        data_to_plot = scaled_data if scaled_data is not None else self.data
        target_to_plot = target if target is not None else self.target

        if len(data_to_plot) != len(target_to_plot):
            raise ValueError("Dlzka data a target sa musi zhodovat.")

        df = pd.DataFrame(data_to_plot, columns=self.feature_names)
        df["target"] = target_to_plot

        df_melted = pd.melt(df, id_vars=["target"], var_name="features", value_name="value")

        self.__generic_plot(
            sns.boxplot,
            x="features",
            y="value",
            hue="target",
            data=df_melted,
            xticks_rotation=90,
            figsize=(14, 6),
            title="Box plots of features"
        )

    def plot_pair_plot(self, features: List[str]):
        df = pd.DataFrame(self.data, columns=self.feature_names)
        df["target"] = self.target

        plot = sns.pairplot(df, vars=features, hue="target", height=2.5)
        plot.fig.suptitle("Pair Plot of Selected Features", y=1.02)
        plt.show()

    def plot_all_features_before_after_scaling(self, X_train: np.ndarray, X_train_scaled: np.ndarray, scale_type: str):
        self.__generic_plot(
            sns.boxplot,
            data=X_train,
            orient="h",
            title=f"Before {scale_type}",
            ylabel="Features",
            xlabel="Values",
            yticks=range(len(self.feature_names)),
            yticklabels=self.feature_names,
            figsize=(16, 8)
        )

        self.__generic_plot(
            sns.boxplot,
            data=X_train_scaled,
            orient="h",
            title=f"After {scale_type}",
            ylabel="Features",
            xlabel="Values",
            yticks=range(len(self.feature_names)),
            yticklabels=self.feature_names,
            figsize=(16, 8)
        )

    def plot_feature_before_after_scaling(self, X_train: np.ndarray, X_train_scaled: np.ndarray, feature_name: str):
        if feature_name not in self.feature_names:
            raise ValueError(f"Feature '{feature_name}' sa nenasla.")

        feature_index = list(self.feature_names).index(feature_name)
        original_feature = X_train[:, feature_index]
        scaled_feature = X_train_scaled[:, feature_index]

        self.__generic_plot(
            plt.hist,
            original_feature,
            bins=20,
            color="blue",
            alpha=0.7,
            title=f"Before Scaling: {feature_name}",
            xlabel=feature_name,
            ylabel="Frequency",
            figsize=(12, 6)
        )

        self.__generic_plot(
            plt.hist,
            scaled_feature,
            bins=20,
            color="orange",
            alpha=0.7,
            title=f"After Scaling: {feature_name}",
            xlabel=feature_name,
            ylabel="Frequency",
            figsize=(12, 6)
        )