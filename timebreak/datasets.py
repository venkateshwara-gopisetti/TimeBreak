"""
"""

from os.path import join as path_join
from random import randint

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from .utils import DATASET_DIR, datasets_list

class SampleData:
    def __init__(self):
        self.xlim = 100
        self.flush()
    def add_series(self, frequency):
        amplitude = randint(1,100)/100
        new_series = amplitude * np.sin(2 * np.pi * self.lsp / frequency)
        self.additives.append({"series":new_series, "amplitude":amplitude, "frequency":frequency})
        self.series += self.additives[-1]["series"]
    def flush(self):
        """Function to clear out instace attributes.
        """
        self.series = self.lsp * 0
        self.lsp = np.linspace(0, self.xlim, self.xlim*20)
        self.additives = []
    def plot_series(self):
        """Function to plot all the series generated in this class on a matplotlib multi-plot
        """
        fig, axs = plt.subplots(nrows=len(self.additives)+1, ncols=1, figsize=(12, 8))
        for row, data in enumerate(self.additives):
            # plot time signal:
            axs[row].set_title(f'Frequency:{data["frequency"]}')
            axs[row].plot(data["series"])
            axs[row].set_xlabel("Time")
            axs[row].set_ylabel("Amplitude")
        axs[-1].set_title('Overall Signal')
        axs[-1].plot(self.series)
        axs[-1].set_xlabel("Time")
        axs[-1].set_ylabel("Amplitude")
        fig.align_xlabels(axs)
        fig.tight_layout()
        plt.show()
    def generate_random(self):
        """Function to generate a random series by calling the add_series function
        """
        self.flush()
        for _ in range(randint(2,5)):
            self.add_series(randint(2,10))

class ReadSampleDataset:
    """Class to read and return a sample dataset from store based on tag.
    """
    def __new__(cls, tag):
        if tag not in datasets_list:
            raise ValueError("Unknown tag. Please use one of the available :%s" % list(datasets_list.keys()))
        return pd.read_csv(path_join(DATASET_DIR, datasets_list[tag]))

if __name__=="__main__":
    a = SampleData()
    a.generate_random()
    a.plot_series()