from importlib import import_module
from typing import Any, Tuple
import sys
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot



def load_module(module_name: str) -> Tuple[Any, str | None]:
    try:
        module = import_module(module_name)
        version = getattr(module, '__version__')
        return module, version

    except ImportError:
        return None, None


def main() -> None:
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
    for dependencie, message in dependencies.items():
        module, version = load_module(dependencie)
        if version and module:
            print(f"[OK] {dependencie} ({version}) - {message}")
            modules[dependencie] = module
        else:
            if dependencie == 'requests':
                print(f"[KO] Missing optional dependencies: {dependencie}")
            else:
                print(f"[KO] MISSING REQUIRED DEPENDENCY: {dependencie}")
                print("Install them with one of the following methods:")
                print("pip install -r requirements.txt")
                print("poetry install")
                sys.exit(1)

    print()
    pd = modules['pandas']
    np = modules['numpy']
    cycle = np.arange(1, 1001)
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
