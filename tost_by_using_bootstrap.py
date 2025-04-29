import numpy as np
from scipy.stats import norm

def tost_bootstrap(x, y, low_eqbound, high_eqbound, n_bootstrap=10000, delta=0.05):
    observed_diff = np.median(x) - np.median(y)

    boot_diffs = []
    for _ in range(n_bootstrap):
        x_sample = np.random.choice(x, size=len(x), replace=True)
        y_sample = np.random.choice(y, size=len(y), replace=True)
        boot_diffs.append(np.median(x_sample) - np.median(y_sample))

    boot_diffs = np.array(boot_diffs)
    
    # TOST (Two One-Sided Tests)
    p_low = np.mean(boot_diffs < low_eqbound)
    p_high = np.mean(boot_diffs > high_eqbound)

    tost_passed = (p_low < delta) and (p_high < delta)

    result = {
        "observed_difference": observed_diff,
        "p_value_low": p_low,
        "p_value_high": p_high,
        "tost_passed": tost_passed,
        "equivalence_bounds": (low_eqbound, high_eqbound)
    }

    return result

np.random.seed(0)
group1 = np.random.normal(loc=100, scale=10, size=50)
group2 = np.random.normal(loc=101, scale=10, size=50)


result = tost_bootstrap(group1, group2, low_eqbound=-3, high_eqbound=3)

for key, value in result.items():
    print(f"{key}: {value}")
