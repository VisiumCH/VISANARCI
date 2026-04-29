"""Tests that bundled ANARCI artifacts (HMM files and germlines) are present in the installed package."""
from importlib.resources import files


def test_bundled_artifacts_exist():
    hmm_dir = files("anarci").joinpath("dat", "HMMs")

    required = [
        files("anarci").joinpath("germlines.py"),
        hmm_dir.joinpath("ALL.hmm"),
        hmm_dir.joinpath("ALL.hmm.h3f"),
        hmm_dir.joinpath("ALL.hmm.h3i"),
        hmm_dir.joinpath("ALL.hmm.h3m"),
        hmm_dir.joinpath("ALL.hmm.h3p"),
    ]

    for path in required:
        assert path.is_file(), f"Missing bundled artifact: {path}"