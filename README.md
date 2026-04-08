# cintel-06-continuous-intelligence

[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://denisecase.github.io/cintel-06-continuous-intelligence/)
[![CI Status](https://github.com/denisecase/cintel-06-continuous-intelligence/actions/workflows/ci-python-zensical.yml/badge.svg?branch=main)](https://github.com/denisecase/cintel-06-continuous-intelligence/actions/workflows/ci-python-zensical.yml)
[![Python 3.14+](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](#)
[![MIT](https://img.shields.io/badge/license-see%20LICENSE-yellow.svg)](./LICENSE)

> Professional Python project for continuous intelligence.

Continuous intelligence systems monitor data streams, detect change, and respond in real time.
This course builds those capabilities through working projects.

In the age of generative AI, durable skills are grounded in real work:
setting up a professional environment,
reading and running code,
understanding the logic,
and pushing work to a shared repository.
Each project follows the structure of professional Python projects.
We learn by doing.

## This Project

This project brings together several techniques used in continuous intelligence systems.

The goal is to copy this repository,
set up your environment,
run the example analysis,
and explore how monitoring techniques can be combined
to assess the current state of a system.

Run the example pipeline, read the code, and see how:

- raw system metrics are transformed into useful signals
- anomalies are detected in those signals
- monitoring results are summarized to assess system health

This project demonstrates how monitoring data can support operational awareness and decision-making.

This module serves as a capstone:
it encourages you to combine techniques developed
in earlier modules into a simple continuous intelligence pipeline:

- Module 2. anomaly detection
- Module 3. signal design
- Module 4. rolling monitoring
- Module 5. drift comparison
- Module 6. system assessment (integration).

## Data

The example pipeline reads system metrics from:

`data/system_metrics_case.csv`

Each row represents one observation of system activity.

The pipeline derives signals such as
**error rate** and **average latency**,
checks for anomalous conditions,
and produces a summary assessment of system behavior.

The dataset includes a short period of degraded performance
so that monitoring signals and anomaly detection
produce visible results.

## Working Files

You'll work with just these areas:

- **data/** - it starts with the data
- **docs/** - tell the story
- **src/cintel/** - where the magic happens
- **pyproject.toml** - update authorship & links
- **zensical.toml** - update authorship & links

## Instructions

Follow the [step-by-step workflow guide](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/) to complete:

1. Phase 1. **Start & Run**
2. Phase 2. **Change Authorship**
3. Phase 3. **Read & Understand**
4. Phase 4. **Modify**
5. Phase 5. **Apply**

## Challenges

Challenges are expected.
Sometimes instructions may not quite match your operating system.
When issues occur, share screenshots, error messages, and details about what you tried.
Working through issues is part of implementing professional projects.

## Success

After completing Phase 1. **Start & Run**, you'll have your own GitHub project, running on your machine, and running the example will print out:

```shell
========================
Pipeline executed successfully!
========================
```

And a new file named `project.log` will appear in the project folder.

## Command Reference

The commands below are used in the workflow guide above.
They are provided here for convenience.

Follow the guide for the **full instructions**.

<details>
<summary>Show command reference</summary>

### In a machine terminal (open in your `Repos` folder)

After you get a copy of this repo in your own GitHub account,
open a machine terminal in your `Repos` folder:

```shell
git clone https://github.com/KHenn22/cintel-06-continuous-intelligence

cd cintel-06-continuous-intelligence
code .
```

### In a VS Code terminal

```shell
uv self update
uv python pin 3.14
uv sync --extra dev --extra docs --upgrade

uvx pre-commit install
git add -A
uvx pre-commit run --all-files

uv run python -m cintel.continuous_intelligence_case

uv run ruff format .
uv run ruff check . --fix
uv run zensical build

git add -A
git commit -m "update"
git push -u origin main
```
</details>

## Make a Technical Modification

Added WARNING state to the system assessment.  This creates a three tier labeling: STABLE, WARNING, or DEGRADED.  The added WARNING label gives an earlier visibility into degrading performance before it becomes critical (DEGRADED).  The WARNING label was intentionally set low for this modification to ensure proper labeling of the .csv info.

## Custom Project - STL Airport On-Time Performance Pipeline

### What This Pipeline Does
This pipeline analyzes arrival on-time performance data for Lambert-St. Louis
International Airport (STL) from the Bureau of Transportation Statistics (BTS).
It reads monthly flight data, assesses STL's performance each month, and labels
each month as STABLE, WARNING, or DEGRADED based on on-time arrival percentage.  It strictly analyzes on-time performance solely on if a scheduled flight arrived within 15 minutes of a scheduled time.  It does not analyze the reason for the delay (i.e. if the delay actually started at the departure airport, was weather related, caused by a traffic management initiative, etc.).

### Data Source
Bureau of Transportation Statistics (BTS)
Reporting Carrier On-Time Performance (1987-present)
Fields: Year, Month, Dest, ArrDelayMinutes
Filtered to: STL (Lambert-St. Louis International Airport)
Time Period: 2025 (January - December)

### Thresholds
- STABLE: On-time arrival percentage >= 80%
- WARNING: On-time arrival percentage between 70% and 80%
- DEGRADED: On-time arrival percentage < 70%,
Note:  An arrival is considered on-time if it arrived within 15 minutes of its scheduled time.  This pipeline does not filter for the reason behind the delay.

### Previous Technical Modification
Added a three-tier assessment label (STABLE, WARNING, DEGRADED) to replace
the original two-tier system (STABLE, DEGRADED). This provides earlier
visibility into degrading airport performance before it becomes critical.

### How to Run
`uv run python -m cintel.ontime_reporting_hennelly`

### Output File
`artifacts/ontime_assessment_hennelly.csv`

## Notes

- Use the **UP ARROW** and **DOWN ARROW** in the terminal to scroll through past commands.
- Use `CTRL+f` to find (and replace) text within a file.
