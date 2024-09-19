import dysts.flows as dfl
from dysts.analysis import compute_timestep

if __name__ == "__main__":
    num_points_per_period = 1024
    num_periods = 4
    num_points = num_periods * num_points_per_period

    dyst_name = "Lorenz"
    system = getattr(dfl, dyst_name)()
    dt = compute_timestep(
        system,
        total_length=num_points,
        transient_fraction=0.2,
        num_iters=5,
        pts_per_period=num_points_per_period,
        return_period=True,
    )
    print("result: ", dt)

# TODO: Use scipy optimize for black box optimization of dt from initial guess
# until it meets characteristic timescale criteria
# only do if it is clear how to make a cost function