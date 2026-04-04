"""Check for common dependencies and generate a simple analysis plot."""

from importlib import import_module
from typing import Any, Tuple
import sys
import matplotlib
from matplotlib import pyplot
matplotlib.use("Agg")


def load_module(module_name: str) -> Tuple[Any, str | None]:
    """Import a module and return the module object plus
    its version if available."""
    try:
        module = import_module(module_name)
        version = getattr(module, '__version__')
        return module, version

    except ImportError:
        return None, None


def main() -> None:
    """Validate dependencies, build a small data frame, and save a plot."""
    print()
    print("LOADING STATUS: Loading programs...")
    print()

    print("Checking dependencies:")
    dependencies = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computations ready",
        "matplotlib": "Visualization ready",
        "requests": "Network access ready (optional)",
    }

    modules = {}
    for dependency, message in dependencies.items():
        module, version = load_module(dependency)
        if version and module:
            print(f"[OK] {dependency} ({version}) - {message}")
            modules[dependency] = module
        else:
            if dependency == 'requests':
                print(f"[KO] Missing optional dependencies: {dependency}")
            else:
                print(f"[KO] MISSING REQUIRED DEPENDENCY: {dependency}")
                print("Install them with one of the following methods:")
                # pip installs packages directly from requirements.txt, while poetry manages
                # dependencies plus a lockfile/virtual environment for reproducible installs.
                print("pip install -r requirements.txt")
                print("poetry install")
                sys.exit(1)

    print()
    pd = modules['pandas']
    np = modules['numpy']
    cycle = np.arange(1, 4)
    df = pd.DataFrame({
        'cycle': cycle,
        'power_level': [100, 200, 300]
    })
    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")
    print("Generating visualization...")

    pyplot.figure(figsize=(10, 5))

    pyplot.plot(df['cycle'], df['power_level'], label='Power_level')
    pyplot.legend()
    pyplot.title("Matrix Data Analysis")
    pyplot.xlabel("cycle")
    pyplot.ylabel("power_level")
    pyplot.grid(True)
    pyplot.tight_layout()
    pyplot.savefig("matrix_analysis.png")

    pyplot.close()

    print()
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == '__main__':
    main()
