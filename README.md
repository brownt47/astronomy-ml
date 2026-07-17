# Astronomy ML

A professional machine learning pipeline for astronomical image analysis, designed to scale from local development to large survey datasets such as Galaxy Zoo and, eventually, data from the Vera C. Rubin Observatory.

## Project Goals

This project aims to build research-quality, reproducible software for astronomical image analysis using modern machine learning techniques.

The long-term objectives are to:

- Develop a modular and maintainable data pipeline.
- Follow professional software engineering practices.
- Support large-scale astronomical datasets.
- Enable publishable research and open-source collaboration.

## Current Features

- Configuration-driven project structure
- Recursive image inventory
- Image validation
- Image metadata extraction
- Manifest generation using pandas
- Comprehensive unit tests with pytest

## Planned Features

- FITS image support with Astropy
- Manifest persistence using Parquet
- Dataset preprocessing pipeline
- Exploratory data analysis
- Machine learning and deep learning models
- Support for distributed processing on the ARTIC cluster
- Future integration with Rubin Observatory data products

## Project Structure

```text
astronomy-ml/
├── configs/
├── data/
├── scripts/
├── src/
│   └── astronomy_ml/
├── tests/
└── README.md
```

## Technologies

- Python
- pandas
- Parquet
- Pillow
- pytest
- pathlib
- YAML configuration
- Git & GitHub

## Development Philosophy

This repository is being developed incrementally using professional software engineering practices.

Each feature is:

1. Designed
2. Implemented
3. Unit tested
4. Reviewed
5. Committed to Git before moving to the next feature

The goal is to produce software that another researcher could reasonably clone, understand, and extend.

## Roadmap

- [x] Project structure
- [x] Configuration management
- [x] Image inventory
- [x] Image validation
- [x] Metadata extraction
- [x] Manifest generation
- [ ] Manifest persistence
- [ ] FITS support
- [ ] Dataset preprocessing
- [ ] Machine learning pipeline
- [ ] Model training
- [ ] Distributed processing
- [ ] Rubin Observatory support

## License

This project is released under the MIT License.
