# VISANARCI Installation

VISANARCI is a pip-installable fork of the original
[ANARCI](https://github.com/oxpig/ANARCI) v1 implementation.

This package includes the pre-built HMM database and germline metadata required  by ANARCI at runtime. Installation 
does **not** require conda, HMMER, MUSCLE, or access to IMGT.

---

## Install from PyPI

```bash
pip install visanarci
```

Verify the installation:

```bash
ANARCI -h
```

## Install from source

```bash
git clone https://github.com/VisiumCH/VISANARCI
cd VISANARCI
pip install -e .
```

---

## Development

To work on the Python package:

```bash
pip install -e .
```

This is sufficient for development. No additional system dependencies or build steps are required.

### Bundled ANARCI artifacts

The following pre-generated artifacts are included in the package:

- `lib/python/anarci/germlines.py`
- `lib/python/anarci/dat/HMMs/ALL.hmm`
- `lib/python/anarci/dat/HMMs/ALL.hmm.h3f`
- `lib/python/anarci/dat/HMMs/ALL.hmm.h3i`
- `lib/python/anarci/dat/HMMs/ALL.hmm.h3m`
- `lib/python/anarci/dat/HMMs/ALL.hmm.h3p`

These files are required by ANARCI and are bundled to ensure reproducible installations.

### Regenerating ANARCI artifacts (maintainers only)

The original ANARCI build pipeline is preserved under build_pipeline/.

⚠️ This step is not required for normal usage or development.

The pipeline depends on IMGT GENE-DB endpoints, which are currently unstable and may fail or change without notice.

To attempt regeneration:

```bash
conda env create -f build_pipeline/environment.yml
conda activate anarci-build
build_pipeline/RUN_pipeline.sh
```

After running the pipeline, verify that the required files exist:

```bash
test -f lib/python/anarci/germlines.py
test -f lib/python/anarci/dat/HMMs/ALL.hmm
test -f lib/python/anarci/dat/HMMs/ALL.hmm.h3f
test -f lib/python/anarci/dat/HMMs/ALL.hmm.h3i
test -f lib/python/anarci/dat/HMMs/ALL.hmm.h3m
test -f lib/python/anarci/dat/HMMs/ALL.hmm.h3p
```

### Building the package

```bash
uv build
uvx twine check dist/*
```