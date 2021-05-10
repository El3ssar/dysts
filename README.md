# thom

Simulate hundreds of chaotic dynamical systems.

## Usage

Import a model and run a simulation with default initial conditions and parameter values

    model = Lorenz()
    model.make_trajectory(1000)
    
    model = Logistic()
    model.make_trajectory(1000)
    
Modify a model's default parameter values

    model = Lorenz()
    model.gamma = 1
    model.ic = [0, 0, 0.2]
    model.make_trajectory(1000)

## Implementation

The right hand side of each dynamical equation is compiled using `numba`, wherever possible. Ensembles of trajectories are vectorized.

Attractor names, default parameter values, references, and other metadata are stored in parseable JSON database files.

The default integration step is stored in each continuous-time model's `dt` field. This integration timestep was chosen based on the highest significant frequency observed in the power spectrum, with significance being determined relative to [surrogate time series](https://en.wikipedia.org/wiki/Surrogate_data_testing). The `period` field contains the timescale associated with the dominant frequency in each system's power spectrum.

When using the `model.make_trajectory` method, integration is performed at the default `dt`. The integrated trajectory is then resampled based on the `period`. The resulting trajectories will have have consistant domant timescales across models, despite having different integration timesteps.

Default initial conditions are generated by running each model until moments of the autocorrelation function all become stationary.

## Contributing

If you know of any systems should be included, please feel free to submit an issue or pull request. The biggest bottleneck when adding new models is a lack of known parameter values and initial conditions, and so please provide a reference or code that contains all parameter values necessary to produce the claimed dynamics.



## To do

+ Find an efficient way to compile the right hand side of each continuous time system, ideally whenever the class is first invoked. Rather than using numba or jax, it might be easiest to just implement most of `thom.py` in Cython.
+ Align the initial phases, potentially by picking default starting initial conditions that lie on the attractor, but which are as close as possible to the origin
+ Add a `dimension` field with the number of dynamical variables
+ Improve the resampling method used by `make_trajectory`




