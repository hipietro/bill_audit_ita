# Bill Audit — Product Scope

## Product vision

Bill Audit is a privacy-focused platform that helps users understand, track, and compare their utility bills.

The application extracts structured information from bills, builds a personal history of costs and consumption, and presents the results through charts and understandable reports.

Users may optionally contribute anonymized bill data to a shared database. This data is aggregated and used to compare each user's bill with bills from similar households and contracts.

The long-term goal is not only to digitize bills, but to answer questions such as:

- How is my consumption changing over time?
- Am I spending more than users in similar conditions?
- Is my effective unit cost unusually high?
- Which parts of my bill have increased?
- Is my consumption consistent with previous periods?
- Are there unusual charges or inconsistencies?
- How does my bill compare with the relevant reference group?

Bill Audit begins with Italian electricity bills but is designed to progressively support multiple providers, document layouts, input formats, and utility types.

## Problem

Italian utility bills contain important information such as consumption, billing periods, taxes, discounts, adjustments, and additional services.

This information can be difficult to understand or compare because:

- providers use different document layouts;
- relevant information may be spread across multiple pages;
- descriptions and labels may vary between providers;
- bills can contain estimated consumption, adjustments, discounts, or additional services;
- customers often verify totals and consumption manually;
- bills may be provided as digital PDFs, scanned documents, or photographs.

Bill Audit aims to transform these documents into consistent, structured, and verifiable information.

## Target users

The initial target users are:

- Italian households that want to understand their utility bills;
- users who want to verify bill totals and consumption;
- users who want to compare bills over time;
- developers and data analysts interested in working with normalized utility-bill data.

Small businesses may be supported later, but business-specific billing rules are not part of the initial scope.

## Product principles

### Provider-independent

The core extraction pipeline must not depend on a single provider or on fixed page coordinates.

Provider-specific adapters may eventually be added as optional improvements, but the main system must use semantic labels, spatial relationships, document structure, and normalized field definitions.

### Evidence-based extraction

Every extracted value should retain information about where it came from, such as:

- page number;
- original text;
- document coordinates;
- extraction method;
- confidence score.

This makes results explainable and easier to verify.

### Explicit uncertainty

The program must not silently invent missing information.

When a value cannot be extracted reliably, the result should contain:

- a missing value;
- a low-confidence indication;
- or a warning requiring user verification.

### Local-first processing

Bills may contain personal and financial information. The initial product should process documents locally whenever possible and must not upload them to external services without explicit user consent.

### Extensible architecture

Input reading, OCR, field extraction, normalization, auditing, and reporting must remain separate components.

This allows new document formats, OCR engines, utility types, and validation rules to be added without rewriting the entire application.

## Long-term product scope

The intended product may eventually support:

### Input formats

- digitally generated PDF files;
- scanned PDF files;
- JPG and JPEG images;
- PNG images;
- photographs taken with a smartphone.

### Utility types

- electricity;
- gas;
- water;
- telecommunications;
- other recurring household services.

### Core capabilities

- automatic utility-type detection;
- provider-independent field extraction;
- normalization of dates, monetary values, units, and descriptions;
- consumption extraction;
- cost-component extraction;
- arithmetic verification;
- detection of missing or inconsistent information;
- comparison between billing periods;
- historical summaries and trends;
- export to structured formats such as JSON and CSV;
- clear warnings for uncertain or unsupported information.

## Personal analytics

Bill Audit should allow users to build a personal history of their bills and visualize:

- consumption over time;
- total cost over time;
- effective cost per kWh or other relevant unit;
- measured and estimated consumption;
- cost components over time;
- taxes, discounts, adjustments, and additional services;
- differences between billing periods;
- seasonal consumption patterns;
- unusual changes and potential anomalies.

Users should be able to filter charts by date, provider, utility type, and billing period.

## Anonymous community benchmarking

Users may explicitly choose to share normalized and anonymized data with the Bill Audit community database.

Sharing must be optional and disabled by default.

Raw bill documents, names, addresses, customer identifiers, tax codes, payment information, and meter identifiers must never be included in the shared dataset.

The shared dataset may contain information such as:

