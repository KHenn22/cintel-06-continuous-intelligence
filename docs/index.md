# Continuous Intelligence

This site provides documentation for this project.
Use the navigation to explore module-specific materials.

## How-To Guide

Many instructions are common to all our projects.

See
[⭐ **Workflow: Apply Example**](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
to get these projects running on your machine.

## Project Documentation Pages (docs/)

- **Home** - this documentation landing page
- **Project Instructions** - instructions specific to this module
- **Your Files** - how to copy the example and create your version
- **Glossary** - project terms and concepts

## Additional Resources

- [Suggested Datasets](https://denisecase.github.io/pro-analytics-02/reference/datasets/cintel/)

## Custom Project

### Dataset
Bureau of Transportation Statistics (BTS) Reporting Carrier On-Time
Performance data for Lambert-St. Louis International Airport (STL).
The dataset contains monthly on-time arrival percentages for 2025
(January - December), sourced from transtats.bts.gov.

### Signals
The primary signal used is PCT_ONTIME_ARR — the percentage of flights
arriving on time (defined as within 15 minutes of scheduled arrival) at STL each
month. No new signals were derived; the raw on-time percentage was used
directly as the monitoring signal.

### Experiments
A three-tier assessment label (STABLE, WARNING, DEGRADED) was added to
replace the original two-tier system. Thresholds were set at:
- STABLE: >= 80% on-time
- WARNING: between 70% and 80%
- DEGRADED: below 70%

Thresholds were chosen around a modified industry average for a medium sized airport.  WARNING Threshold is right around average performance (78-80%), but DEGRADED was set below operational stress (75%).  The additional buffer is that the data used does not screen for the reasoning behind the delay, and essentially assumes that the reason for the delay was solely due to conditions at the arrival airport and not anywhere else along the route.

### Results
STL's 2025 performance showed a clear seasonal pattern. January-April and
September-November were STABLE (above 80%). May-August and December were WARNING (below 80%),
with June and July being the lowest at 74% and 73% respectively.

### Interpretation
STL airport experiences measurable performance degradation during summer
months, possibly due to thunderstorm activity in the St. Louis region.
This pattern suggests airlines and passengers should anticipate delays
during June-August. Continuous monitoring using this pipeline could
provide early warning when performance begins declining each spring.  Further analysis behind each delay should be undertaken to determine what factors caused the delay.  This would also properly account for what portion of the flight was the delay, rather than just looking at the destination.
