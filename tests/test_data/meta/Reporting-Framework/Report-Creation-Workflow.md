### Report Creation Workflow

#### Description

The report creation workflow is how a report is actually created.

#### Workflow

::: mermaid
flowchart TD;

classDef default stroke:#808080,fill:#FFFFFF;

classDef blocked fill:#EF9A9A;
classDef design fill:#FFCC80;
classDef in_progress fill:#FFF59D;
classDef resolved fill:#A5D6A7;

prepare_environment:::design;
create_report_git_branch:::design;
has_cohort{has_cohort}:::design;
create_cohort_notebook:::design;
create_report_notebook:::design;
can_be_extract{can_be_extract}:::design;
create_pbi_report:::design;
create_extract:::design;
submit_pr:::design;
complete_pr:::design;
deliver_report:::design;

prepare_environment --> create_report_git_branch;
create_report_git_branch --> has_cohort;
has_cohort -->|True| create_cohort_notebook;
has_cohort -->|False| create_report_notebook;
create_cohort_notebook --> create_report_notebook;
create_report_notebook --> can_be_extract;
can_be_extract -->|True| create_extract;
can_be_extract -->|False| create_pbi_report;
create_pbi_report --> submit_pr;
create_extract --> submit_pr;
submit_pr --> complete_pr;
complete_pr --> deliver_report;
:::

### Prepare Environment

Get everything set up to do the work.

#### Output

- Reporting Environment

### Create Report Git Branch
- Specified from: Create Git Branch

Each report is tracked on a separate branch of the reports repository

#### Input

- Report ID

#### Output

- Git Branch

### Reporting Environment

The computing environment the reporting will be completed in.
