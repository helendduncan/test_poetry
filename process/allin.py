import sys
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def reader(pth):
    # Read in the path to the (demo) file
    # Return the data as a pandas dataframe
    selected_file = Path(pth)
    if not selected_file.exists():
        raise IOError("Cannot find file")
    # return f"Using file {selected_file}"
    df = pd.read_csv(selected_file)
    return df


def reshape(df):
    # Get the unique values of IP1 and IP2
    IP1 = sorted(df["IP1"].unique())
    IP2 = sorted(df["IP2"].unique())
    # Use Pandas to create a pivot table of the data based on IP1 and IP2 values
    # Have all NAN converted to 10,000,000
    fit_df = df.pivot_table("Fit", index="IP2", columns="IP1", aggfunc="sum").fillna(
        10000000
    )
    relax_df = df.pivot_table(
        "Relax", index="IP2", columns="IP1", aggfunc="sum"
    ).fillna(10000000)
    # Convert both to numpy arrays
    fit = fit_df.to_numpy()
    relax = relax_df.to_numpy()
    fig, axf = plt.subplots()
    fit_plot = axf.contourf(IP1, IP2, fit, cmap="coolwarm", levels=50)
    plt.close(fig)
    fig, axr = plt.subplots()
    relax_plot = axr.contourf(IP1, IP2, relax, cmap="coolwarm", levels=50)
    plt.close(fig)
    return (axf, axr)


def mkpng(ax=None,name=None,ext=None):
    if ax is None: raise TypeError
    if ext == None: ext = 'png'
    if name==None:  name='output_graph'
    opn=name+'.'+ext
    fig = ax.get_figure()
    fig.savefig(opn)
