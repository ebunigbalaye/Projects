# **Field Operations Task Tracker (CLI Tool)**

A lightweight command-line tool for managing and monitoring operational tasks in oil & gas field environments.

---

## **Problem Statement (Oil & Gas Context)**

Oil & gas field operations involve daily tasks across multiple sites—well inspections, pump checks, pipeline monitoring, maintenance jobs, safety rounds, and corrective actions.

These tasks are often tracked manually (paper, WhatsApp, spreadsheets), leading to:

* Missed maintenance activities
* Poor visibility on overdue or high-risk tasks
* Difficulty coordinating across multiple field locations
* No unified way to filter tasks by site, priority, or responsibility

**This tool solves that.**

---

## **What This Tool Does**

A simple Python CLI that allows operations teams to:

* **Add tasks** (name, description, assigned technician, site, priority, due date)
* **List tasks** in a clean, tabular format
* **Filter tasks** using optional flags (status, priority)


## **How It Works**

The tool stores tasks in a local JSONfile.
When the user runs a command:

1. Tasks are loaded from storage
2. Any filters (if provided) are applied
3. Results are printed in a formatted terminal table
All filters are optional.



# **Usage**
## **1. Add a New Task**

```bash
python main.py add \
  --name "Pump inspection" \
  --assigned "John Doe" \
  --site "Well 17" \
  --priority High \
  --due "2025-11-25" \
  --notes "Routine check on pump pressure"
```

---

## **2. List All Tasks**

```bash
python main.py view


# **🧠 How Oil & Gas Teams Would Use It**

* **Field supervisors** track daily assignments across wells, flowstations, compressor stations, or pipelines.
* **Technicians** update task statuses without needing a UI.
* **Maintenance leads** filter for overdue or high-priority items.
* **Shift teams** hand over tasks easily between shifts or crew rotations.

This mirrors real task workflows at Chevron, Shell, Oando, TotalEnergies, and NLNG.

