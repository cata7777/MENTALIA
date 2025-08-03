# Extracted Tesis Maestras

This directory contains metadata for thesis archives detected in the repository.
Run `python3 extract_maestras.py` to regenerate `SUMMARY.json`. To avoid adding
large files to the repository, individual thesis files are removed after
processing unless the environment variable `KEEP_FILES=1` is set.

Use `python3 maestra_microservice.py` to launch a simple HTTP service exposing the
aggregated thesis data.
