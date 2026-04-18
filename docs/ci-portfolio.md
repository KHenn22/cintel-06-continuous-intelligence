# Continuous Intelligence Portfolio

Kevin Hennelly

2026-04

This page summarizes my work on **continuous intelligence** projects.

## 1. Professional Project

### Repository Link

[(clickable link to your repository)](https://github.com/KHenn22/cintel-06-continuous-intelligence)

### Brief Overview of Project Tools and Choices

The continuous intelligence projects through this course implement a comprehensive monitoring system using professional Python development practices. All projects use Python 3.14+ with Polars for high-performance data processing, datafun_toolkit for structured logging, and pyproject.toml for dependency management. The series progresses from basic setup and anomaly detection to advanced signal design, rolling monitoring, drift detection, and finally integrated continuous intelligence pipelines. Key tools include GitHub for version control, UV for package management, and structured logging for operational transparency.  In addition to using the example data, many projects also focused on aviation data.  In particular, airport and airline data were analyzed used tools and techniques for CI taught throughout the course.

## 2. Anomaly Detection

### Repository Link

[(clickable link to your repository)](https://github.com/KHenn22/cintel-02-static-anomalies)

### Techniques

Anomalies were detected using simple threshold-based detection on clinic patient data (age and height measurements). Values exceeding predefined thresholds were flagged as anomalies: age > 16 years or height > 72 inches. Severity levels were then assigned based on how far values exceeded thresholds, categorized as mild, moderate, or severe.

### Artifacts

[artifacts/anomalies_hennelly.csv](artifacts/anomalies_hennelly.csv) contains 24 detected anomalies from adult patient records, with columns for age, height, and severity classifications (age_severity, height_severity, severity_level).

### Insights

The analysis detected 24 anomalies in what was intended to be a pediatric clinic database, but the data contained adult patients aged 21-118 years. Using pediatric thresholds (age ≤ 16 years, height ≤ 72 inches), all adult records were correctly identified as anomalies with severity levels ranging from moderate to severe. This demonstrates how threshold-based anomaly detection can serve as data quality control, identifying records that violate domain constraints and don't belong in the target dataset - in this case, adult patients mistakenly entered into a children's clinic system.

## 3. Signal Design

### Repository Link

[(clickable link to your repository)](https://github.com/KHenn22/cintel-03-signal-design)

### Signals

This module focuses on `aviation_signal_analysis.py`, which analyzes January 2025 on-time performance data for all carriers in the dataset from `data/airline_ontime_data_jan_2025.csv`.
- flights: total flights per carrier
- delayed: number of flights delayed by 15+ minutes or cancelled
- high_delay_alert: boolean flag when the carrier's delay rate exceeds 20%

### Artifacts

[artifacts/aviation_signals_jan_2025.csv](artifacts/aviation_signals_jan_2025.csv) contains the per-carrier delay summary and the high_delay_alert signal.

### Insights

Grouping by carrier and converting delay counts into a delay-rate alert makes it easier to identify higher delayed airlines at a glance. This aviation signal analysis shows how derived signals turn raw flight records into actionable monitoring output by flagging carriers with more than 20% delayed or cancelled flighs.

## 4. Rolling Monitoring

### Repository Link

[(clickable link to your repository)](https://github.com/KHenn22/cintel-04-rolling-monitoring)

### Techniques

The `airline_delay_rolling_monitor_hennelly.py` script aggregates daily flight data by carrier, then applies a 5-day rolling window per airline. It then computes rolling means and standard deviations for flights, cancellations, and average departure delay. Anomalies are flagged when cancellations or delay values exceed the rolling mean plus one standard deviation.

### Artifacts

[artifacts/airline_delay_rolling_metrics_hennelly.csv](artifacts/airline_delay_rolling_metrics_hennelly.csv) contains daily airline metrics, rolling statistics for each carrier, and boolean spike flags (`cancellation_spike_flag`, `delay_spike_flag`).

### Insights

Rolling monitoring shows how system behavior changes over time by comparing today’s airline metrics to the recent carrier-specific history instead of treating each day as independent.
- A rolling average reveals patterns that individual observations hide because it smooths short-term noise and highlights sustained deviations from recent normal behavior.
- By smoothing daily variation, the model can distinguish normal day-to-day volatility from true operational spikes in cancellations or departure delay.

For example, the `airline_delay_rolling_metrics_hennelly.csv` shows cancellation spikes across October 2025 for a number of airlines, demonstrating that the monitoring logic catches temporary disruptions in airline performance that raw daily counts alone would not make obvious.

## 5. Drift Detection

### Repository Link

[(clickable link to your repository)](https://github.com/KHenn22/cintel-05-drift-detection)

### Techniques

The `hennelly_drift_detector_percentage.py` script compares reference and current system metric datasets (`reference_metrics_hennelly.csv` and `current_metrics_hennelly.csv`). It summarizes each period with mean and median values for requests, errors, and total latency, then computes absolute differences and percent changes.

Drift is flagged when the mean or median difference exceeds the thresholds: 20 requests, 2 errors, or 1000ms latency.

### Artifacts

[artifacts/drift_summary_hennelly_percentage.csv](artifacts/drift_summary_hennelly_percentage.csv) contains the side-by-side reference/current summary, mean/median differences, percent changes, and drift flags.

[artifacts/drift_summary_long_hennelly_percentage.csv](artifacts/drift_summary_long_hennelly_percentage.csv) contains the same summary in a long-form, and easier-to-read row-per-field format.

### Insights

The drift detector found strong evidence of drift across the monitored metrics:
- Requests increased by about 28.22% from the reference period.
- Errors increased by about 173.91%.
- Total latency increased by about 47.85%.

All drift flags are true in the summary artifact, indicating that both mean and median comparisons exceed the defined thresholds for requests, errors, and latency. This demonstrates how comparing current behavior to a historical baseline helps identify meaningful performance changes that suggest the system is no longer operating in its expected range.

## 6. Continuous Intelligence Pipeline

### Repository Link

[(clickable link to your repository)](https://github.com/KHenn22/cintel-06-continuous-intelligence)

### Techniques

This pipeline is implemented by two scripts:
- `airport_filter_hennelly.py` filters all airport on-time CSV files under `data/` to extract only flights destined for STL, creating `data/stl_2025_ontime.csv`.
- `ontime_reporting_hennelly.py` reads the STL-specific dataset, computes a monthly on-time arrival signal (`pct_ontime_arr`), and classifies system state using three tiers: `STABLE` (>= 80%), `WARNING` (< 80% but >= 70%), and `DEGRADED` (< 70%).

The assessment connects earlier CI concepts by combining airport data filtering, signal design, anomaly detection, and system-state reasoning into a single end-to-end reporting workflow.

### Artifacts

[artifacts/ontime_assessment_hennelly.csv](artifacts/ontime_assessment_hennelly.csv) contains the monthly on-time arrival percentages for STL in 2025 and the derived system state classification.

### Assessment

The STL on-time reporting pipeline evaluates airport performance at the monthly level and labels each month as `STABLE`, `WARNING`, or `DEGRADED` based on whether the arrival on-time percentage meets the defined operational thresholds. This demonstrates how CI pipelines can turn filtered data and derived signals into a concise operational assessment for decision makers.
