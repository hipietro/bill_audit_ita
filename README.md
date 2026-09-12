# Bill Audit Italia

A privacy-focused tool for extracting, analyzing, and comparing data from Italian utility bills.

> This README may not deserve its own commit yet, but it is getting one anyway.

## About the project

Bill Audit Italia was born primarily as a learning project.

I am building it to gain practical experience with technologies such as Python, NumPy, pandas, PySpark, and, later, C# and ASP.NET Core. Other tools may be introduced as the project evolves.

Development will therefore be deliberately gradual. Commits may be small and infrequent because the goal is not only to finish the application, but also to understand the concepts and technologies used to build it.

The repository is public so that the entire learning and development process can be followed over time.

## Product vision

Bill Audit aims to help users understand their utility bills instead of treating them as difficult documents that are only opened when something looks wrong.

The long-term application should be able to:

- extract structured information from utility bills;
- support different providers and document layouts;
- accept digital PDFs, scanned documents, and photographs;
- track consumption and costs over time;
- display personal consumption and cost charts;
- identify missing information and potential inconsistencies;
- verify bill totals and cost components;
- generate understandable reports;
- optionally compare anonymized data with data shared by other users.

The application will initially focus on Italian electricity bills. Support for gas, water, telecommunications, and other recurring services may be added later.

## What makes it different?

Bill Audit is not intended to be a parser built around a single provider or a fixed document layout.

The project is designed around a provider-independent extraction pipeline that progressively combines:

- document text extraction;
- semantic field recognition;
- document layout information;
- OCR for scanned documents and photographs;
- normalized bill models;
- arithmetic validation;
- historical analysis;
- anonymous community benchmarking.

When the application is uncertain about an extracted value, it should report that uncertainty instead of silently inventing information.

## Community benchmarking

In a future version, users will be able to explicitly choose whether to contribute normalized and anonymized bill data to a shared database.

This community dataset may be used to answer questions such as:

- Is my consumption increasing over time?
- Is my effective unit cost unusually high?
- How does my bill compare with similar households?
- Which cost components have changed?
- Are there unusual charges or inconsistencies?
- How do my costs compare with the relevant reference group?

Sharing will be optional and disabled by default.

Raw bill files and personally identifiable information must never be included in the shared dataset. This includes names, exact addresses, tax codes, customer identifiers, meter identifiers, and payment information.

## Current status

Bill Audit is in the very early stages of development.

The project currently includes:

- an installable Python package;
- a basic command-line entry point;
- initial bill-domain models;
- validation for the main bill fields;
- automated tests with pytest;
- initial cost and electricity-consumption models.

PDF extraction, charts, OCR, online data sharing, and comparison reports are not implemented yet.

## Initial scope

Version `0.1` will focus on:

- Italian electricity bills;
- digitally generated PDF files;
- bills from multiple providers;
- extraction of the main bill fields;
- normalized cost components;
- electricity-consumption data;
- arithmetic verification;
- clear warnings for missing or uncertain information;
- local processing.

The first version will not guarantee compatibility with every possible bill layout.

See [`docs/product-scope.md`](docs/product-scope.md) for the complete product scope and planned evolution.

## Planned roadmap

### v0.1 — PDF extraction and bill auditing

- Read digitally generated electricity-bill PDFs.
- Extract the main bill fields.
- Normalize monetary values, dates, and consumption.
- Support bills from multiple providers.
- Verify totals and cost components.
- Report missing or inconsistent information.

### v0.2 — Personal history and charts

- Store normalized bills locally.
- Track consumption and costs over time.
- Create charts using pandas and a visualization library.
- Compare different billing periods.
- Highlight significant changes.

### v0.3 — OCR and image support

- Support scanned PDF files.
- Support JPG, JPEG, and PNG images.
- Correct rotation and perspective.
- Detect low-quality or blurred images.
- Extract text using OCR.
- Attach confidence information to extracted fields.

### v0.4 — Shared data platform

- Create a web API using C# and ASP.NET Core.
- Store anonymized bill information in PostgreSQL.
- Manage explicit user consent.
- Validate all shared data.
- Prevent personal information from being uploaded.

### v0.5 — Community reports

- Compare users with relevant reference groups.
- Calculate averages, medians, percentiles, and distributions.
- Detect unusual costs and consumption.
- Generate understandable comparison reports.

### Future versions

- Gas bills.
- Water bills.
- Telecommunications bills.
- Additional charts and historical analysis.
- Larger-scale data processing when justified.

## Technologies

Technologies currently used or planned include:

- **Python** — core application and document-processing logic;
- **pytest** — automated testing;
- **NumPy** — numerical calculations and statistical operations;
- **pandas** — bill history, aggregation, and data analysis;
- **PySpark** — possible large-scale data processing if the dataset eventually requires it;
- **C# and ASP.NET Core** — future web API and shared-data services;
- **PostgreSQL** — future storage for normalized and anonymized community data;
- **OCR and document-layout tools** — future extraction from scans and photographs.

Technologies will be introduced only when the project reaches a problem that gives them a meaningful purpose.

## Installation

Clone the repository and move into the project directory:

```bash
git clone https://github.com/hipietro/bill_audit_ita.git
cd bill_audit_ita
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project and its development dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Usage

Run the command-line application:

```bash
bill-audit
```

The command-line interface is currently only a minimal project entry point. Actual bill processing will be added during the implementation of version `0.1`.

## Running the tests

Run the complete test suite with:

```bash
python -m pytest
```

## Privacy

Utility bills may contain sensitive personal and financial information.

For this reason:

- processing should remain local whenever possible;
- real personal data must not be committed to this repository;
- sample bills must be synthetic or properly anonymized;
- online sharing must always require explicit consent;
- raw bill documents must not be uploaded to the community database;
- extracted data must be reviewed and anonymized before sharing.

## Contributing

The project is currently being developed as a personal learning journey, so contributions are not actively requested yet.

Suggestions, discussions, bug reports, and educational feedback are still welcome through GitHub issues.

## Disclaimer

Bill Audit is an educational project.

Its output should not be considered legal, financial, tax, or contractual advice. Extracted information and automated checks may be incomplete or incorrect and should always be verified against the original bill.

## License

A license has not been selected yet.