- utility type;
- billing period;
- broad geographic area;
- provider;
- type of offer;
- contracted power;
- total consumption;
- total amount;
- normalized cost components;
- effective unit cost;
- household-size range;
- selected contextual information provided voluntarily by the user.

Before uploading any information, the application must show exactly which fields will be shared and require explicit user confirmation.

## Comparison groups

Meaningful comparisons should be made between sufficiently similar users.

Possible comparison criteria include:

- billing period;
- broad geographic area;
- utility type;
- household-size range;
- contracted power;
- type of offer;
- primary heating source;
- presence of solar panels;
- resident or non-resident contract;
- approximate property characteristics.

Reports must clearly indicate which criteria were used and how many anonymous records were included in the comparison.

Comparison groups containing too few users must not be displayed, to reduce privacy risks and avoid unreliable conclusions.

## Community report

The final report may include:

- consumption trend;
- total-cost trend;
- effective unit cost;
- comparison with the median of similar users;
- percentile within the comparison group;
- difference from the comparison-group average;
- unusually high or low cost components;
- estimated-versus-measured consumption;
- detected anomalies;
- missing or uncertain information;
- an explanation of how each result was calculated.

Comparisons must be presented as informational analysis and not as legal, financial, or contractual advice.

## Version 0.1 scope

Version 0.1 will validate the extraction and auditing architecture using Italian electricity bills.

### Supported documents

- digitally generated PDF files;
- Italian electricity bills;
- bills from multiple providers;
- documents containing extractable text.

The implementation must not be built exclusively around one provider.

### Information to extract

Version 0.1 should attempt to extract:

- provider name;
- bill number;
- issue date;
- billing-period start date;
- billing-period end date;
- total amount due;
- currency;
- total electricity consumption in kWh;
- measured consumption, when available;
- estimated consumption, when available;
- cost components;
- component descriptions;
- component amounts.

### Initial cost categories

Cost components may be normalized into categories such as:

- energy sales;
- network and system charges;
- excise duty;
- VAT;
- social bonus;
- discounts;
- adjustments;
- additional products or services;
- TV licence fee;
- other items.

### Audit capabilities

Version 0.1 should:

- verify that dates are logically valid;
- reject negative totals when they are not meaningful;
- compare the sum of cost components with the bill total;
- report the difference between the calculated and declared totals;
- identify missing required information;
- produce warnings instead of failing when optional information is unavailable;
- preserve enough source information to explain extracted values.

## Outside version 0.1

The following capabilities are part of the product vision but are not required for version 0.1:

- scanned PDF support;
- JPG, JPEG, and PNG support;
- image correction and preprocessing;
- OCR;
- automatic document-type classification;
- gas, water, and telecommunications bills;
- guaranteed support for every possible document layout;
- handwritten documents;
- automatic tariff recommendations;
- legal or financial advice;
- automatic complaints to providers;
- cloud accounts and document synchronization;
- a graphical user interface.

## Version 0.1 validation

Version 0.1 should be tested using anonymized electricity bills from at least two different providers.

The test set should include:

- at least one bill for each supported provider;
- bills with different billing periods and totals;
- at least one bill containing estimated or measured consumption;
- at least one bill containing a discount, adjustment, tax, or additional charge.

No real personal information should be committed to the repository.

## Definition of done

Version 0.1 is considered complete when:

- a user can provide a supported electricity-bill PDF;
- the program extracts the defined core fields;
- extracted values are represented using normalized Python models;
- missing or uncertain fields produce clear warnings;
- arithmetic validation compares cost components with the declared total;
- the same extraction pipeline works with bills from at least two providers;
- automated tests cover the models, extraction behaviour, and audit rules;
- sample documents or fixtures contain no personal information;
- the project documentation clearly explains supported and unsupported cases.

## Planned evolution

### Version 0.2 — Image and OCR support

Add support for scanned PDFs and JPG, JPEG, and PNG images, including:

- image rotation;
- perspective correction;
- contrast enhancement;
- blur detection;
- OCR;
- layout analysis;
- confidence scores.

### Version 0.3 — Gas bills

Extend the normalized data model to support gas consumption and units such as standard cubic metres.

### Version 0.4 — Additional utility types

Evaluate water and telecommunications bills using utility-specific models and audit rules.