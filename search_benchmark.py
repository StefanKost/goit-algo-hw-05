import timeit
from pathlib import Path
from typing import Callable, Dict

from search_algorithms import boyer_moore_search, kmp_search, rabin_karp_search

ALGORITHMS: Dict[str, Callable[[str, str], int]] = {
    "Boyer-Moore": boyer_moore_search,
    "Knuth-Morris-Pratt": kmp_search,
    "Rabin-Karp": rabin_karp_search,
}


def load_file(filepath: str | Path) -> str:
    """Load text from a file."""
    return Path(filepath).read_text(encoding="utf-8", errors="ignore")


def measure(func: Callable[[str, str], int], text: str, pattern: str, iterations: int) -> float:
    """Measure average execution time over multiple iterations."""
    return timeit.timeit(lambda: func(text, pattern), number=iterations)


def run_benchmark(filepath: str | Path, existing: str, fictional: str, iterations: int) -> dict:
    """Run substring search benchmark for both patterns."""
    text = load_file(filepath)
    results = {"existing": {}, "fictional": {}}

    for name, func in ALGORITHMS.items():
        results["existing"][name] = measure(func, text, existing, iterations)
        results["fictional"][name] = measure(func, text, fictional, iterations)

    return results


def print_results(article_name: str, results: dict) -> None:
    """Print benchmark results in a table."""
    print(f"\n{article_name}")
    divider = "-" * 58
    print(divider)
    print(f"{'Algorithm':<25} {'Existing (sec)':<15} {'Fictional (sec)':<15}")
    print(divider)

    for algo in results["existing"]:
        ex_time = results["existing"][algo]
        fic_time = results["fictional"][algo]
        print(f"{algo:<25} {ex_time:<15f} {fic_time:<15f}")


def find_fastest(results: dict, pattern_type: str) -> str:
    """Return the name of the fastest algorithm for a given pattern type."""
    return min(results[pattern_type], key=results[pattern_type].get)


if __name__ == "__main__":
    ITERATIONS = 1000
    base_path = Path(__file__).parent / 'data'

    existing_pattern = "хеш-таблиці"
    fictional_pattern = "fake text"

    print("-" * 58)
    print("|" + " " * 9 + "Substring Search Algorithms Comparison" + " " * 9 + "|")
    print("-" * 58)
    print(f"Iterations: {ITERATIONS}")
    print(f"Existing pattern: '{existing_pattern}'")
    print(f"Fictional pattern: '{fictional_pattern}'")

    # Run benchmarks for both articles
    results_one = run_benchmark(base_path / "article_one.txt", existing_pattern, fictional_pattern, ITERATIONS)
    print_results("Article 1", results_one)

    results_two = run_benchmark(base_path / "article_two.txt", existing_pattern, fictional_pattern, ITERATIONS)
    print_results("Article 2", results_two)

    # Conclusions
    print("-" * 58)
    print(" " * 23 + "Conclusions")
    print("-" * 58)

    print("Article 1:")
    print(f"- Fastest (existing): {find_fastest(results_one, 'existing')}")
    print(f"- Fastest (fictional): {find_fastest(results_one, 'fictional')}")

    print("\nArticle 2:")
    print(f"- Fastest (existing): {find_fastest(results_two, 'existing')}")
    print(f"- Fastest (fictional): {find_fastest(results_two, 'fictional')}")

    # Overall fastest
    total = {algo: (
            results_one["existing"][algo] + results_one["fictional"][algo] +
            results_two["existing"][algo] + results_two["fictional"][algo]
    ) for algo in ALGORITHMS}

    overall_fastest = min(total, key=total.get)
    print(f"\nFastest: {overall_fastest}")
