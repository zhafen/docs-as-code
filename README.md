# docs-as-code

## Overview

This project aims to create a Python package that allows any system or workflow to be concretely described and have human-readable documentation generated for that system.

## Functional Requirements

1. **Workflow Definition**: Define workflows in Python, which can be converted to Airflow DAGs.
2. **System Description**: Describe systems in Python, including organizational hierarchies and daily operations.
3. **Documentation Generation**: After defining a workflow or system precisely in Python, generate human-facing documentation that describes and visualizes how the system works.

## Design

The design of this package focuses on re-using as much code as possible from existing projects. The areas to pull from include:

- **Workflow Definition**: Airflow and other workflow orchestration tools.
- **System Definition**: Digital twins/IoT for system definition.
- **Data Storage**: Entity component systems and relational data.
- **Documentation**: Markdown and Mermaid for documentation.